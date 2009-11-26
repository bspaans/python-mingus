#!/usr/bin/python
# -*- coding: utf-8 -*-

# Medieval backwards compatibility

"""

================================================================================

    Music theory Python package, note value module
    Copyright (C) 2008-2009, Bart Spaans, Javier Palanca

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

    A note value indicates the relative duration of a note. In mingus,
    note values are represented by floating point numbers.
    A quarter note is 4, because it stands for 1/4 note, an eighth note is 8
    because it stands for 1/8, a sixteenth note is 16, etc.
    These are all pretty straight forward, but how do you define a sixteenth
    triplet? Well, sixteenth triplets are made by taking an eighth note
    and deviding it in 3 equal parts. 1/8 times 1/3 = 1/24; so 24 is the number
    we want. How about a dotted eighth note? A dotted eighth note has the length
    of an eighth note plus half an eighth note. 1/8 + 1/16 = 3/16 = 1 / 16 / 3.
    So 16/3 is the number we are looking for.

    As you can see these calculations can be quite tiresome and can clutter
    up your code. This module is here to help do the conversion.

================================================================================
"""

longa = 0.25
breve = 0.5
semibreve = 1
minim = 2
crotchet = 4
quaver = 8
semiquaver = 16
demisemiquaver = 32
hemidemisemiquaver = 64

# British notation is hilarious

quasihemidemisemiquaver = 128
semihemidemisemiquaver = 128

# From the part of Europe that is traditionally sane with units:

whole = 1
half = 2
quarter = 4
eighth = 8
sixteenth = 16
thirty_second = 32
sixty_fourth = 64
hundred_twenty_eighth = 128

# MusicXML conversion table

musicxml = {
    1: 'whole',
    2: 'half',
    4: 'quarter',
    8: 'eighth',
    16: '16th',
    32: '32th',
    64: '64th',
    128: '128th',
    }
base_values = [
    0.25,
    0.5,
    1,
    2,
    4,
    8,
    16,
    32,
    64,
    128,
    ]
base_quintuplets = [
    0.3125,
    0.625,
    1.25,
    2.5,
    5,
    10,
    20,
    40,
    80,
    160,
    ]
base_triplets = [
    0.375,
    0.75,
    1.5,
    3,
    6,
    12,
    24,
    48,
    96,
    192,
    ]
base_septuplets = [
    0.4375,
    0.875,
    1.75,
    3.5,
    7,
    14,
    28,
    56,
    112,
    224,
    ]


def add(value1, value2):
    """Returns the value of the two combined.
{{{
>>> value.add(value.eighth, value.quarter)
2.6666666666666665
}}}"""

    return 1 / (1.0 / value1 + 1.0 / value2)


def subtract(value1, value2):
    """Returns the note value for value1 minus value2. There are no exceptions for \
producing negative values, which can be useful for taking differences.
{{{
>>> value.substract(value.quarter, value.eighth)
8.0
}}}"""

    return 1 / (1.0 / value1 - 1.0 / value2)


def dots(value, nr=1):
    """Returns the dotted note value. A dot adds half the duration of the note. A \
second dot adds half of what was added before, etc. So a dotted eighth note \
has the length of three sixteenth notes. An eighth note with two dots has \
the length of seven thirty second notes.
{{{
>>> value.dots(value.eighth)
5.3333333333333333
>>> value.dots(value.eighth, 2)
4.5714285714285712
>>> value.dots(value.quarter)
2.6666666666666665
}}}"""

    return (0.5 * value) / (1.0 - 0.5 ** (nr + 1))


def triplet(value):
    """Returns the triplet note value. A triplet divides the base value above into \
three parts. So a triplet eighth note is a third of a quarter note.
{{{
>>> value.triplet(value.eighth)
12
>>> value.triplet(4)
6
}}}"""

    return tuplet(value, 3, 2)


def quintuplet(value):
    """Returns the quintuplet note value. A quintuplet divides the base value _two_ \
above into five parts. So a quintuplet eighth note is a fifth of a half \
note.
{{{
>>> value.quintuplet(8)
10
>>> value.quintuplet(4)
5
}}}"""

    return tuplet(value, 5, 4)


def septuplet(value, in_fourths=True):
    """Returns the septuplet note value. The usage of a septuplet is ambigious: \
seven notes can be played either in the duration of four or eighth notes. If \
in_fourths is set to True, this function will use 4, otherwise 8 notes. So a \
septuplet eighth note is respectively either 14 or 7. Notice how \
`value.septuplet(8, False) == value.septuplet(4, True)`.
{{{
>>> value.septuplet(8)
14
>>> value.septuplet(8, False)
7
}}}"""

    if in_fourths:
        return tuplet(value, 7, 4)
    else:
        return tuplet(value, 7, 8)


def tuplet(value, rat1, rat2):
    """A tuplet can be written as a ratio. For example: 5:4 means that you play 5 \
notes in the duration of 4 (a quintuplet), 3:2 means that you play 3 notes \
in the duration of 2 (a triplet), etc. This function calculates the note \
value when playing in rat1:rat2.
{{{
>>> value.tuplet(8, 3, 2)
12
}}}"""

    return (rat1 * value) / float(rat2)


def determine(value):
    """Analyses the value and returns a tuple containing the parts it's made of. \
The tuple respectively consists of the base note value, the number of dots, \
and the ratio (see `tuplet`). For example:
{{{
>>> value.determine(8)
(8, 0, 1, 1)
>>> value.determine(12)
(8, 0, 3, 2)
>>> value.determine(14)
(8, 0, 7, 4)
}}}
This function recognizes all the base values, triplets, quintuplets, \
septuplets and up to four dots. The values are matched on range."""

    i = -2
    for v in base_values:
        if value == v:
            return (value, 0, 1, 1)
        if value < v:
            break
        i += 1
    scaled = float(value) / 2 ** i
    if scaled >= 0.9375:  # base value
        return (base_values[i], 0, 1, 1)
    elif scaled >= 0.8125:

                           # septuplet: scaled = 0.875

        return (base_values[i + 1], 0, 7, 4)
    elif scaled >= 17 / 24.0:

                            # triplet: scaled = 0.75

        return (base_values[i + 1], 0, 3, 2)
    elif scaled >= 31 / 48.0:

                            # dotted note (one dot): scaled = 2/3.0

        return (v, 1, 1, 1)
    elif scaled >= 67 / 112.0:

                              # quintuplet: scaled = 0.625

        return (base_values[i + 1], 0, 5, 4)
    d = 3
    for x in range(2, 5):
        d += 2 ** x
        if scaled == 2.0 ** x / d:
            return (v, x, 1, 1)
    return (base_values[i + 1], 0, 1, 1)


