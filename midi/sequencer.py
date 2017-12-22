#!/usr/bin/python
# -*- coding: utf-8 -*-

#    mingus - Music theory Python package, sequencer module.
#    Copyright (C) 2008-2009, Bart Spaans
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""A general purpose sequencer for the objects in mingus.containers.

You can use the Sequencer object either by creating a subclass and
implementing some of the events (init, play_event, stop_event, cc_event,
instr_event) or by attaching observer objects via 'attach' and catching the
messages in the notify(msg_type, param_dict) function of your object.

See SequencerObserver for a pre made, easy to extend base class that can be
attached to the Sequencer.
"""

from mingus.containers.instrument import MidiInstrument

class Sequencer(object):

    """A general purpose sequencer for the objects in mingus.containers.

    You can use the Sequencer object either by creating a subclass and
    implementing some of the events (init, play_event, stop_event, cc_event,
    instr_event) or by attaching observer objects via 'attach' and catching 
    the messages in the notify(msg_type, param_dict) function of your object.

    See SequencerObserver for a pre made, easy to extend base class that can
    be attached to the Sequencer.
    """

    output = None

    # Low level messages
    MSG_PLAY_INT = 0
    MSG_STOP_INT = 1
    MSG_CC = 2
    MSG_INSTR = 3
    MSG_SLEEP = 4

    # High level messages
    MSG_PLAY_NOTE = 5
    MSG_STOP_NOTE = 6
    MSG_PLAY_NC = 7
    MSG_STOP_NC = 8
    MSG_PLAY_BAR = 9
    MSG_PLAY_BARS = 10
    MSG_PLAY_TRACK = 11
    MSG_PLAY_TRACKS = 12
    MSG_PLAY_COMPOSITION = 13

    def __init__(self):
        self.listeners = []
        self.init()

        # Events Implement some of these functions when subclassing

    def init(self):
        pass

    def play_event(self, note, channel, velocity):
        pass

    def stop_event(self, note, channel):
        pass

    def cc_event(self, channel, control, value):
        pass

    def instr_event(self, channel, instr, bank):
        pass

    def sleep(self, seconds):
        pass

    def attach(self, listener):
        """Attach an object that should be notified of events.

        The object should have a notify(msg_type, param_dict) function.
        """
        if listener not in self.listeners:
            self.listeners.append(listener)

    def detach(self, listener):
        """Detach a listening object so that it won't receive any events
        anymore."""
        if listener in self.listeners:
            self.listeners.remove(listener)

    def notify_listeners(self, msg_type, params):
        """Send a message to all the observers."""
        for c in self.listeners:
            c.notify(msg_type, params)

    def set_instrument(self, channel, instr, bank=0):
        """Set the channel to the instrument _instr_."""
        self.instr_event(channel, instr, bank)
        self.notify_listeners(self.MSG_INSTR, {'channel': int(channel),
            'instr': int(instr), 'bank': int(bank)})

    def control_change(self, channel, control, value):
        """Send a control change message.

        See the MIDI specification for more information.
        """
        if control < 0 or control > 128:
            return False
        if value < 0 or value > 128:
            return False
        self.cc_event(channel, control, value)
        self.notify_listeners(self.MSG_CC, {'channel': int(channel),
            'control': int(control), 'value': int(value)})
        return True

    def play_Note(self, note, channel=1, velocity=100):
        """Play a Note object on a channel with a velocity[0-127].

        You can either specify the velocity and channel here as arguments or
        you can set the Note.velocity and Note.channel attributes, which
        will take presedence over the function arguments.
        """
        if hasattr(note, 'velocity'):
            velocity = note.velocity
        if hasattr(note, 'channel'):
            channel = note.channel
        self.play_event(int(note) + 12, int(channel), int(velocity))
        self.notify_listeners(self.MSG_PLAY_INT, {'channel': int(channel),
            'note': int(note) + 12, 'velocity': int(velocity)})
        self.notify_listeners(self.MSG_PLAY_NOTE, {'channel': int(channel),
            'note': note, 'velocity': int(velocity)})
        return True

    def stop_Note(self, note, channel=1):
        """Stop a note on a channel.

        If Note.channel is set, it will take presedence over the channel
        argument given here.
        """
        if hasattr(note, 'channel'):
            channel = note.channel
        self.stop_event(int(note) + 12, int(channel))
        self.notify_listeners(self.MSG_STOP_INT, {'channel': int(channel),
            'note': int(note) + 12})
        self.notify_listeners(self.MSG_STOP_NOTE, {'channel': int(channel),
            'note': note})
        return True

    def stop_everything(self):
        """Stop all the notes on all channels."""
        for x in range(118):
            for c in range(16):
                self.stop_Note(x, c)

    def play_NoteContainer(self, nc, channel=1, velocity=100):
        """Play the Notes in the NoteContainer nc."""
        self.notify_listeners(self.MSG_PLAY_NC, {'notes': nc,
            'channel': channel, 'velocity': velocity})
        if nc is None:
            return True
        for note in nc:
            if not self.play_Note(note, channel, velocity):
                return False
        return True

    def stop_NoteContainer(self, nc, channel=1):
        """Stop playing the notes in NoteContainer nc."""
        self.notify_listeners(self.MSG_PLAY_NC, {'notes': nc,
            'channel': channel})
        if nc is None:
            return True
        for note in nc:
            if not self.stop_Note(note, channel):
                return False
        return True

    def play_Bar(self, bar, channel=1, bpm=120):
        """Play a Bar object.

        Return a dictionary with the bpm lemma set on success, an empty dict
        on some kind of failure.

        The tempo can be changed by setting the bpm attribute on a
        NoteContainer.
        """
        self.notify_listeners(self.MSG_PLAY_BAR, {'bar': bar, 'channel'
                              : channel, 'bpm': bpm})

        # length of a quarter note
        qn_length = 60.0 / bpm
        for nc in bar:
            if not self.play_NoteContainer(nc[2], channel, 100):
                return {}

            # Change the quarter note length if the NoteContainer has a bpm
            # attribute
            if hasattr(nc[2], 'bpm'):
                bpm = nc[2].bpm
                qn_length = 60.0 / bpm
            ms = qn_length * (4.0 / nc[1])
            self.sleep(ms)
            self.notify_listeners(self.MSG_SLEEP, {'s': ms})
            self.stop_NoteContainer(nc[2], channel)
        return {'bpm': bpm}

    def play_Bars(self, bars, channels, bpm=120):
        """Play several bars (a list of Bar objects) at the same time.

        A list of channels should also be provided. The tempo can be changed
        by providing one or more of the NoteContainers with a bpm argument.
        """
        self.notify_listeners(self.MSG_PLAY_BARS, {'bars': bars,
            'channels': channels, 'bpm': bpm})
        qn_length = 60.0 / bpm  # length of a quarter note
        tick = 0.0  # place in beat from 0.0 to bar.length
        cur = [0] * len(bars)  # keeps the index of the NoteContainer under
                               # investigation in each of the bars
        playing = []  # The NoteContainers being played.

        while tick < bars[0].length:
            # Prepare a and play a list of NoteContainers that are ready for it.
            # The list `playing_new` holds both the duration and the
            # NoteContainer.
            playing_new = []
            for (n, x) in enumerate(cur):
                (start_tick, note_length, nc) = bars[n][x]
                if start_tick <= tick:
                    self.play_NoteContainer(nc, channels[n])
                    playing_new.append([note_length, n])
                    playing.append([note_length, nc, channels[n], n])

                    # Change the length of a quarter note if the NoteContainer
                    # has a bpm attribute
                    if hasattr(nc, 'bpm'):
                        bpm = nc.bpm
                        qn_length = 60.0 / bpm

            # Sort the list and sleep for the shortest duration
            if len(playing_new) != 0:
                playing_new.sort()
                shortest = playing_new[-1][0]
                ms = qn_length * (4.0 / shortest)
                self.sleep(ms)
                self.notify_listeners(self.MSG_SLEEP, {'s': ms})
            else:
                # If somehow, playing_new doesn't contain any notes (something
                # that shouldn't happen when the bar was filled properly), we
                # make sure that at least the notes that are still playing get
                # handled correctly.
                if len(playing) != 0:
                    playing.sort()
                    shortest = playing[-1][0]
                    ms = qn_length * (4.0 / shortest)
                    self.sleep(ms)
                    self.notify_listeners(self.MSG_SLEEP, {'s': ms})
                else:
                    # warning: this could lead to some strange behaviour. OTOH.
                    # Leaving gaps is not the way Bar works. should we do an
                    # integrity check on bars first?
                    return {}

            # Add shortest interval to tick
            tick += 1.0 / shortest

            # This final piece adjusts the duration in `playing` and checks if a
            # NoteContainer should be stopped.
            new_playing = []
            for (length, nc, chan, n) in playing:
                duration = 1.0 / length - 1.0 / shortest
                if duration >= 0.00001:
                    new_playing.append([1.0 / duration, nc, chan, n])
                else:
                    self.stop_NoteContainer(nc, chan)
                    if cur[n] < len(bars[n]) - 1:
                        cur[n] += 1
            playing = new_playing

        for p in playing:
            self.stop_NoteContainer(p[1], p[2])
            playing.remove(p)
        return {'bpm': bpm}

    def play_Track(self, track, channel=1, bpm=120):
        """Play a Track object."""
        self.notify_listeners(self.MSG_PLAY_TRACK, {'track': track, 'channel'
                              : channel, 'bpm': bpm})
        for bar in track:
            res = self.play_Bar(bar, channel, bpm)
            if res != {}:
                bpm = res['bpm']
            else:
                return {}
        return {'bpm': bpm}

    def play_Tracks(self, tracks, channels, bpm=120):
        """Play a list of Tracks.

        If an instance of MidiInstrument is used then the instrument will be
        set automatically.
        """
        self.notify_listeners(self.MSG_PLAY_TRACKS, {'tracks': tracks,
            'channels': channels, 'bpm': bpm})

        # Set the right instruments
        for x in range(len(tracks)):
            instr = tracks[x].instrument
            if isinstance(instr, MidiInstrument):
                try:
                    i = instr.names.index(instr.name)
                except:
                    i = 1
                self.set_instrument(channels[x], i)
            else:
                self.set_instrument(channels[x], 1)
        current_bar = 0
        max_bar = len(tracks[0])

        # Play the bars
        while current_bar < max_bar:
            playbars = []
            for tr in tracks:
                playbars.append(tr[current_bar])
            res = self.play_Bars(playbars, channels, bpm)
            if res != {}:
                bpm = res['bpm']
            else:
                return {}
            current_bar += 1
        return {'bpm': bpm}

    def play_Composition(self, composition, channels=None, bpm=120):
        """Play a Composition object."""
        self.notify_listeners(self.MSG_PLAY_COMPOSITION, {'composition'
                              : composition, 'channels': channels, 'bpm': bpm})
        if channels == None:
            channels = [x + 1 for x in range(len(composition.tracks))]
        return self.play_Tracks(composition.tracks, channels, bpm)

    def modulation(self, channel, value):
        """Set the modulation."""
        return self.control_change(channel, 1, value)

    def main_volume(self, channel, value):
        """Set the main volume."""
        return self.control_change(channel, 7, value)

    def pan(self, channel, value):
        """Set the panning."""
        return self.control_change(channel, 10, value)

