#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
================================================================================

    mingus - Music theory Python package, keys module.
    Copyright (C) 2010-2011, Carlo Stemberger

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

    This module [TODO].

================================================================================
"""

from mt_exceptions import FormatError, NoteFormatError, RangeError
import notes
import operator
from itertools import cycle, islice

keys = [
        ('Cb', 'ab'), #  7 b
        ('Gb', 'eb'), #  6 b
        ('Db', 'bb'), #  5 b
        ('Ab', 'f'),  #  4 b
        ('Eb', 'c'),  #  3 b
        ('Bb', 'g'),  #  2 b
        ('F', 'd'),   #  1 b
        ('C', 'a'),   #  nothing
        ('G', 'e'),   #  1 #
        ('D', 'b'),   #  2 #
        ('A', 'f#'),  #  3 #
        ('E', 'c#'),  #  4 #
        ('B', 'g#'),  #  5 #
        ('F#', 'd#'), #  6 #
        ('C#', 'a#')  #  7 #
        ]

base_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

_key_cache = {}

def is_valid_key(key):
    """Return true if key is in a recognized format. False if not."""

    for couple in keys:
        if key in couple:
            return True
    return False

def get_key(number=0, symbol=''):
    """Return the tuple containing the major key corrensponding to the
    accidentals put as input, and his relative minor."""

    if number not in range(8):
        raise RangeError, 'Integer not in range 0-7.'
    if symbol == 'b':
        couple = 7 - number
    elif symbol == "#":
        couple = 7 + number
    elif symbol == '' and number == 0:
        couple = 7
    else:
        raise FormatError, "'%s' unrecognized: only 'b' and '#' admitted"\
                % symbol
    return keys[couple]

def get_key_signature(key):
    """Return the key signature (None for C or a)."""

    if not is_valid_key(key):
        raise NoteFormatError, "Unrecognized format for key '%s'" % key

    for couple in keys:
        if key in couple:
            accidentals = keys.index(couple) - 7
            if accidentals > 0:
                return accidentals, '#'
            elif accidentals < 0:
                return -accidentals, 'b'

def get_key_signature_accidentals(key):
    """Return the list of accidentals present into the key signature."""
    accidentals = []
    try:
        number, symbol = get_key_signature(key)
    except:
        return accidentals
    if symbol == 'b':
        for i in range(number):
            accidentals.append((notes.fifths[::-1][i], symbol))
    elif symbol == '#':
        for i in range(number):
            accidentals.append((notes.fifths[i], symbol))
    return accidentals

def get_notes(key):
    """Return an ordered list of the notes in this natural key.

    For example: if the key is set to 'F', this function will return `['F',
    'G', 'A', 'Bb', 'C', 'D', 'E']`; if the key is set to 'c', `['C', 'D',
    'Eb', 'F', 'G', 'Ab', 'Bb']`.
    """

    if _key_cache.has_key(key):
        return _key_cache[key]
    if not is_valid_key(key):
        raise NoteFormatError, "Unrecognized format for key '%s'" % key
    result = []

    # Calculate notes
    accidentals = get_key_signature_accidentals(key)
    altered_notes = map(operator.itemgetter(0), accidentals)
    try:
        symbol = accidentals[0][1]
    except:
        pass
    raw_tonic_index = base_scale.index(key.upper()[0])
    for note in islice(cycle(base_scale), raw_tonic_index, raw_tonic_index+7):
        if note in altered_notes:
            result.append('%s%s' % (note, symbol))
        else:
            result.append(note)
    
    # Save result to cache
    _key_cache[key] = result
    return result

