"""

================================================================================

	mingus - Music theory Python package, progressions module
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

	The progressions module is here to easily indentify and generate
	chords from progressions and vice versa.

================================================================================

"""

import chords
import intervals

jazz = ["ii7", "V7", "I7"]

standard_blues = ["I", "I", "I", "I",\
				  "IV", "IV", "I", "I",\
				  "V7", "V7", "IV", "IV"]

def to_chords(progression, key = 'C'):
	"""Converts a list of chord functions (eg `['I', 'V7']`) to \
a list of chords."""
	return map(lambda x: chords.__dict__[x](key), progression)

def determine(chord, key, shorthand = False):
	"""Determines the harmonic function of chord in key. This function can \
also deal with lists of chords.
{{{
>>> determine(["C", "E", "G"], "C")
['tonic']
>>> determine(["G", "B", "D"], "C")
['dominant']
>>> determine(["G", "B", "D", "F"], "C", True)
['V7']
>>> determine([["C", "E", "G"], ["G", "B", "D"]], "C", True)
[['I'], ['V']]
}}}"""

	result = []
	# Handle lists of chords
	if type(chord[0]) == list:
		for c in chord:
			result.append(determine(c, key, shorthand))
		return result
			

	
	func_dict = {
		"I": "tonic",
		"ii": "supertonic",
		"iii": "mediant",
		"IV": "subdominant",
		"V": "dominant",
		"vi": "submediant",
		"vii" : "subtonic",
	}

	expected_chord = [
		["I", "M", "M7"],
		["ii", "m", "m7"],
		["iii", "m", "m7"],
		["IV", "M", "M7"],
		["V", "M", "7"],
		["vi", "m", "m7"],
		["vii", "dim", "m7b5"],
	]

	type_of_chord = chords.determine(chord, True, False, True)
	for chord in type_of_chord:

		name = chord[0]
		# Get accidentals
		a = 1
		for n in chord[1:]:
			if n == 'b':
				name += 'b'
			elif n == '#':
				name += '#'
			else:
				break
			a += 1
		chord_type = chord[a:]

		# Determine chord function
		interval_type, interval = intervals.determine(key, name).split(" ")
		if interval == "unison":
			func = 'I'
		elif interval == "second":
			func = 'ii'
		elif interval == "third":
			func = 'iii'
		elif interval == "fourth":
			func = 'IV'
		elif interval == 'fifth':
			func = 'V'
		elif interval == 'sixth':
			func = 'vi'
		elif interval == 'seventh':
			func = 'vii'

		# Check whether the chord is altered or not
		for x in expected_chord:
			if x[0] == func:
				# Triads
				if chord_type == x[1]:
					if not shorthand:
						func = func_dict[func]
				# Sevenths
				elif chord_type == x[2]:
					if shorthand:
						func += '7'
					else:
						func = func_dict[func] + ' seventh'
				# Other
				else:
					if shorthand:
						func += chord_type
					else:
						func = func_dict[func] + chords.chord_shorthand_meaning[chord_type]

		# Handle b's and #'s (for instance Dbm in key C is bII)
		if shorthand:
			if interval_type == "minor":
				func = "b" + func
			elif interval_type == "augmented":
				func = "#" + func
			elif interval_type == "diminished":
				func = "bb" + func
		else:
			if interval_type == "minor":
				func = "minor " + func
			elif interval_type == "augmented":
				func = "augmented " + func
			elif interval_type == "diminished":
				func = "diminished " + func

		# Add to results
		result.append(func)

	return result

	

