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

	In music and music theory you often deal with sequences 
	of chords. These chord sequences are called progressions and are
	often written down using roman numerals. In this system the 'I' 
	refers to the first natural triad in a key, the II to the second,
	etc. We can add prefixes and suffixes to denote more complex 
	progressions, like: #V7, bIIdim7, etc.

	This module provides methods which can convert progressions 
	to chords and vice versa.

================================================================================

"""

import notes
import chords
import intervals


def to_chords(progression, key = 'C'):
	"""Converts a list of chord functions (eg `['I', 'V7']`) or \
a string (eg. 'I7') to a list of chords. \
Any number of accidentals can be used as prefix to augment or diminish; \
for example: bIV or #I. All the chord abbreviations in the chord module \
can be used as suffixes; for example: Im7, IVdim7, etc. \
You can combine prefixes and suffixes to manage complex progressions: \
#vii7, #iidim7, iii7, etc. \
Using 7 as suffix is ambiguous, since it is classicly used to denote \
the seventh chord when talking about progressions instead of _just_ the \
dominanth seventh chord. We have taken the classic route; I7 \
will get you a major seventh chord. If you specifically want a dominanth \
seventh, use Idom7."""

	if type(progression) == str:
		progression = [progression]

	result = []
	for chord in progression:
		
		# strip preceding accidentals from the string
		acc = 0
		roman_numeral = ""
		suffix = ""
		i =0 

		for c in chord:
			if c == '#':
				acc += 1
			elif c == 'b':
				acc -= 1
			elif c.upper() == 'I' or c.upper() == 'V':
				roman_numeral += c.upper()
			else:
				break
			i += 1
		suffix = chord[i:]

		# There is no roman numeral parsing, just a simple check.
		# Sorry to disappoint.
		#warning Should throw exception
		if roman_numeral not in ['I', 'II', 'III', 'IV',\
					'V', 'VI', 'VII']:
			return []

		# These suffixes don't need any post processing
		if suffix == '7' or suffix == '':
			roman_numeral += suffix

			# ahh Python. Everything is a dict.
			r = chords.__dict__[roman_numeral](key)
		else:
			r = chords.__dict__[roman_numeral](key)
			r = chords.chord_shorthand[suffix](r[0])


		# Let the accidentals do their work
		while acc < 0:
			r = map(notes.diminish, r)
			acc += 1
		while acc > 0:
			r = map(notes.augment, r)
			acc -= 1

		result.append(r)
	return result
	


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

	

