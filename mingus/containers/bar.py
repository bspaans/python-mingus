#!/usr/bin/python
# -*- coding: utf-8 -*-

#    mingus - Music theory Python package, bar module.
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

from mingus.core import meter as _meter
from mingus.core import progressions, keys
from .note_container import NoteContainer
from .note import Note
from .mt_exceptions import MeterFormatError

class Bar(object):
    """A bar object.

    A Bar is basically a container for NoteContainers.

    Bars can be stored together with Instruments in Tracks.
    """

    key = 'C'
    meter = (4, 4)
    current_beat = 0.0
    length = 0.0
    bar = []

    def __init__(self, key='C', meter=(4, 4)):
        # warning should check types
        if type(key) == str:
            key = keys.Key(key)
        self.key = key
        self.set_meter(meter)
        self.empty()

    def empty(self):
        """Empty the Bar, remove all the NoteContainers."""
        self.bar = []
        self.current_beat = 0.0
        return self.bar

    def set_meter(self, meter):
        """Set the meter of this bar.

        Meters in mingus are represented by a single tuple.

        If the format of the meter is not recognised, a MeterFormatError
        will be raised.
        """
        # warning should raise exception
        if _meter.valid_beat_duration(meter[1]):
            self.meter = (meter[0], meter[1])
            self.length = meter[0] * (1.0 / meter[1])
        elif meter == (0, 0):
            self.meter = (0, 0)
            self.length = 0.0
        else:
            raise MeterFormatError("The meter argument '%s' is not an "
                    "understood representation of a meter. "
                    "Expecting a tuple." % meter)

    def place_notes(self, notes, duration):
        """Place the notes on the current_beat.

        Notes can be strings, Notes, list of strings, list of Notes or a
        NoteContainer.

        Raise a MeterFormatError if the duration is not valid.

        Return True if succesful, False otherwise (ie. the Bar hasn't got
        enough room for a note of that duration).
        """
        # note should be able to be one of strings, lists, Notes or
        # NoteContainers
        if hasattr(notes, 'notes'):
            pass
        elif hasattr(notes, 'name'):
            notes = NoteContainer(notes)
        elif type(notes) == str:
            notes = NoteContainer(notes)
        elif type(notes) == list:
            notes = NoteContainer(notes)
        if self.current_beat + 1.0 / duration <= self.length or self.length\
             == 0.0:
            self.bar.append([self.current_beat, duration, notes])
            self.current_beat += 1.0 / duration
            return True
        else:
            return False

    def place_notes_at(self, notes, at):
        """Place notes at the given index."""
        for x in self.bar:
            if x[0] == at:
                x[0][2] += notes

    def place_rest(self, duration):
        """Place a rest of given duration on the current_beat.

        The same as place_notes(None, duration).
        """
        return self.place_notes(None, duration)

    def remove_last_entry(self):
        """Remove the last NoteContainer in the Bar."""
        self.current_beat -= 1.0 / self.bar[-1][1]
        self.bar = self.bar[:-1]
        return self.current_beat

    def is_full(self):
        """Return False if there is room in this Bar for another
        NoteContainer, True otherwise."""
        if self.length == 0.0:
            return False
        if len(self.bar) == 0:
            return False
        if self.current_beat >= self.length - 0.001:
            return True
        return False

    def change_note_duration(self, at, to):
        """Change the note duration at the given index to the given
        duration."""
        if valid_beat_duration(to):
            diff = 0
            for x in self.bar:
                if diff != 0:
                    x[0][0] -= diff
                if x[0] == at:
                    cur = x[0][1]
                    x[0][1] = to
                    diff = 1 / cur - 1 / to

    def get_range(self):
        """Return the highest and the lowest note in a tuple."""
        (min, max) = (100000, -1)
        for cont in self.bar:
            for note in cont[2]:
                if int(note) < int(min):
                    min = note
                elif int(note) > int(max):
                    max = note
        return (min, max)

    def space_left(self):
        """Return the space left on the Bar."""
        return self.length - self.current_beat

    def value_left(self):
        """Return the value left on the Bar."""
        return 1.0 / self.space_left()

    def augment(self):
        """Augment the NoteContainers in Bar."""
        for cont in self.bar:
            cont[2].augment()

    def diminish(self):
        """Diminish the NoteContainers in Bar."""
        for cont in self.bar:
            cont[2].diminish()

    def transpose(self, interval, up=True):
        """Transpose the notes in the bar up or down the interval.

        Call transpose() on all NoteContainers in the bar.
        """
        for cont in self.bar:
            cont[2].transpose(interval, up)

    def determine_chords(self, shorthand=False):
        """Return a list of lists [place_in_beat, possible_chords]."""
        chords = []
        for x in self.bar:
            chords.append([x[0], x[2].determine(shorthand)])
        return chords

    def determine_progression(self, shorthand=False):
        """Return a list of lists [place_in_beat, possible_progressions]."""
        res = []
        for x in self.bar:
            res.append([x[0], progressions.determine(x[2].get_note_names(),
                       self.key.key, shorthand)])
        return res

    def get_note_names(self):
        """Return a list of unique note names in the Bar."""
        res = []
        for cont in self.bar:
            for x in cont[2].get_note_names():
                if x not in res:
                    res.append(x)
        return res

    def __add__(self, note_container):
        """Enable the '+' operator on Bars."""
        if self.meter[1] != 0:
            return self.place_notes(note_container, self.meter[1])
        else:
            return self.place_notes(note_container, 4)

    def __getitem__(self, index):
        """Enable the  '[]' notation on Bars to get the item at the index."""
        return self.bar[index]

    def __setitem__(self, index, value):
        """Enable the use of [] = notation on Bars.

        The value should be a NoteContainer, or a string/list/Note
        understood by the NoteContainer.
        """
        if hasattr(value, 'notes'):
            pass
        elif hasattr(value, 'name'):
            value = NoteContainer(value)
        elif type(value) == str:
            value = NoteContainer(value)
        elif type(value) == list:
            res = NoteContainer()
            for x in value:
                res + x
            value = res
        self.bar[index][2] = value

    def __repr__(self):
        """Enable str() and repr() for Bars."""
        return str(self.bar)

    def __len__(self):
        """Enable the len() method for Bars."""
        return len(self.bar)

    def __eq__(self, other):
        """Enable the '==' operator for Bars."""
        for b in range(0, len(self.bar) - 1):
            if self.bar[b] != other.bar[b]:
                return False
        return True

