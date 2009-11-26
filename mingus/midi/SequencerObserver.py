#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

================================================================================

        mingus - Music theory Python package, sequencer observer
    Copyright (C) 2008-2009, Bart Spaans

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

================================================================================

        Provides an easy to extend base class that can be used to observe
        a Sequencer. Each time a Sequencer starts playing a new Note, Bar, w/e,
        an event is fired; this SequencerObserver intercepts the event messages
        and calls the proper function so you only have to implement the \
functions
        for the events you need to see.

================================================================================
"""

from mingus.midi.Sequencer import Sequencer


class SequencerObserver:

    """ Provides an easy to extend base class that can be used to observe a \
Sequencer. Each time a Sequencer starts playing a new Note, Bar, w/e, an \
event is fired; this SequencerObserver intercepts the event messages and \
calls the proper function so you only have to implement the functions for \
the events you need to see."""

    # Low Level MIDI Events

    def play_int_note_event(
        self,
        int_note,
        channel,
        velocity,
        ):
        pass

    def stop_int_note_event(self, int_note, channel):
        pass

    def cc_event(
        self,
        channel,
        control,
        value,
        ):
        pass

    def instr_event(
        self,
        channel,
        instr,
        bank,
        ):
        pass

    def sleep(self, seconds):
        pass

    def play_Note(
        self,
        note,
        channel,
        velocity,
        ):
        pass

    def stop_Note(self, note, channel):
        pass

    def play_NoteContainer(self, notes, channel):
        pass

    def stop_NoteContainer(self, notes, channel):
        pass

    def play_Bar(
        self,
        bar,
        channel,
        bpm,
        ):
        pass

    def play_Bars(
        self,
        bars,
        channels,
        bpm,
        ):
        pass

    def play_Track(
        self,
        track,
        channel,
        bpm,
        ):
        pass

    def play_Tracks(
        self,
        tracks,
        channels,
        bpm,
        ):
        pass

    def play_Composition(
        self,
        composition,
        channels,
        bpm,
        ):
        pass

    def notify(self, msg_type, params):
        if msg_type == Sequencer.MSG_PLAY_INT:
            self.play_int_note_event(params['note'], params['channel'],
                                     params['velocity'])
        elif msg_type == Sequencer.MSG_STOP_INT:
            self.stop_int_note_event(params['note'], params['channel'])
        elif msg_type == Sequencer.MSG_CC:
            self.cc_event(params['channel'], params['control'], params['value'])
        elif msg_type == Sequencer.MSG_INSTR:
            self.instr_event(params['channel'], params['instr'], params['bank'])
        elif msg_type == Sequencer.MSG_SLEEP:
            self.sleep(params['s'])
        elif msg_type == Sequencer.MSG_PLAY_NOTE:
            self.play_Note(params['note'], params['channel'], params['velocity'
                           ])
        elif msg_type == Sequencer.MSG_STOP_NOTE:
            self.stop_Note(params['note'], params['channel'])
        elif msg_type == Sequencer.MSG_PLAY_NC:
            self.play_NoteContainer(params['notes'], params['channel'])
        elif msg_type == Sequencer.MSG_STOP_NC:
            self.stop_NoteContainer(params['notes'], params['channel'])
        elif msg_type == Sequencer.MSG_PLAY_BAR:
            self.play_Bar(params['bar'], params['channel'], params['bpm'])
        elif msg_type == Sequencer.MSG_PLAY_BARS:
            self.play_Bars(params['bars'], params['channels'], params['bpm'])
        elif msg_type == Sequencer.MSG_PLAY_TRACK:
            self.play_Track(params['track'], params['channel'], params['bpm'])
        elif msg_type == Sequencer.MSG_PLAY_TRACKS:
            self.play_Tracks(params['tracks'], params['channels'], params['bpm'
                             ])
        elif msg_type == Sequencer.MSG_PLAY_COMPOSITION:
            self.play_Composition(params['composition'], params['channels'],
                                  params['bpm'])


