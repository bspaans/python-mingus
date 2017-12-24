#!/usr/bin/python
# -*- coding: utf-8 -*-

#    mingus - Music theory Python package, track module.
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

from mt_exceptions import InstrumentRangeError
from mingus.containers.note_container import NoteContainer
from mingus.containers.bar import Bar
import mingus.core.value as value

class Track(object):

    """A track object.

    The Track class can be used to store Bars and to work on them.

    The class is also designed to be used with Instruments, but this is
    optional.

    Tracks can be stored together in Compositions.
    """

    bars = []
    instrument = None
    name = 'Untitled'  # Will be looked for when saving a MIDI file.
    tuning = None  # Used by tablature

    def __init__(self, instrument=None):
        self.bars = []
        self.instrument = instrument

    def add_bar(self, bar):
        """Add a Bar to the current track."""
        self.bars.append(bar)
        return self

    def add_notes(self, note, duration=None):
        """Add a Note, note as string or NoteContainer to the last Bar.

        If the Bar is full, a new one will automatically be created.

        If the Bar is not full but the note can't fit in, this method will
        return False. True otherwise.

        An InstrumentRangeError exception will be raised if an Instrument is
        attached to the Track, but the note turns out not to be within the
        range of the Instrument.
        """
        if self.instrument != None:
            if not self.instrument.can_play_notes(note):
                raise InstrumentRangeError, \
                    "Note '%s' is not in range of the instrument (%s)" % (note,
                        self.instrument)
        if duration == None:
            duration = 4

        # Check whether the last bar is full, if so create a new bar and add the
        # note there
        if len(self.bars) == 0:
            self.bars.append(Bar())
        last_bar = self.bars[-1]
        if last_bar.is_full():
            self.bars.append(Bar(last_bar.key, last_bar.meter))
            # warning should hold note if it doesn't fit

        return self.bars[-1].place_notes(note, duration)

    def get_notes(self):
        """Return an iterator that iterates through every bar in the this
        track."""
        for bar in self.bars:
            for beat, duration, notes in bar:
                yield beat, duration, notes 

    def from_chords(self, chords, duration=1):
        """Add chords to the Track.

        The given chords should be a list of shorthand strings or list of
        list of shorthand strings, etc.

        Each sublist divides the value by 2.

        If a tuning is set, chords will be expanded so they have a proper
        fingering.

        Example:
        >>> t = Track().from_chords(['C', ['Am', 'Dm'], 'G7', 'C#'], 1)
        """
        tun = self.get_tuning()

        def add_chord(chord, duration):
            if type(chord) == list:
                for c in chord:
                    add_chord(c, duration * 2)
            else:
                chord = NoteContainer().from_chord(chord)
                if tun:
                    chord = tun.find_chord_fingering(chord,
                            return_best_as_NoteContainer=True)
                if not self.add_notes(chord, duration):
                    # This should be the standard behaviour of add_notes
                    dur = self.bars[-1].value_left()
                    self.add_notes(chord, dur)

                    # warning should hold note
                    self.add_notes(chord, value.subtract(duration, dur))

        for c in chords:
            if c is not None:
                add_chord(c, duration)
            else:
                self.add_notes(None, duration)
        return self

    def get_tuning(self):
        """Return a StringTuning object.

        If an instrument is set and has a tuning it will be returned.
        Otherwise the track's one will be used.
        """
        if self.instrument and self.instrument.tuning:
            return self.instrument.tuning
        return self.tuning

    def set_tuning(self, tuning):
        """Set the tuning attribute on both the Track and its instrument (when
        available).

        Tuning should be a StringTuning or derivative object.
        """
        if self.instrument:
            self.instrument.tuning = tuning
        self.tuning = tuning
        return self

    def transpose(self, interval, up=True):
        """Transpose all the notes in the track up or down the interval.

        Call transpose() on every Bar.
        """
        for bar in self.bars:
            bar.transpose(interval, up)
        return self

    def augment(self):
        """Augment all the bars in the Track."""
        for bar in self.bars:
            bar.augment()
        return self

    def diminish(self):
        """Diminish all the bars in the Track."""
        for bar in self.bars:
            bar.diminish()
        return self

    def __add__(self, value):
        """Enable the '+' operator for Tracks.

        Notes, notes as string, NoteContainers and Bars accepted.
        """
        if hasattr(value, 'bar'):
            return self.add_bar(value)
        elif hasattr(value, 'notes'):
            return self.add_notes(value)
        elif hasattr(value, 'name') or type(value) == str:
            return self.add_notes(value)

    def test_integrity(self):
        """Test whether all but the last Bars contained in this track are
        full."""
        for b in self.bars[:-1]:
            if not b.is_full():
                return False
        return True

    def __eq__(self, other):
        """Enable the '==' operator for tracks."""
        for x in range(0, len(self.bars) - 1):
            if self.bars[x] != other.bars[x]:
                return False
        return True

    def __getitem__(self, index):
        """Enable the '[]' notation for Tracks."""
        return self.bars[index]

    def __setitem__(self, index, value):
        """Enable the '[] =' notation for Tracks.

        Throw an UnexpectedObjectError if the value being set is not a
        mingus.containers.Bar object.
        """
        if not hasattr(value, 'bar'):
            raise UnexpectedObjectError("Unexpected object '%s', "
                    "expecting a mingus.containers.Barobject" % value)
        self.bars[index] = value

    def __repr__(self):
        """Return a string representing the class."""
        return str([self.instrument, self.bars])

    def __len__(self):
        """Enable the len() function for Tracks."""
        return len(self.bars)

