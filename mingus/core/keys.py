#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
================================================================================

    mingus - Music theory Python package, keys module.
    Copyright (C) 2010, Carlo Stemberger

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

def is_valid_key(key):
    """Return true if key is in a recognized format. False if not."""

    for couple in keys:
        if key in couple:
            return True
    return False

def get_key(number=0, token=''):
    """Return the tuple containing the major key corrensponding to the
    accidentals put as input, and his relative minor."""

    if number not in range(8):
        raise RangeError, 'Integer not in range 0-7.'
    if token == 'b':
        couple = 7 - number
    elif token == "#":
        couple = 7 + number
    elif token == '' and number == 0:
        couple = 7
    else:
        raise FormatError, "'%s' unrecognized: only 'b' and '#' admitted"\
                % token
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

