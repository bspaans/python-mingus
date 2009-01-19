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

numerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII' ]
numeral_intervals = [0, 2, 4, 5, 7, 9, 11]

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
		roman_numeral, acc, suffix = parse_string(chord)

		# There is no roman numeral parsing, just a simple check.
		# Sorry to disappoint.
		#warning Should throw exception
		if roman_numeral not in numerals:
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
	"""Determines the harmonic function of chord in key. This function can also deal with lists of chords. 
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

def parse_string(progression):
	"""Returns a tuple (roman numeral, accidentals, chord suffix). 
{{{
>>> progressions.parse_string("I")
('I', 0, '')
>>> progressions.parse_string("bIM7")
('I', -1, 'M7')
}}}"""
	acc = 0
	roman_numeral = ""
	suffix = ""
	i =0 

	for c in progression:
		if c == '#':
			acc += 1
		elif c == 'b':
			acc -= 1
		elif c.upper() == 'I' or c.upper() == 'V':
			roman_numeral += c.upper()
		else:
			break
		i += 1
	suffix = progression[i:]
	return (roman_numeral, acc, suffix)

def tuple_to_string(prog_tuple):
	"""Creates a string from tuples returned by parse_string"""
	roman, acc, suff = prog_tuple
	if acc > 6:
		acc = 0 - (acc % 6)
	elif acc < -6:
		acc = (acc % 6)
	while acc < 0:
		roman = 'b' + roman
		acc += 1
	while acc > 0:
		roman = '#' + roman
		acc -= 1
	return roman + suff
	

def substitute_harmonic(progression, substitute_index, ignore_suffix = False):
	"""Does simple harmonic substitutions. Returns a \
list of possible substitions for `progression[substitute_index]`. \
If `ignore_suffix` is set to True the suffix of the chord being substituted \
will be ignored. Otherwise only progressions without a suffix, or with suffix '7' \
will be substituted. The following table is used to convert progressions: \
|| I || III ||
|| I || VI ||
|| IV || II ||
|| IV || VI ||
|| V || VII ||"""

	simple_substitutions = [
			("I", "III"),
			("I", "VI"),
			("IV", "II"),
			("IV", "VI"),
			("V", "VII"),
			]
	res = []
	roman, acc, suff = parse_string(progression[substitute_index])
	if suff == '' or suff == '7' or ignore_suffix:
		for subs in simple_substitutions:
			r = subs[1] if roman == subs[0] else None
			if r == None:
				r = subs[0] if roman == subs[1] else None
			if r != None:
				suff = suff if suff == '7' else ''
				res.append(tuple_to_string((r, acc, suff)))
	return res

	
def substitute(progression, substitute_index, depth = 0):
	"""Gives a list of possible substitution for \
`progression[substitute_index]`. If depth > 0 the substitutions \
of each result will be recursively added as well.
{{{
>>> progressions.substitue(["I", "IV", "V", "I"], 0)
["III", "VI", etc.
}}}"""
	res = []

	simple_substitutions = [
			("I", "III"),
			("I", "VI"),
			("IV", "II"),
			("IV", "VI"),
			("V", "VII"),
			("V", "VIIdim7"),
			("V", "IIdim7"),
			("V", "IVdim7"),
			("V", "bVIIdim7"),
			]


	p = progression[substitute_index]
	roman, acc, suff = parse_string(p)
	
	# Do the simple harmonic substitutions
	if suff == '' or suff == '7':
		for subs in simple_substitutions:
			r = None
			if roman == subs[0]:
				r = subs[1]
			elif roman == subs[1]:
				r = subs[0]
			if r != None:
				res.append(tuple_to_string((r, acc, '')))
				# Add seventh or triad depending on r
				if r[-1] != "7":
					res.append(tuple_to_string((r, acc, '7')))
				else:
					res.append(tuple_to_string((r[:-1], acc, '')))


	# Add natural seventh
	if suff == '' or suff == 'M' or suff == 'm':
		res.append(tuple_to_string((roman, acc, suff + '7')))


	# Minor to major substitution
	if suff == 'm' or suff == 'm7':
		n = skip(roman, 2)
		a = interval_diff(roman, n, 4)
		res.append(tuple_to_string((n, a, 'M')))
		res.append(tuple_to_string((n, a, 'M7')))

	# Major to minor substitution
	if suff == 'M' or suff == 'M7':
		n = skip(roman, 6)
		a = interval_diff(roman, n, 9)
		res.append(tuple_to_string((n, a, 'm')))
		res.append(tuple_to_string((n, a, 'm7')))

	
	# Diminished progressions
	if suff == 'dim7' or suff == 'dim':
		
		# Add the corresponding dominant seventh
		res.append(tuple_to_string((skip(roman, 5), acc, 'dom7')))


		# Add chromatic dominant seventh
		n = skip(roman, 1)
		res.append(tuple_to_string((n, acc + interval_diff(roman, n, 1), 'dom7')))

		# Add diminished chord
		last = roman
		for x in range(4):
			next = skip(last, 2)
			acc += interval_diff(last, next, 3)
			res.append(tuple_to_string((next , acc, suff)))
			last = next

	res2 = []
	if depth > 0:
		for x in res:
			new_progr = progression
			new_progr[substitute_index] = x
			res2 += substitute(new_progr, substitute_index, depth - 1)
	return res + res2

def interval_diff(progression1, progression2, interval):
	"""Returns the number of half steps progression2 needs to be \
diminished or augmented until the interval between `progression1` \
and `progression2` is `interval`"""
	i = numeral_intervals[numerals.index(progression1)]
	j = numeral_intervals[numerals.index(progression2)]
	acc = 0
	if j < i:
		j += 12
	while j - i > interval:
		acc -= 1
		j -= 1
	while j - i < interval:
		acc += 1
		j += 1
	return acc
	

def skip(roman_numeral, skip = 1):
	"""Skips places to the next roman numeral. 
{{{
>>> progressions.next("I")
'II'
>>> progressions.next("VII")
'I'
>>> progressions.next("I", 2)
'III'
}}}"""
	i = numerals.index(roman_numeral) + skip
	return numerals[i % 7]

