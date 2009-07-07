"""
================================================================================

	mingus - Music theory Python package, notes module.
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

	This module is the foundation of the music theory package.
	It handles conversions from integers to notes and vice versa and thus
	enables simple calculations. You should note however, that the 
	int_to_note conversion can't be correctly done without knowing
	exactly what key we are in and what augmentations are being used.
	The same function in other modules ([refMingusCoreDiatonic diatonics]
	and [refMingusContainersNote container.Note]) will
	do a better _theoretical_ job at int_to_note, but this one is 
	still usable for simple representations and trackers, etc. where
	keys don't really matter.

================================================================================

"""

from mt_exceptions import NoteFormatError, RangeError
import intervals


# _note_dict is a mapping of the C scale to half notes. It is used to calculate 
# for instance C# (add 1 to 0), Fb (substract 1 from 5), etc. in note_to_int
# and it is also used in is_valid_note to check formatting validity.
_note_dict = { 'C' : 0, 
			  'D' : 2,
			  'E' : 4,
			  'F' : 5, 
			  'G' : 7,
			  'A' : 9,
			  'B' : 11 
			  }

fifths = ['F', 'C', 'G', 'D', 'A', 'E', 'B']


def int_to_note(note_int):
	"""Converts integers in the range of 0-11 to notes in the \
form of C or C# (no Cb). You can use int_to_note in diatonic_key to \
do theoretically correct conversions that bear the key in mind. \
Throws a !RangeError exception if the note_int is not in range(0,12)."""

	if note_int not in range(0,12):
		raise RangeError, "int out of bounds (0-11): %d " % note_int
	
	n = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
	return n[note_int]


def is_enharmonic(note1, note2):
	"""Test whether note1 and note2 are enharmonic, ie. they sound the same"""
	return note_to_int(note1) == note_to_int(note2)


def is_valid_note(note):
	"""Returns true if note is in a recognised format. False if not"""
	if not(_note_dict.has_key(note[0])):
		return False
	for post in note[1:]:
		if post != 'b' and post != '#':
			return False
	return True



def note_to_int(note):
	"""Converts notes in the form of C, C#, Cb, C##, etc. to \
an integer in the range of 0-11. Throws an !NoteFormatError \
exception if the note format is not recognised."""

	if is_valid_note(note):
		val = _note_dict[note[0]]
	else:
		raise NoteFormatError, "Unknown note format '%s'" % note

	# Check for '#' and 'b' postfixes
	for post in note[1:]:
		if post == 'b':
			val -= 1
		elif post == '#':
			val += 1
	return val % 12


def remove_redundant_accidentals(note):
	"""Removes redundant #'s and b's from the given note. \
For example: C##b becomes C#, Eb##b becomes E, etc."""
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
	"""Augments a given note. 
	Examples:
{{{
>>> augment("C")
'C#'
>>> augment("Cb") 
'C'
}}}"""
	if note[-1] != 'b':
		return note + '#'
	else:
		return note[:-1]

def diminish(note):
	"""Diminishes a given note.
	Examples: 
{{{
>>> diminish("C") 
'Cb'
>>> diminish("C#") 
'C'
}}}"""
	if note[-1] != '#':
		return note + 'b'
	else:
		return note[:-1]

def to_major(note):
	"""Returns the major of `note`.
	Example:
{{{
>>> to_major("A") 
'C'
}}}"""
	return intervals.minor_third(note)

def to_minor(note):
	"""Returns the minor of note.
	Example:
{{{
>>> to_minor("C")
'A'
}}}"""
	return intervals.major_sixth(note)
