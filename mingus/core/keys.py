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

#from mt_exceptions import NoteFormatError, RangeError
#import intervals
import notes

def is_valid_key(key):
    """Return true if key is in a recognized format. False if not."""

    return notes.is_valid_note(key.upper())

sharp_keys = [
        ('C', 'a'),   # 0
        ('G', 'e'),   # 1
        ('D', 'b'),   # 2
        ('A', 'f#'),  # 3
        ('E', 'c#'),  # 4
        ('B', 'g#'),  # 5
        ('F#', 'd#'), # 6
        ('C#', 'a#')  # 7
        ]

flat_keys = [
        ('C', 'a'),   # 0
        ('F', 'd'),   # 1
        ('Bb', 'g'),  # 2
        ('Eb', 'c'),  # 3
        ('Ab', 'f'),  # 4
        ('Db', 'bb'), # 5
        ('Gb', 'eb'), # 6
        ('Cb', 'ab')  # 7
        ]

