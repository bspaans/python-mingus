"""

================================================================================

	Music theory Python package, diatonic module.
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

	The diatonic module provides a simple interface for dealing with diatonic
	keys. The function get_notes(key) for instance returns the notes in a 
	given key; even for extremely exotic notations ("C#####" or "Gbbbb").

================================================================================

"""

from mt_exceptions import NoteFormatError, KeyError, RangeError
import notes

basic_keys = ["Gb", "Db", "Ab", "Eb", "Bb",\
			  "F", "C", "G", "D", "A", "E", "B",\
			  "F#", "C#", "G#", "D#", "A#"]


_key_cache = {}

def get_notes(key):
	"""Returns an ordered list of the notes in this key. \
For example: if the key is set to 'F', this function will return \
`['F', 'G', 'A', 'Bb', 'C', 'D', 'E']`. \
Exotic or ridiculous keys like 'C####' or even 'Gbb##bb#b##' will work; \
Note however that the latter example will also get cleaned up to 'G'. \
This function will raise an !NoteFormatError if the key isn't recognised"""

	#check cache
	global key_dict
	if _key_cache.has_key(key):
		return _key_cache[key]

	if not (notes.is_valid_note(key)):
		raise NoteFormatError, "Unrecognised format for key '%s'" % key

	fifth_index = notes.fifths.index(key[0])

	result = []

	# fifth_index = 0 is a special case. It's the key of F and needs 
	# Bb instead of B included in the result.
	if fifth_index != 0:
		result.append(notes.fifths[(fifth_index - 1) % 7] + key[1:])
		for x in notes.fifths[fifth_index:]:
			result.append(x  + key[1:])
		for x in notes.fifths[:(fifth_index - 1)]:
			result.append(x + key[1:] + "#")
	else:
		for x in notes.fifths[0:6]:
			result.append(x + key[1:])
		result.append("Bb" + key[1:])

	result.sort()

	# Remove redundant #'s and b's from the result
	result = map(notes.remove_redundant_accidentals, result)
	tonic = result.index(notes.remove_redundant_accidentals(key))

	result = result[tonic:] + result[:tonic]

	#Save result to cache
	_key_cache[key] = result
	return result


def int_to_note(note_int, key):
	"""A better implementation of int_to_note found in the \
[refMingusCoreNotes notes] module. This version bears the key in mind \
and thus creates theoretically correct notes. Will throw a \
!RangeError if `note_int` is not in range(0,12)"""

	if note_int not in range(0,12):
		raise RangeError, "Integer not in range 0-11."

	intervals = [0, 2, 4, 5, 7, 9, 11]

	current = notes.note_to_int(key)
	known_intervals = map(lambda x: (x + current) % 12, intervals)

	known_notes = get_notes(key)
	if note_int in known_intervals:
		return known_notes[known_intervals.index(note_int)]	
	else:
		if note_int - 1 in known_intervals:
			return notes.remove_redundant_accidentals(\
                                  known_notes[known_intervals.index(note_int - 1)] + "#")
		elif note_int + 1 in known_intervals:
			return notes.remove_redundant_accidentals(\
                                  known_notes[known_intervals.index(note_int + 1)] + "b")

def interval(key, start_note, interval):
	"""Returns the note found at the interval starting from start_note \
in the given key. For example interval('C', 'D', 1) will return 'E'. \
Will raise a !KeyError if the start_note is not a valid note."""
	
	if not notes.is_valid_note(start_note):
		raise KeyError,"The start note '%s' is not a valid note" % start_note

	notes_in_key = get_notes(key)

	for n in notes_in_key:
		if n[0] == start_note[0]:
			index = notes_in_key.index(n)
	return notes_in_key[(index + interval) % 7]
