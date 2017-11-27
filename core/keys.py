#!/usr/bin/python
# -*- coding: utf-8 -*-

#    mingus - Music theory Python package, keys module.
#    Copyright (C) 2010-2011, Carlo Stemberger
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

"""Module for dealing with keys.

This module provides a simple interface for dealing with keys.
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

major_keys = [couple[0] for couple in keys]
minor_keys = [couple[1] for couple in keys]

base_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

_key_cache = {}

def is_valid_key(key):
    """Return True if key is in a recognized format. False if not."""
    for couple in keys:
        if key in couple:
            return True
    return False

def get_key(accidentals=0):
    """Return the key corrisponding to accidentals.

    Return the tuple containing the major key corrensponding to the
    accidentals put as input, and his relative minor; negative numbers for
    flats, positive numbers for sharps.
    """
    if accidentals not in range(-7, 8):
        raise RangeError('integer not in range (-7)-(+7).')
    return keys[accidentals+7]

def get_key_signature(key='C'):
    """Return the key signature.

    0 for C or a, negative numbers for flat key signatures, positive numbers
    for sharp key signatures.
    """
    if not is_valid_key(key):
        raise NoteFormatError("unrecognized format for key '%s'" % key)

    for couple in keys:
        if key in couple:
            accidentals = keys.index(couple) - 7
            return accidentals

def get_key_signature_accidentals(key='C'):
    """Return the list of accidentals present into the key signature."""
    accidentals = get_key_signature(key)
    res = []

    if accidentals < 0:
        for i in range(-accidentals):
            res.append('{0}{1}'.format(list(reversed(notes.fifths))[i], 'b'))
    elif accidentals > 0:
        for i in range(accidentals):
            res.append('{0}{1}'.format(notes.fifths[i], '#'))
    return res

def get_notes(key='C'):
    """Return an ordered list of the notes in this natural key.

    Examples:
    >>> get_notes('F')
    ['F', 'G', 'A', 'Bb', 'C', 'D', 'E']
    >>> get_notes('c')
    ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb']
    """
    if _key_cache.has_key(key):
        return _key_cache[key]
    if not is_valid_key(key):
        raise NoteFormatError("unrecognized format for key '%s'" % key)
    result = []

    # Calculate notes
    altered_notes = map(operator.itemgetter(0),
            get_key_signature_accidentals(key))

    if get_key_signature(key) < 0:
        symbol = 'b'
    elif get_key_signature(key) > 0:
        symbol = '#'

    raw_tonic_index = base_scale.index(key.upper()[0])

    for note in islice(cycle(base_scale), raw_tonic_index, raw_tonic_index+7):
        if note in altered_notes:
            result.append('%s%s' % (note, symbol))
        else:
            result.append(note)
    
    # Save result to cache
    _key_cache[key] = result
    return result

def relative_major(key):
    """Return the relative major of a minor key.

    Example:
    >>> relative_major('a')
    'C'
    """
    for couple in keys:
        if key == couple[1]:
            return couple[0]
    raise NoteFormatError("'%s' is not a minor key" % key)

def relative_minor(key):
    """Return the relative minor of a major key.

    Example:
    >>> relative_minor('C')
    'a'
    """
    for couple in keys:
        if key == couple[0]:
            return couple[1]
    raise NoteFormatError("'%s' is not a major key" % key)

class Key(object):

    """A key object."""

    def __init__(self, key='C'):
        self.key = key

        if self.key[0].islower():
            self.mode = 'minor'
        else:
            self.mode = 'major'
        
        try:
            symbol = self.key[1]
            if symbol == '#':
                symbol = 'sharp '
            else:
                symbol = 'flat '
        except:
            symbol = ''
        self.name = '{0} {1}{2}'.format(self.key[0].upper(), symbol, self.mode)

        self.signature = get_key_signature(self.key)

    def __eq__(self, other):
        if self.key == other.key:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

