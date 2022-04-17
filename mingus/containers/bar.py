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

from __future__ import absolute_import

import six

from mingus.containers import PercussionNote
from mingus.containers.mt_exceptions import MeterFormatError
from mingus.containers.note_container import NoteContainer
from mingus.core import meter as _meter
from mingus.core import progressions, keys
from typing import Optional

from mingus.containers.get_note_length import get_note_length, get_beat_start, get_bar_length


class Bar(object):
    """A bar object.

    A Bar is basically a container for NoteContainers. This is where NoteContainers
    get their duration.

    Each NoteContainer must start in the bar, but it can end outside the bar.

    Bars can be stored together with Instruments in Tracks.
    """
    def __init__(self, key="C", meter=(4, 4), bpm=120):
        # warning should check types
        if isinstance(key, six.string_types):
            key = keys.Key(key)
        self.key = key
        self.bpm = bpm
        self.set_meter(meter)
        self.empty()

    def empty(self):
        """Empty the Bar, remove all the NoteContainers."""
        self.bar = []  # list of [current_beat, note duration number, list of notes]
        self.current_beat = 0.0  # fraction of way through bar
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
            raise MeterFormatError(
                f"The meter argument {meter} is not an "
                "understood representation of a meter. "
                "Expecting a tuple."
            )

    def place_notes(self, notes, duration):
        """Place the notes on the current_beat.

        Notes can be strings, Notes, list of strings, list of Notes or a
        NoteContainer.

        Raise a MeterFormatError if the duration is not valid.

        Return True if successful, False otherwise if the note does not start in the bar.
        """
        # note should be able to be one of strings, lists, Notes or
        # NoteContainers
        if hasattr(notes, "notes"):
            pass
        elif hasattr(notes, "name"):
            notes = NoteContainer(notes)
        elif isinstance(notes, six.string_types):
            notes = NoteContainer(notes)
        elif isinstance(notes, list):
            notes = NoteContainer(notes)

        if self.is_full():
            return False
        else:
            self.bar.append([self.current_beat, duration, notes])
            self.current_beat += 1.0 / duration
            return True

    def place_rest(self, duration):
        """Place a rest of given duration on the current_beat.

        The same as place_notes(None, duration).
        """
        return self.place_notes(None, duration)

    @staticmethod
    def _is_note(note: Optional[NoteContainer]) -> bool:
        """
        Return whether the 'note' contained in a bar position is an actual NoteContainer.
        If False, it is a rest (currently represented by None).
        """
        return isinstance(note, NoteContainer)

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
        if _meter.valid_beat_duration(to):
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
        (min_note, max_note) = (100000, -1)
        for cont in self.bar:
            for note in cont[2]:
                if int(note) < int(min_note):
                    min_note = note
                elif int(note) > int(max_note):
                    max_note = note
        return min_note, max_note

    def space_left(self):
        """Return the space left on the Bar."""
        return self.length - self.current_beat

    def value_left(self):
        """Return the value left on the Bar."""
        return 1.0 / self.space_left()

    def augment(self):
        """Augment the NoteContainers in Bar."""
        for cont in self.bar:
            if self._is_note(cont[2]):
                cont[2].augment()

    def diminish(self):
        """Diminish the NoteContainers in Bar."""
        for cont in self.bar:
            if self._is_note(cont[2]):
                cont[2].diminish()

    def transpose(self, interval, up=True):
        """Transpose the notes in the bar up or down the interval.

        Call transpose() on all NoteContainers in the bar.
        """
        for cont in self.bar:
            if self._is_note(cont[2]):
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
            res.append(
                [
                    x[0],
                    progressions.determine(x[2].get_note_names(), self.key.key, shorthand),
                ]
            )
        return res

    def get_note_names(self):
        """Return a list of unique note names in the Bar."""
        res = []
        for cont in self.bar:
            for x in cont[2].get_note_names():
                if x not in res:
                    res.append(x)
        return res

    def play(self, start_time: int, bpm: float, channel: int, score: dict) -> int:
        """
        Put bar events into score.

        :param start_time: start time of bar in milliseconds
        :param bpm: beats per minute
        :param channel: channel number
        :param score: dict of events
        :return: duration of bar in milliseconds
        """
        assert type(start_time) == int

        for bar_fraction, duration_type, notes in self.bar:
            duration_ms = get_note_length(duration_type, self.meter[1], bpm)

            current_beat = bar_fraction * self.meter[1] + 1.0
            beat_start = get_beat_start(current_beat, bpm)
            start_key = start_time + beat_start
            end_key = start_key + duration_ms

            if notes:
                for note in notes:
                    score.setdefault(start_key, []).append(
                        {
                            'func': 'start_note',
                            'note': note,
                            'channel': channel,
                            'velocity': note.velocity
                        }
                    )

                    note_duration = getattr(note, 'duration', None)
                    if note_duration:
                        score.setdefault(start_key + note_duration, []).append(
                            {
                                'func': 'end_note',
                                'note': note,
                                'channel': channel,
                            }
                        )
                    elif not isinstance(note, PercussionNote):
                        score.setdefault(end_key, []).append(
                            {
                                'func': 'end_note',
                                'note': note,
                                'channel': channel,
                            }
                        )
                else:
                    pass
        return get_bar_length(self.meter, bpm)

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
        if hasattr(value, "notes"):
            pass
        elif hasattr(value, "name"):
            value = NoteContainer(value)
        elif isinstance(value, six.string_types):
            value = NoteContainer(value)
        elif isinstance(value, list):
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
        return self.bar == other.bar
