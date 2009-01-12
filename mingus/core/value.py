"""

================================================================================

	Music theory Python package, note value module
	Copyright (C) 2008, Bart Spaans

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
	A quarter note is 4, because it stands for 1/4 note, an eight note is 8
	because it stands for 1/8, a sixteenth note is 16, etc.
	These are all pretty straight forward, but how do you define a sixteenth 
	triplet? Well, sixteenth triplets are made by taking an eight note 
	and deviding it in 3 equal parts. 1/8 * 1/3 = 1/24; so 24 is the number 
	we want. How about a dotted eight note? A dotted eight note has the length
	of an eight note plus half an eight note. 1/8 + 1/16 = 3/16 = 1 / 16 / 3.
	So 16/3 is the number we are looking for. 

	As you can see these calculations can be quite tiresome and can clutter 
	up your code. This module is here to help do the conversion.

================================================================================

"""

# Medieval backwards compatibility 
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
eight = 8
sixteenth = 16
thirty_second = 32
sixty_fourth = 64
hundred_twenty_eight = 128


base_values   = [ 0.25, 0.5,  1,   2, 4, 8,  16, 32, 64, 128]
base_triplets = [0.375, 0.75, 1.5, 3, 6, 12, 24, 48, 96, 192]


def add(value1, value2):
	"""Returns the value of the two combined.
{{{
>>> value.add(value.eight, value.quarter)
2.6666666666666665
}}}"""
	return 1 / (1.0 / value1 + 1.0 / value2)

def subtract(value1, value2):
	"""Returns the note value for value1 minus value2. \
There are no exceptions for producing negative values, 
which can be useful for taking differences.
{{{
>>> value.substract(value.quarter, value.eight)
8.0
}}}"""
	return 1 / (1.0 / value1 - 1.0 / value2)

def dots(value, nr = 1):
	"""Returns the dotted note value. A dot adds half the duration of the note. \
A second dot adds half of what was added before, etc. So a dotted eight note has the \
length of three sixteenth notes. An eight note with two dots has the length of five \
thirty second notes.
{{{
>>> value.dot(value.eight)
5.3333333333333333
>>> value.dot(value.eight, 2)
4.5714285714285712
>>> value.dot(4)
2.6666666666666665
}}}"""
	d = 0.0
	while nr >= 0:
		d += 1.0 / (2 ** nr)
		nr -= 1
	return value / d

def triplet(value):
	"""Returns the triplet note value.
{{{
>>> value.triplet(value.eight)
12
>>> value.triplet(4)
6
}}}"""
	return 3 * (value / 2.0)


def determine(value):
	pass
