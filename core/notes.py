#!/usr/bin/python
# -*- coding: utf-8 -*-

#    mingus - Music theory Python package, notes module.
#    Copyright (C) 2008-2009, Bart Spaans
#    Copyright (C) 2011, Carlo Stemberger
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

"""Basic module for notes.

This module is the foundation of the music theory package.

It handles conversions from integers to notes and vice versa and thus
enables simple calculations.
"""

from .mt_exceptions import NoteFormatError, RangeError, FormatError

_note_dict = {
    'C': 0,
    'D': 2,
    'E': 4,
    'F': 5,
    'G': 7,
    'A': 9,
    'B': 11
    }
fifths = ['F', 'C', 'G', 'D', 'A', 'E', 'B']

def int_to_note(note_int, accidentals='#'):
    """Convert integers in the range of 0-11 to notes in the form of C or C#
    or Db.

    Throw a RangeError exception if the note_int is not in the range 0-11.

    If not specified, sharps will be used.

    Examples:
    >>> int_to_note(0)
    'C'
    >>> int_to_note(3)
    'D#'
    >>> int_to_note(3, 'b')
    'Eb'
    """
    if note_int not in list(range(12)):
        raise RangeError('int out of bounds (0-11): %d' % note_int)
    ns = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    nf = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
    if accidentals == '#':
        return ns[note_int]
    elif accidentals == 'b':
        return nf[note_int]
    else:
        raise FormatError("'%s' not valid as accidental" % accidentals)

def is_enharmonic(note1, note2):
    """Test whether note1 and note2 are enharmonic, i.e. they sound the same."""
    return note_to_int(note1) == note_to_int(note2)

def is_valid_note(note):
    """Return True if note is in a recognised format. False if not."""
    if note[0] not in _note_dict:
        return False
    for post in note[1:]:
        if post != 'b' and post != '#':
            return False
    return True

def note_to_int(note):
    """Convert notes in the form of C, C#, Cb, C##, etc. to an integer in the
    range of 0-11.

    Throw a NoteFormatError exception if the note format is not recognised.
    """
    if is_valid_note(note):
        val = _note_dict[note[0]]
    else:
        raise NoteFormatError("Unknown note format '%s'" % note)

    # Check for '#' and 'b' postfixes
    for post in note[1:]:
        if post == 'b':
            val -= 1
        elif post == '#':
            val += 1
    return val % 12

def reduce_accidentals(note):
    """Reduce any extra accidentals to proper notes.

    Example:
    >>> reduce_accidentals('C####')
    'E'
    """
    val = note_to_int(note[0])
    for token in note[1:]:
        if token == 'b':
            val -= 1
        elif token == '#':
            val += 1
        else:
            raise NoteFormatError("Unknown note format '%s'" % note)
    if val >= note_to_int(note[0]):
        return int_to_note(val%12)
    else:
        return int_to_note(val%12, 'b')

def remove_redundant_accidentals(note):
    """Remove redundant sharps and flats from the given note.

    Examples:
    >>> remove_redundant_accidentals('C##b')
    'C#'
    >>> remove_redundant_accidentals('Eb##b')
    'E'
    """
    val = 0
    for token in note[1:]:
        if token == 'b':
            val -= 1
        elif token == '#':
            val += 1
    result = note[0]
    while val > 0:
        result = augment(result)
        val -= 1
    while val < 0:
        result = diminish(result)
        val += 1
    return result

def augment(note):
    """Augment a given note.

    Examples:
    >>> augment('C')
    'C#'
    >>> augment('Cb')
    'C'
    """
    if note[-1] != 'b':
        return note + '#'
    else:
        return note[:-1]

def diminish(note):
    """Diminish a given note.

    Examples:
    >>> diminish('C')
    'Cb'
    >>> diminish('C#')
    'C'
    """
    if note[-1] != '#':
        return note + 'b'
    else:
        return note[:-1]

