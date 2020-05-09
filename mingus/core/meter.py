# -*- coding: utf-8 -*-

#    mingus - Music theory Python package, meter module.
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

"""Module for dealing with meters.

A meter is represented by a tuple. 4/4 time would look like (4,4), 3/4 like
(3,4), etc.
"""
from __future__ import absolute_import

common_time = (4, 4)
cut_time = (2, 2)


def valid_beat_duration(duration):
    """Return True when log2(duration) is an integer."""
    if duration == 0:
        return False
    elif duration == 1:
        return True
    else:
        r = duration
        while r != 1:
            if r % 2 == 1:
                return False
            r /= 2
        return True


def is_valid(meter):
    """Return True if meter is a valid tuple representation of a meter.

    Examples for meters are (3,4) for 3/4, (4,4) for 4/4, etc.
    """
    return meter[0] > 0 and valid_beat_duration(meter[1])


def is_compound(meter):
    """Return True if meter is a compound meter, False otherwise.

    Examples:
    >>> is_compound((3,4))
    True
    >>> is_compound((4,4))
    False
    """
    return is_valid(meter) and meter[0] % 3 == 0 and 6 <= meter[0]


def is_simple(meter):
    """Return True if meter is a simple meter, False otherwise.

    Examples:
    >>> is_simple((3,4))
    True
    >>> is_simple((4,4))
    True
    """
    return is_valid(meter)


def is_asymmetrical(meter):
    """Return True if meter is an asymmetrical meter, False otherwise.

    Examples:
    >>> is_asymmetrical((3,4))
    True
    >>> is_asymmetrical((4,4))
    False
    """
    return is_valid(meter) and meter[0] % 2 == 1
