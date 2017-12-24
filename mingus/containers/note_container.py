#!/usr/bin/python
# -*- coding: utf-8 -*-

#    mingus - Music theory Python package, note_container module.
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

from .note import Note
from mingus.core import intervals, chords, progressions
from .mt_exceptions import UnexpectedObjectError

class NoteContainer(object):

    """A container for notes.

    The NoteContainer provides a container for the mingus.containers.Note
    objects.

    It can be used to store single and multiple notes and is required for
    working with Bars.
    """

    notes = []

    def __init__(self, notes=[]):
        self.empty()
        self.add_notes(notes)

    def empty(self):
        """Empty the container."""
        self.notes = []

    def add_note(self, note, octave=None, dynamics={}):
        """Add a note to the container and sorts the notes from low to high.

        The note can either be a string, in which case you could also use
        the octave and dynamics arguments, or a Note object.
        """
        if type(note) == str:
            if octave is not None:
                note = Note(note, octave, dynamics)
            elif len(self.notes) == 0:
                note = Note(note, 4, dynamics)
            else:
                if Note(note, self.notes[-1].octave) < self.notes[-1]:
                    note = Note(note, self.notes[-1].octave + 1, dynamics)
                else:
                    note = Note(note, self.notes[-1].octave, dynamics)
        if not hasattr(note, 'name'):
            raise UnexpectedObjectError("Object '%s' was not expected. "
                    "Expecting a mingus.containers.Note object." % note)
        if note not in self.notes:
            self.notes.append(note)
            self.notes.sort()
        return self.notes

    def add_notes(self, notes):
        """Feed notes to self.add_note.

        The notes can either be an other NoteContainer, a list of Note
        objects or strings or a list of lists formatted like this:
        >>> notes = [['C', 5], ['E', 5], ['G', 6]]

        or even:
        >>> notes = [['C', 5, {'volume': 20}], ['E', 6, {'volume': 20}]]
        """
        if hasattr(notes, 'notes'):
            for x in notes.notes:
                self.add_note(x)
            return self.notes
        elif hasattr(notes, 'name'):
            self.add_note(notes)
            return self.notes
        elif type(notes) == str:
            self.add_note(notes)
            return self.notes
        for x in notes:
            if type(x) == list and len(x) != 1:
                if len(x) == 2:
                    self.add_note(x[0], x[1])
                else:
                    self.add_note(x[0], x[1], x[2])
            else:
                self.add_note(x)
        return self.notes

    def from_chord(self, shorthand):
        """Shortcut to from_chord_shorthand."""
        return self.from_chord_shorthand(shorthand)

    def from_chord_shorthand(self, shorthand):
        """Empty the container and add the notes in the shorthand.

        See mingus.core.chords.from_shorthand for an up to date list of
        recognized format.

        Example:
        >>> NoteContainer().from_chord_shorthand('Am')
        ['A-4', 'C-5', 'E-5']
        """
        self.empty()
        self.add_notes(chords.from_shorthand(shorthand))
        return self

    def from_interval(self, startnote, shorthand, up=True):
        """Shortcut to from_interval_shorthand."""
        return self.from_interval_shorthand(startnote, shorthand, up)

    def from_interval_shorthand(self, startnote, shorthand, up=True):
        """Empty the container and add the note described in the startnote and
        shorthand.

        See core.intervals for the recognized format.

        Examples:
        >>> nc = NoteContainer()
        >>> nc.from_interval_shorthand('C', '5')
        ['C-4', 'G-4']
        >>> nc.from_interval_shorthand('C', '5', False)
        ['F-3', 'C-4']
        """
        self.empty()
        if type(startnote) == str:
            startnote = Note(startnote)
        n = Note(startnote.name, startnote.octave, startnote.dynamics)
        n.transpose(shorthand, up)
        self.add_notes([startnote, n])
        return self

    def from_progression(self, shorthand, key='C'):
        """Shortcut to from_progression_shorthand."""
        return self.from_progression_shorthand(shorthand, key)

    def from_progression_shorthand(self, shorthand, key='C'):
        """Empty the container and add the notes described in the progressions
        shorthand (eg. 'IIm6', 'V7', etc).

        See mingus.core.progressions for all the recognized format.

        Example:
        >>> NoteContainer().from_progression_shorthand('VI')
        ['A-4', 'C-5', 'E-5']
        """
        self.empty()
        chords = progressions.to_chords(shorthand, key)
        # warning Throw error, not a valid shorthand

        if chords == []:
            return False
        notes = chords[0]
        self.add_notes(notes)
        return self

    def _consonance_test(self, testfunc, param=None):
        """Private function used for testing consonance/dissonance."""
        n = list(self.notes)
        while len(n) > 1:
            first = n[0]
            for second in n[1:]:
                if param is None:
                    if not testfunc(first.name, second.name):
                        return False
                else:
                    if not testfunc(first.name, second.name, param):
                        return False
            n = n[1:]
        return True

    def is_consonant(self, include_fourths=True):
        """Test whether the notes are consonants.

        See the core.intervals module for a longer description on
        consonance.
        """
        return self._consonance_test(intervals.is_consonant, include_fourths)

    def is_perfect_consonant(self, include_fourths=True):
        """Test whether the notes are perfect consonants.

        See the core.intervals module for a longer description on
        consonance.
        """
        return self._consonance_test(intervals.is_perfect_consonant,
                include_fourths)

    def is_imperfect_consonant(self):
        """Test whether the notes are imperfect consonants.

        See the core.intervals module for a longer description on
        consonance.
        """
        return self._consonance_test(intervals.is_imperfect_consonant)

    def is_dissonant(self, include_fourths=False):
        """Test whether the notes are dissonants.

        See the core.intervals module for a longer description.
        """
        return not self.is_consonant(not include_fourths)

    def remove_note(self, note, octave=-1):
        """Remove note from container.

        The note can either be a Note object or a string representing the
        note's name. If no specific octave is given, the note gets removed
        in every octave.
        """
        res = []
        for x in self.notes:
            if type(note) == str:
                if x.name != note:
                    res.append(x)
                else:
                    if x.octave != octave and octave != -1:
                        res.append(x)
            else:
                if x != note:
                    res.append(x)
        self.notes = res
        return res

    def remove_notes(self, notes):
        """Remove notes from the containers.

        This function accepts a list of Note objects or notes as strings and
        also single strings or Note objects.
        """
        if type(notes) == str:
            return self.remove_note(notes)
        elif hasattr(notes, 'name'):
            return self.remove_note(notes)
        else:
            list(map(lambda x: self.remove_note(x), notes))
            return self.notes

    def remove_duplicate_notes(self):
        """Remove duplicate and enharmonic notes from the container."""
        res = []
        for x in self.notes:
            if x not in res:
                res.append(x)
        self.notes = res
        return res

    def sort(self):
        """Sort the notes in the container from low to high."""
        self.notes.sort()

    def augment(self):
        """Augment all the notes in the NoteContainer."""
        for n in self.notes:
            n.augment()

    def diminish(self):
        """Diminish all the notes in the NoteContainer."""
        for n in self.notes:
            n.diminish()

    def determine(self, shorthand=False):
        """Determine the type of chord or interval currently in the
        container."""
        return chords.determine(self.get_note_names(), shorthand)

    def transpose(self, interval, up=True):
        """Transpose all the notes in the container up or down the given
        interval."""
        for n in self.notes:
            n.transpose(interval, up)
        return self

    def get_note_names(self):
        """Return a list with all the note names in the current container.

        Every name will only be mentioned once.
        """
        res = []
        for n in self.notes:
            if n.name not in res:
                res.append(n.name)
        return res

    def __repr__(self):
        """Return a nice and clean string representing the note container."""
        return str(self.notes)

    def __getitem__(self, item):
        """Enable the use of the container as a simple array.

        Example:
        >>> n = NoteContainer(['C', 'E', 'G'])
        >>> n[0]
        'C-4'
        """
        return self.notes[item]

    def __setitem__(self, item, value):
        """Enable the use of the [] notation on NoteContainers.

        This function accepts Notes and notes as string.

        Example:
        >>> n = NoteContainer(['C', 'E', 'G'])
        >>> n[0] = 'B'
        >>> n
        ['B-4', 'E-4', 'G-4']
        """
        if type(value) == str:
            n = Note(value)
            self.notes[item] = n
        else:
            self.notes[item] = value
        return self.notes

    def __add__(self, notes):
        """Enable the use of the '+' operator on NoteContainers.

        Example:
        >>> n = NoteContainer(['C', 'E', 'G'])
        >>> n + 'B'
        ['C-4', 'E-4', 'G-4', 'B-4']
        """
        self.add_notes(notes)
        return self

    def __sub__(self, notes):
        """Enable the use of the '-' operator on NoteContainers.

        Example:
        >>> n = NoteContainer(['C', 'E', 'G'])
        >>> n - 'E'
        ['C-4', 'G-4']
        """
        self.remove_notes(notes)
        return self

    def __len__(self):
        """Return the number of notes in the container."""
        return len(self.notes)

    def __eq__(self, other):
        """Enable the '==' operator for NoteContainer instances."""
        for x in self:
            if x not in other:
                return False
        return True

