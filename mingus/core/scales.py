#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

================================================================================

    Music theory Python package, scales module
    Copyright (C) 2008-2009, Bart Spaans

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

    The scales module allows you to create a plethora of scales. Here's a
    little overview:

    === The diatonic scale and its modes ===
    * diatonic(note)
    * ionian(note)
    * dorian(note)
    * phrygian(note)
    * lydian(note)
    * mixolydian(note)
    * aeolian(note)
    * locrian(note)

    === The minor scales ===
    * natural_minor(note)
    * harmonic_minor(note)
    * melodic_minor(note)

    === Other scales ===
    * chromatic(note)
    * whole_note(note)
    * diminished(note)


================================================================================
"""

import intervals
import notes
from diatonic import get_notes

# The diatonic scales and its modes


def diatonic(note):
    """Returns the diatonic scale starting on note.
    Example:
{{{
>>> diatonic(\"C\")
[\"C\", \"D\", \"E\", \"F\", \"G\", \"A\", \"B\"]
}}}"""

    return get_notes(note)


def ionian(note):
    """Returns the ionian mode scale starting on note.
    Example:
{{{
>>> ionian(\"C\")
[\"C\", \"D\", \"E\", \"F\", \"G\", \"A\", \"B\"]
}}}"""

    return diatonic(note)


def dorian(note):
    """Returns the dorian mode scale starting on note.
    Example:
{{{
>>> dorian(\"D\")
[\"D\", \"E\", \"F\", \"G\", \"A\", \"B\", \"C\"]
}}}"""

    i = ionian(intervals.minor_seventh(note))
    return i[1:] + [i[0]]


def phrygian(note):
    """Returns the phrygian mode scale starting on note.
    Example:
{{{
>>> phrygian(\"E\")
[\"E\", \"F\", \"G\", \"A\", \"B\", \"C\", \"D\"]
}}}"""

    i = ionian(intervals.minor_sixth(note))
    return i[2:] + i[:2]


def lydian(note):
    """Returns the lydian mode scale starting on note.
    Example:
{{{
>>> lydian(\"F\")
[\"F\", \"G\", \"A\", B\", \"C\", \"D\", \"E\"]
}}}"""

    i = ionian(intervals.perfect_fifth(note))
    return i[3:] + i[:3]


def mixolydian(note):
    """Returns the mixolydian mode scale starting on note.
    Example:
{{{
>>> mixolydian(\"G\")
[\"G\", \"A\", \"B\", \"C\", \"D\", \"E\", \"F\"]
}}}"""

    i = ionian(intervals.perfect_fourth(note))
    return i[4:] + i[:4]


def aeolian(note):
    """Returns the aeolian mode scale starting on note.
    Example:
{{{
>>> aeolian(\"A\")
[\"A\", \"B\", \"C\", \"D\", \"E\", \"F\", \"G\"]
}}}"""

    i = ionian(intervals.minor_third(note))
    return i[5:] + i[:5]


def locrian(note):
    """Returns the locrian mode scale starting on note.
    Example:
{{{
>>> locrian(\"B\")
[\"B\", \"C\", \"D\", \"E\", \"F\", \"G\", \"A\"]
}}}"""

    i = ionian(intervals.minor_second(note))
    return i[6:] + i[:6]


# The minor modes


def natural_minor(note):
    """Returns the natural minor scale starting on note.
    Example:
{{{
>>> natural_minor(\"A\")
[\"A\", \"B\", \"C\", \"D\", \"E\", \"F\", \"G\"]
}}}"""

    s = get_notes(notes.to_major(note))
    return s[5:] + s[:5]


def harmonic_minor(note):
    """Returns the harmonic minor scale starting on note.
    Example:
{{{
>>> harmonic_minor(\"A\")
\"A\", \"B\", \"C\", \"D\", \"E\", \"F\", \"G#\"]
}}}"""

    nat = natural_minor(note)
    nat[6] = notes.augment(nat[6])
    return nat


def melodic_minor(note):
    """Returns the melodic minor scale starting on note.
    Example:
{{{
>>> melodic_minor(\"A\")
[\"A\", \"B\", \"C\", \"D\", \"E\", \"F#\", \"G#\"]
}}}"""

    har = harmonic_minor(note)
    har[5] = notes.augment(har[5])
    return har


# Other scales


def chromatic(note):
    return map(lambda x: intervals.get_interval(note, x), range(0, 12))


def whole_note(note):
    """Returns the whole note scale starting on note.
    Example:
{{{
>>> whole_note(\"C\")
[\"C\", \"D\", \"E\", \"F#\", \"G#\", \"A#\"]
}}}"""

    n = 0
    last = note
    res = [last]
    while n < 5:
        new = intervals.major_second(last)
        last = new
        res.append(new)
        n += 1
    return res


def diminished(note):
    """Returns the diminshed scale on note.
    Example:
{{{
>>> diminished(\"C\")
['C', 'D', 'Eb', 'F', 'Gb', 'Ab', 'A', 'B']
}}}"""

    def whole_step_half_step(n):
        res = [intervals.major_second(n), intervals.minor_third(n)]
        return res

    res = [note]
    for i in range(3):
        res += whole_step_half_step(note)
        note = res[-1]
    res = res + [intervals.major_seventh(res[0])]
    res[-2] = intervals.major_sixth(res[0])
    return res


def determine(scale):
    """Determines the kind of scale. Can recognize all the diatonic modes and the \
minor scales.
    Example:
{{{
>>> determine([\"C\", \"D\", \"E\", \"F\", \"G\", \"A\", \"B\"])
'C ionian'
}}}"""

    possible_result = [
        ['ionian', [
            'major second',
            'major third',
            'perfect fourth',
            'perfect fifth',
            'major sixth',
            'major seventh',
            ]],
        ['dorian', [
            'major second',
            'minor third',
            'perfect fourth',
            'perfect fifth',
            'major sixth',
            'minor seventh',
            ]],
        ['phrygian', [
            'minor second',
            'minor third',
            'perfect fourth',
            'perfect fifth',
            'minor sixth',
            'minor seventh',
            ]],
        ['lydian', [
            'major second',
            'major third',
            'major fourth',
            'perfect fifth',
            'major sixth',
            'major seventh',
            ]],
        ['mixolydian', [
            'major second',
            'major third',
            'perfect fourth',
            'perfect fifth',
            'major sixth',
            'minor seventh',
            ]],
        ['aeolian', [
            'major second',
            'minor third',
            'perfect fourth',
            'perfect fifth',
            'minor sixth',
            'minor seventh',
            ]],
        ['locrian', [
            'minor second',
            'minor third',
            'perfect fourth',
            'minor fifth',
            'minor sixth',
            'minor seventh',
            ]],
        ['natural minor', [
            'major second',
            'minor third',
            'perfect fourth',
            'perfect fifth',
            'minor sixth',
            'minor seventh',
            ]],
        ['harmonic minor', [
            'major second',
            'minor third',
            'perfect fourth',
            'perfect fifth',
            'minor sixth',
            'major seventh',
            ]],
        ['melodic minor', [
            'major second',
            'minor third',
            'perfect fourth',
            'perfect fifth',
            'major sixth',
            'major seventh',
            ]],
        ]
    tonic = scale[0]
    n = 0

    # -- Describing the algorithm: Filter out all the wrong answers in
    # possible_result

    for note in scale[1:]:

        # 1. Determine the interval

        intval = intervals.determine(tonic, note)
        a = 0
        temp = []

        # 2. Go through possible_result and add it to temp if it's a hit, do
        # nothing otherwise

        for x in possible_result:
            if x[1][n] == intval:
                temp.append(x)
        n += 1

        # 3. Set possible_result to temp

        possible_result = temp

    # Get the results from possible_result and return

    res = []
    for x in possible_result:
        res.append(scale[0] + ' ' + x[0])
    return res


