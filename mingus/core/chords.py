"""
================================================================================

	Music theory Python package, chords module
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

	The chords module is a huge module that builds on the \
	[refMingusCoreIntervals intervals] module. It can be used to generate and \
	recognise a plethora of chords. The following overview groups some of the functions you are most likely to use together.  

	== Generate Diatonic Chords ==
	* Triads
		* triad
		* triads
	* Sevenths
		* seventh
		* sevenths

	== Generate Absolute Chords ==
	* Triads
		* minor_triad
		* major_triad
		* diminished_triad
	* Sixths
		* minor_sixth
		* major_sixth
	* Sevenths
		* minor_seventh
		* major_seventh
		* dominant_seventh
		* minor_major_seventh
		* minor_seventh_flat_five
		* diminished_seventh
	* Ninths
		* minor_ninth
		* major_ninth
		* dominant_ninth
	* Elevenths
		* minor_eleventh
		* eleventh
	* Thirteenths
		* minor_thirteenth
		* major_thirteenth
		* dominant_thirteenth
	* Augmented chords
		* augmented_triad
		* augmented_major_seventh
		* augmented_minor_seventh
	* Suspended chords
		* suspended_second_triad
		* suspended_fourth_triad
		* suspended_seventh
		* suspended_fourth_ninth
		* suspended_ninth
	* Altered chords
		* dominant_flat_ninth
		* dominant_sharp_ninth
		* dominant_flat_five
		* sixth_ninth
		* hendrix_chord

	== Get Chords by Function ==

	* Function
		* tonic and tonic7
		* supertonic and supertonic7
		* mediant and mediant7
		* subdominant and subdominant7
		* dominant and dominant7
		* submediant and submediant7
	* Aliases
		* I, II, III, IV, V, VI
		* ii, iii, vi, vii
		* I7, II7, III7, IV7, V7, VI7
		* ii7, iii7, vi7

	== Useful Functions ==

	* determine - Can recognize all the chords that can be generated with from_shorthand (a lot) and their inversions.
	* from_shorthand - Generates chords from shorthand (eg. 'Cmin7')


================================================================================
"""

import intervals
import notes
import diatonic
from mt_exceptions import NoteFormatError, FormatError



# A cache for composed triads
_triads_cache = {}
# A cache for composed sevenths
_sevenths_cache = {}



# A dictionairy that can be used to present
# lookup chord abbreviations. This dictionairy is also
# used in determine_seventh()
chord_shorthand_meaning = {
		# Triads
		"m" : " minor triad",
		"M" : " major triad",
		"" : " major triad",
		"dim" : " diminished triad",

		# Augmented chords
		"aug" : " augmented triad",
		"+" : " augmented triad",
		"7#5" : " augmented minor seventh",
		"M7+5" : " augmented minor seventh",
		"M7+" : " augmented major seventh",
		"m7+" : " augmented minor seventh",
		"7+" : " augmented major seventh",

		# Suspended chords
		"sus47" :" suspended seventh",
		"sus4" :" suspended fourth triad",
		"sus2" :" suspended second triad",
		"sus" :" suspended fourth triad",
		"11" :" eleventh",
		"sus4b9" :" suspended fourth ninth",
		"susb9" :" suspended fourth ninth",

		# Sevenths
		"m7" :" minor seventh",
		"M7" :" major seventh",
		"dom7" :" dominant seventh",
		"7" :" dominant seventh",
		"m7b5" :" half diminished seventh",
		"dim7" :" diminished seventh",
		"m/M7" :" minor/major seventh",
		"mM7" :" minor/major seventh",
		
		
		# Sixths
		"m6" : " minor sixth",
		"M6" : " major sixth",
		"6" : " major sixth", 
		"6/7" : " dominant sixth",
		"67": " dominant sixth",
		"6/9" :" sixth ninth",
		"69" : " sixth ninth",

		# Ninths
		"9" : " dominant ninth",
		"7b9" : " dominant flat ninth",
		"7#9" :" dominant sharp ninth",
		"M9" :" major ninth",
		"m9" :" minor ninth",

		# Elevenths
		"7#11" :" lydian dominant seventh",
		"m11" :" minor eleventh",

		# Thirteenths
		"M13" :" major thirteenth",
		"m13" :" minor thirteenth",

		"13" :" dominant thirteenth",

		# Altered Chords
		"7b5" :" dominant flat five",
		
		# Special
		"hendrix" :" hendrix chord",
		"7b12" :" hendrix chord",
		"5" :" perfect fifth",
}


#===================================================================
#							Triads
#===================================================================


# diatonic


def triad(note, key):
	"""Returns the triad on note in key as a list.
	Example:
{{{
>>> triad("E", "C") 
["E", "G", "B"]
>>> triad("E", "B")
["E", "G#", "B"]
}}}"""
	return [note, intervals.third(note, key), intervals.fifth(note, key)]





def triads(key):
	"""Returns all the triads in key. Implemented using a cache."""
	
	if _triads_cache.has_key(key):
		return _triads_cache[key]
	res = map(lambda x: triad(x, key), diatonic.get_notes(key))
	_triads_cache[key] = res
	return res




# absolute



def major_triad(note):
	"""Builds a major triad on note.
	Example:
{{{
>>> major_triad("C")
["C", "E", "G"]
}}}"""
	return [note, intervals.major_third(note), intervals.perfect_fifth(note)]




def minor_triad(note):
	"""Builds a minor triad on note.
	Example:
{{{
>>> minor_triad("C")
["C", "Eb", "G"]
}}}"""
	return [note, intervals.minor_third(note), intervals.perfect_fifth(note)]




def diminished_triad(note):
	"""Builds a diminished triad on note.
	Example:
{{{
>>> diminished_triad("C")
["C", "Eb", "Gb"]
}}}"""
	return [note, intervals.minor_third(note), intervals.minor_fifth(note)]




def augmented_triad(note):
	"""Builds an augmented triad on note.
	Example:
{{{
>>> augmented_triad("C")
["C", "E", "G#"]
}}}"""
	return [note, intervals.major_third(note),\
					notes.augment(intervals.major_fifth(note))]




#===================================================================
#	Sevenths
#===================================================================


# diatonic


def seventh(note, key):
	"""Returns the seventh chord on note in key.
	Example:
{{{
>>> seventh("C", "C")
["C", "E", "G", "B"]
}}}"""
	return triad(note, key) + [intervals.seventh(note, key)]



def sevenths(key):
	"""Returns all the sevenths chords in key in a list"""
	if _sevenths_cache.has_key(key):
		return _sevenths_cache[key]
	
	res = map(lambda x: seventh(x, key), diatonic.get_notes(key))
	_sevenths_cache[key] = res
	return res



#absolute
def major_seventh(note):
	"""Builds a major seventh on note.
	Example:
{{{
>>> major_seventh("C") 
["C", "E", "G", "B"]
}}}"""
	return major_triad(note) + [intervals.major_seventh(note)]




def minor_seventh(note):
	"""Builds a minor seventh on note.
	Example:
{{{
>>> minor_seventh("C")
["C", "Eb", "G", "Bb"]
}}}"""
	return minor_triad(note) + [intervals.minor_seventh(note)]




def dominant_seventh(note):
	"""Builds a dominant seventh on note.
	Example:
{{{
>>> dominant_seventh("C")
["C", "E", "G", "Bb"]
}}}"""
	return major_triad(note) + [intervals.minor_seventh(note)]




def half_diminished_seventh(note):
	"""Builds a half diminished seventh (=minor seventh flat five) \
chord on note.
	Example:
{{{
>>> half_diminished_seventh("C")
["C", "Eb", "Gb", "Bb"]
}}}"""
	return diminished_triad(note) + [intervals.minor_seventh(note)]




def minor_seventh_flat_five(note):
	"""See half_diminished_seventh(note) for docs"""
	return half_diminished_seventh(note)




def diminished_seventh(note):
	"""Builds a diminished seventh chord on note.
	Example:
{{{
>>> diminished_seventh("C") 
["C", "Eb", "Gb", "Bbb"]
}}}"""
	return diminished_triad(note) + [notes.diminish(\
					intervals.minor_seventh(note))]

	
	
def minor_major_seventh(note):
	"""Builds a minor major seventh chord on note.
	Example:
{{{
>>> minor_major_seventh("C")
["C", "Eb", "G", "B"]
}}}"""
	return minor_triad(note) + [intervals.major_seventh(note)]




#===================================================================
#	Sixths
#===================================================================


# absolute



def minor_sixth(note):
	"""Builds a minor sixth chord on note.
	Example:
{{{
>>> minor_sixth("C")
['C', 'Eb', 'G', 'A']
}}}"""
	return minor_triad(note) + [intervals.major_sixth(note)]




def major_sixth(note):
	"""Builds a major sixth chord on note.
	Example:
{{{
>>> major_sixth("C")
['C', 'E', 'G', 'A']
}}}"""
	return major_triad(note) + [intervals.major_sixth(note)]




def dominant_sixth(note):
	"""Builds the altered chord 6/7 on note.
	Example:
{{{
>>> dominant_sixth("C")
['C', 'E', 'G', 'A', 'Bb']
}}}"""
	return major_sixth(note) + [intervals.minor_seventh(note)]



def sixth_ninth(note):
	"""Builds the sixth/ninth chord on note.
	Example:
{{{
>>> sixth_ninth('C')
['C', 'E', 'G', 'A', 'D']
}}}"""
	return major_sixth(note) + [intervals.major_second(note)]




#===================================================================
#	Ninths
#===================================================================



# absolute


def minor_ninth(note):
	"""Builds a minor ninth chord on note.
	Example:
{{{
>>> minor_ninth("C")
['C', 'Eb', 'G', 'Bb', 'D']
}}}"""
	return minor_seventh(note) + [intervals.major_second(note)]



def major_ninth(note):
	"""Builds a major ninth chord on note.
	Example:
{{{
>>> major_ninth("C")
['C', 'E', 'G', 'B', 'D']
}}}"""
	return major_seventh(note) + [intervals.major_second(note)]



def dominant_ninth(note):
	"""Builds a dominant ninth chord on note.
	Example:
{{{
>>> dominant_ninth("C")
['C', 'E', 'G', 'Bb', 'D']
}}}"""
	return dominant_seventh(note) + [intervals.major_second(note)]



def dominant_flat_ninth(note):
	"""Builds a dominant flat ninth chord on note.
	Example:
{{{
>>> dominant_ninth("C")
['C', 'E', 'G', 'Bb', 'Db']
}}}"""
	res = dominant_ninth(note)
	res[4] = intervals.minor_second(note)
	return res



def dominant_sharp_ninth(note):
	"""Builds a dominant sharp ninth chord on note.
	Example:
{{{
>>> dominant_ninth("C")
['C', 'E', 'G', 'Bb', 'D#']
}}}"""
	res = dominant_ninth(note)
	res[4] = notes.augment(intervals.major_second(note))
	return res



#===================================================================
#	Elevenths
#===================================================================

# diatonic


# absolute


def eleventh(note):
	"""Builds an eleventh chord on note.
	Example:
{{{
>>> eleventh("C")
['C', 'G', 'Bb', 'F']
}}}"""
	return [note, intervals.perfect_fifth(note), \
		intervals.minor_seventh(note), intervals.perfect_fourth(note)]


def minor_eleventh(note):
	"""Builds a minor eleventh chord on note.
	Example:
{{{
>>> minor_eleventh("C")
['C', 'Eb', 'G', 'Bb', 'F']
}}}"""
	return minor_seventh(note) + [intervals.perfect_fourth(note)]



#===================================================================
#	Thirteenths
#===================================================================

# absolute
def minor_thirteenth(note):
	"""Builds a minor thirteenth chord on note.
	Example:
{{{
>>> minor_thirteenth('C')
['C', 'Eb', 'G', 'Bb', 'D', 'A']
}}}"""
	return minor_ninth(note) + [intervals.major_sixth(note)]



def major_thirteenth(note):
	"""Builds a major thirteenth chord on note.
	Example:
{{{
>>> major_thirteenth('C')
['C', 'E', 'G', 'B', 'D', 'A']
}}}"""
	return major_ninth(note) + [intervals.major_sixth(note)]



def dominant_thirteenth(note):
	"""Builds a dominant thirteenth chord on note.
	Example:
{{{
>>> dominant_thirteenth('C')
['C', 'E', 'G', 'Bb', 'D', 'A']
}}}"""
	return dominant_ninth(note) + [intervals.major_sixth(note)]




#===================================================================
#	Suspended Chords
#===================================================================


# absolute


def suspended_triad(note):
	"""An alias for suspended_fourth_triad"""
	return suspended_fourth_triad(note)



def suspended_second_triad(note):
	"""Builds a suspended second triad on note.
	Example:
{{{
>>> suspended_second_triad("C")
["C", "D", "G"]
}}}"""
	return [note, intervals.major_second(note), intervals.perfect_fifth(note)]



def suspended_fourth_triad(note):
	"""Builds a suspended fourth triad on note.
	Example:
{{{
>>> suspended_fourth_triad("C")
["C", "F", "G"]
}}}"""
	return [note, intervals.perfect_fourth(note), intervals.perfect_fifth(note)]



def suspended_seventh(note):
	"""Builds a suspended (flat) seventh chord on note.
	Example:
{{{
>>> suspended_seventh("C")
["C", "F", "G", "Bb"]

}}}"""
	return suspended_fourth_triad(note) + [intervals.minor_seventh(note)]



def suspended_fourth_ninth(note):
	"""Builds a suspended fourth flat ninth chord on note.
	Example:
{{{
>>> suspended_ninth("C")
['C', 'F', 'G', 'Db']
}}}"""
	return suspended_fourth_triad(note) + [intervals.minor_second(note)]




#===================================================================
#	Augmented Chords
#===================================================================




def augmented_major_seventh(note):
	"""Builds an augmented major seventh chord on note.
	Example:
{{{
>>> augmented_major_seventh("C") 
["C", "E", "G#", "B"]
}}}"""
	return augmented_triad(note) + [intervals.major_seventh(note)]



def augmented_minor_seventh(note):
	"""Builds an augmented minor seventh chord on note.
	Example:
{{{
>>> augmented_minor_seventh("C")
["C", "E", "G#", "Bb"]
}}}"""
	return augmented_triad(note) + [intervals.minor_seventh(note)]




#===================================================================
#	Various
#	Altered and Special chords
#===================================================================


def dominant_flat_five(note):
	"""Builds a dominant flat five chord on note.
	Example:
{{{
>>> dominant_flat_five("C")
['C', 'E', 'Gb', 'Bb']
}}}"""
	res = dominant_seventh(note)
	res[2] = notes.diminish(res[2])
	return res



def lydian_dominant_seventh(note):
	"""Builds the lydian dominant seventh (7#11) on note
	Example:
{{{
>>> lydian_dominant_seventh('C')
['C', 'E', 'G', 'Bb', 'F#']

}}}"""
	return dominant_seventh(note) + [notes.augment(intervals.perfect_fourth(note))]


def hendrix_chord(note):
	"""Builds the famous Hendrix chord (7b12)
	Example:
{{{
>>> hendrix_chord('C')
['C', 'E', 'G', 'Bb', 'Eb']
}}}"""
	return dominant_seventh(note) + [intervals.minor_third(note)]




#===================================================================
#	Chords by harmonic function
#===================================================================



def tonic(key):
	"""Returns the tonic chord in key.
	Example:
{{{
>>> tonic("C") 
["C", "E", "G"]
}}}"""
	return triads(key)[0]



def tonic7(key):
	"""Same as tonic(key), but returns seventh chord instead"""
	return sevenths(key)[0]




def supertonic(key):
	"""Returns the supertonic chord in key.
	Example:
{{{
>>> supertonic("C")
["D", "F", "A"]
}}}"""
	return triads(key)[1]



def supertonic7(key):
	"""Same as supertonic(key), but returns seventh chord"""
	return sevenths(key)[1]



def mediant(key):
	"""Returns the mediant chord in key.
	Example:
{{{
>>> mediant("C") 
["E", "G", "B"]
}}}"""
	return triads(key)[2]




def mediant7(key):
	"""Same as mediant(key), but returns seventh chord"""
	return sevenths(key)[2]



def subdominant(key):
	"""Returns the subdominant chord in key.
	Example:
{{{
>>> subdominant("C") 
["F", "A", "C"]
}}}"""
	return triads(key)[3]




def subdominant7(key):
	"""Same as subdominant(key), but returns seventh chord"""
	return sevenths(key)[3]




def dominant(key):
	"""Returns the dominant chord in key.
	Example:
{{{
>>> dominant("C") 
["G", "B", "D"]
}}}"""
	return triads(key)[4]




def dominant7(key):
	"""Same as dominant(key), but returns seventh chord"""
	return sevenths(key)[4]



def submediant(key):
	"""Returns the submediant chord in key.
	Example:
{{{
>>> submediant("C") 
["A", "C", "E"]
}}}"""
	return triads(key)[5]




def submediant7(key):
	"""Same as submediant(key), but returns seventh chord"""
	return sevenths(key)[5]


def subtonic(key):
	"""Returns the subtonic in key.
	Example:
{{{
>>> subtonic("C")
['B', 'D', 'F']
}}}"""
	return triads(key)[6]

def subtonic7(key):
	"""Same as subtonic(key), but returns seventh chord"""
	return sevenths(key)[6]


#===================================================================
#	 Aliases
#===================================================================


def I(key):
	return tonic(key)

def I7(key):
	return tonic7(key)

def ii(key):
	return supertonic(key)

def II(key):
	return supertonic(key)

def ii7(key):
	return supertonic7(key)

def II7(key):
	return supertonic7(key)

def iii(key):
	return mediant(key)

def III(key):
	return mediant(key)

def iii7(key):
	return mediant7(key)

def III7(key):
	return mediant7(key)

def IV(key):
	return subdominant(key)

def IV7(key):
	return subdominant7(key)

def V(key):
	return dominant(key)

def V7(key):
	return dominant7(key)

def vi(key):
	return submediant(key)

def VI(key):
	return submediant(key)

def vi7(key):
	return submediant7(key)

def VI7(key):
	return submediant7(key)

def vii(key):
	return subtonic(key)

def VII(key):
	return subtonic(key)

def vii7(key):
	return subtonic(key)

def VII7(key):
	return subtonic7(key)


#===================================================================
# 	Inversions
#===================================================================


def invert(chord):
	"""Inverts a given chord one time"""
	return chord[1:] + [chord[0]]

def first_inversion(chord):
	"""The first inversion of a chord"""
	return invert(chord)

def second_inversion(chord):
	"""Returns the second inversion of chord"""
	return invert(invert(chord))

def third_inversion(chord):
	"""Returns the third inversion of chord"""
	return invert(invert(invert(chord)))


#===================================================================
# 	Other
#===================================================================


def from_shorthand(shorthand_string, slash = None):
	"""Takes a chord written in shorthand and returns the notes in the \
chord. The function can recognize triads, sevenths, sixths, ninths, elevenths, \
thirteenths, slashed chords and a number of altered chords. \
The second argument should not be given and is only used for a recursive call \
when a slashed chord or polychord is found. See [http://en.wikibooks.org/wiki/Music_Theory/Complete_List_of_Chord_Patterns Wikibooks] for a nice overview of chord patterns.
	Example:
{{{
>>> from_shorthand("Amin")
["A", "C", "E"]
>>> from_shorthand("Am/M7")
["F", "Ab", "C", "E"]
>>> from_shorthand("A")
["A", "C#", "E"]
>>> from_shorthand("A/G")
["G", "A", "C#", "E"]
>>> from_shorthand("Dm|G")
["G", "B", "D", "F", "A"]

}}}
	Recognised abbreviations: the letters `m` and `M` in the following abbreviations  \
can always be substituted by respectively `min`, `mi` or `-` and `maj` or `ma` (eg. \
`from_shorthand("Amin7") == from_shorthand("Am7")`, etc.).
	* Triads: *'m'*, *'M'* or *''*, *'dim'*. 
	* Sevenths: *'m7'*, *'M7'*, *'7'*, *'m7b5'*, *'dim7'*, *'m/M7'* or *'mM7'*
	* Augmented chords: *'aug'* or *'+'*, *'7#5'* or *'M7+5'*, *'M7+'*, *'m7+'*, *'7+'*
	* Suspended chords: *'sus4'*, *'sus2'*, *'sus47'*, *'sus'*, *'11'*, *'sus4b9'* or *'susb9'*
	* Sixths: *'6'*, *'m6'*, *'M6'*, *'6/7'* or *'67'*, *6/9* or *69*
	* Ninths: *'9'*, *'M9'*, *'m9'*, *'7b9'*, *'7#9'*
	* Elevenths: *'11'*, *'7#11'*, *'m11'*
	* Thirteenths: *'13'*, *'M13'*, *'m13'*
	* Altered chords: *'7b5'*, *'7b9'*, *'7#9'*, *'67'* or *'6/7'*
	* Special: *'5'*, *'NC'*, *'hendrix'*
	"""

	#warning reduce?? 
	if type(shorthand_string) == list:
		res = []
		for x in shorthand_string:
			res.append(from_shorthand(x))
		return res

	if shorthand_string in ["NC", "N.C."]:
		return []

	# Shrink shorthand_string to a format recognised by chord_shorthand
	shorthand_string = shorthand_string.replace('min', 'm')
	shorthand_string = shorthand_string.replace('mi', 'm')
	shorthand_string = shorthand_string.replace('-', 'm')

	shorthand_string = shorthand_string.replace('maj', 'M')
	shorthand_string = shorthand_string.replace('ma', 'M')

	# Get the note name
	if not notes.is_valid_note(shorthand_string[0]):
		raise NoteFormatError, "Unrecognised note '%s' in chord '%s'" % \
				(shorthand_string[0], shorthand_string)

	name = shorthand_string[0]

	# Look for accidentals
	for n in shorthand_string[1:]:
		if n == '#':
			name += n
		elif n == 'b':
			name += n
		else:
			break

	# Look for slashes and polychords '|'
	slash_index = -1
	s = 0
	rest_of_string = shorthand_string[len(name):]
	for n in rest_of_string:
		if n == '/':
			slash_index = s
		elif n == '|':
			# Generate polychord
			return from_shorthand(shorthand_string[:len(name) + s], \
				from_shorthand(shorthand_string[len(name) + s + 1:]))
		s += 1

	# Generate slash chord
	if slash_index != -1 and rest_of_string not in ["m/M7", "6/9", "6/7"]:
		res = shorthand_string[:len(name) + slash_index]
		return from_shorthand(shorthand_string[:len(name) + slash_index], \
				shorthand_string[len(name) + slash_index + 1:])

	shorthand_start = len(name)


	# Return chord
	short_chord = shorthand_string[shorthand_start:]
	if chord_shorthand.has_key(short_chord):
		res = chord_shorthand[short_chord](name)
		if slash != None:

			# Add slashed chords
			if type(slash) == str:
				if notes.is_valid_note(slash):
					res = [slash] + res
				else:
					raise NoteFormatError, \
						"Unrecognised note '%s' in slash chord'%s'" %\
						(slash, slash + shorthand_string)

			# Add polychords
			elif type(slash) == list:
				r = slash
				for n in res:
					if n != r[-1]:
						r.append(n)
				return r 
		return res
		
	else:
                raise FormatError, "Unknown shorthand: %s" % shorthand_string



#===================================================================
#	Chord recognition
#===================================================================

def determine(chord, shorthand = False, no_inversions = False, no_polychords = False):
	"""Names a chord. Can determine almost every chord, from a simple triad to a fourteen note polychord."""
	if chord == []:
		return []
	elif len(chord) == 1:
		return chord
	elif len(chord) == 2:
		return [intervals.determine(chord[0], chord[1])]
	elif len(chord) == 3:
		return determine_triad(chord, shorthand, no_inversions, no_polychords)
	elif len(chord) == 4:
		return determine_seventh(chord, shorthand, no_inversions, no_polychords)
	elif len(chord) == 5:
		return determine_extended_chord5(chord, shorthand, no_inversions, no_polychords)
	elif len(chord) == 6:
		return determine_extended_chord6(chord, shorthand, no_inversions, no_polychords)
	elif len(chord) == 7:
		return determine_extended_chord7(chord, shorthand, no_inversions, no_polychords)
	else:
		return determine_polychords(chord, shorthand)



def determine_triad(triad, shorthand = False, no_inversions = False, placeholder = None):
	"""Names the triad. Returns answers in a list. The third argument should \
not be given. If shorthand is True the answers will be in abbreviated form.

Can determine major, minor, diminished and suspended triads. \
Also knows about invertions.

Examples:
{{{
>>> determine_triad(["A", "C", "E"])
'A minor triad'
>>> determine_triad(["C", "E", "A"]) 
'A minor triad, first inversion'
>>> determine_triad(["A", "C", "E"], True)
'Am'
}}}"""

	if len(triad) != 3:
		#warning: raise exception: not a triad
		return False

	def inversion_exhauster(triad, shorthand, tries, result):
		"""Recursive helper function that runs tries every inversion
		and saves the result."""

		intval1 = intervals.determine(triad[0], triad[1], True)
		intval2 = intervals.determine(triad[0], triad[2], True)

		def add_result(short):
			result.append((short, tries, triad[0]))

		intval = intval1 + intval2
		if intval == "25": add_result("sus2")

		elif intval == "3b7": add_result("dom7") # changed from just '7'
		elif intval == "3b5": add_result("7b5") # why not b5?
		elif intval == "35": add_result("M")
		elif intval == "3#5": add_result("aug")
		elif intval == "36": add_result("M6")
		elif intval == "37": add_result("M7")

		elif intval == "b3b5": add_result("dim")
		elif intval == "b35": add_result("m")
		elif intval == "b36": add_result("m6")
		elif intval == "b3b7": add_result("m7")
		elif intval == "b37": add_result("m/M7")

		elif intval == "45": add_result("sus4")

		elif intval == "5b7": add_result("m7")
		elif intval == "57": add_result("M7")

		if tries != 3 and not no_inversions:
			return inversion_exhauster([triad[-1]] + triad[:-1], shorthand,\
					tries + 1, result)
		else:
			res = []
			for r in result:
				if shorthand:
					res.append(r[2] + r[0])
				else:
					res.append(r[2] + chord_shorthand_meaning[r[0]] + int_desc(r[1]))

			return res

	return inversion_exhauster(triad, shorthand, 1, [])


def determine_seventh(seventh, shorthand = False, no_inversion = False, no_polychords = False):
	"""Determines the type of seventh chord. Returns the results in a \
lists, ordered on inversions. Expects `seventh` to be a \
list of 4 notes. If `shorthand` is set to True, results \
will be returned in chord shorthand ('Cmin7', etc.) - inversions will be \
dropped in that case.
	Example:
{{{
>>> determine_seventh(['C', 'E', 'G', 'B'])
['C major seventh']
}}}"""

	if len(seventh) != 4:
		#warning raise exception: seventh chord is not a seventh chord
		return False

	def inversion_exhauster(seventh, shorthand, tries, result, polychords):
		"""determine sevenths recursive functions"""

		# Check whether the first three notes of seventh 
		# are part of some triad.
		triads = determine_triad(seventh[:3], True, True)
			
		# Get the interval between the first and last note
		intval3 = intervals.determine(seventh[0], seventh[3])

		def add_result(short, poly = False):
			"""helper function"""
			result.append((short, tries, seventh[0], poly))

		# Recognizing polychords
		if tries == 1 and not no_polychords:
			polychords = polychords +  determine_polychords(seventh, shorthand)

		# Recognizing sevenths
		for triad in triads:
			# Basic triads
			triad = triad[len(seventh[0]):]
			if triad == "m":
				if intval3 == "minor seventh":
					add_result("m7")
				elif intval3 == "major seventh":
					add_result("m/M7")
				elif intval3 == "major sixth":
					add_result("m6")
			elif triad == "M":
				if intval3 == "major seventh":
					add_result("M7")
				elif intval3 == "minor seventh":
					add_result("7")
				elif intval3 == "major sixth":
					add_result("M6")
			elif triad == "dim":
				if intval3 == "minor seventh":
					add_result("m7b5")
				elif intval3 == "diminished seventh":
					add_result("dim7")
			elif triad == "aug":
				if intval3 == "minor seventh":
					add_result("m7+")
				if intval3 == "major seventh":
					add_result("M7+")
			elif triad == "sus4":
				if intval3 == "minor seventh":
					add_result("sus47")
				elif intval3 == "minor second":
					add_result("sus4b9")
			# Other
			elif triad == 'm7':
				if intval3 == 'perfect fourth':
					add_result("11")
			elif triad == '7b5':
				if intval3 == 'minor seventh':
					add_result("7b5")
	


		# Loop until we have exhausted all the inversions
		if tries != 4 and not no_inversion:
			return inversion_exhauster([seventh[-1]] + seventh[:-1], \
							shorthand, tries + 1, result, polychords)
		else:
			# Return results
			res = []
			# Reset seventh
			seventh = [seventh[3]] + seventh[0:3]
			for x in result:
				if shorthand:
					res.append(x[2] + x[0])
				else:
					res.append(x[2] + chord_shorthand_meaning[x[0]] + int_desc(x[1]))
			return res + polychords
	return inversion_exhauster(seventh, shorthand, 1, [], [])


def determine_extended_chord5(chord, shorthand = False, no_inversions = False, no_polychords = False):
	"""Determines the names of an extended chord"""
	if len(chord) != 5:
		#warning raise exeption: not an extended chord
		return False

	def inversion_exhauster(chord, shorthand, tries, result, polychords):
		"""Recursive helper function"""

		def add_result(short):
			result.append((short, tries, chord[0]))

		triads = determine_triad(chord[:3], True, True)
		sevenths = determine_seventh(chord[:4], True, True, True)

		# Determine polychords
		if tries == 1 and not no_polychords:
			polychords += determine_polychords(chord, shorthand)


		# Determine 'normal' chords
		intval4 = intervals.determine(chord[0], chord[4])
		for seventh in sevenths:
			seventh = seventh[len(chord[0]):]
			if seventh == "M7":
				if intval4 == 'major second':
					add_result("M9")
			elif seventh == "m7":
				if intval4 == 'major second':
					add_result("m9")
				elif intval4 == 'perfect fourth':
					add_result("m11")
			elif seventh == "7":
				if intval4 == 'major second':
					add_result("9")
				elif intval4 == 'minor second':
					add_result("7b9")
				elif intval4 == 'augmented second':
					add_result("7#9")
				elif intval4 == 'minor third':
					add_result("7b12")
				elif intval4 == 'augmented fourth':
					add_result("7#11")
				elif intval4 == 'major sixth':
					add_result("13")
			elif seventh == "M6":
				if intval4 == "major second":
					add_result("6/9")
				elif intval4 == "minor seventh":
					add_result("6/7")

		if tries != 5 and not no_inversions:
			return inversion_exhauster([chord[-1]] + chord[:-1], \
						shorthand, tries + 1, result, polychords)
		else:
			res = []
			for r in result:
				if shorthand:
					res.append(r[2] + r[0])
				else:
					res.append(r[2] + chord_shorthand_meaning[r[0]] + int_desc(r[1]))
			return res + polychords

	return inversion_exhauster(chord, shorthand, 1, [], [])



def determine_extended_chord6(chord, shorthand = False, no_inversions = False, no_polychords = False):
	"""Determines the names of an 6 note chord"""
	if len(chord) != 6:
		#warning raise exeption: not an extended chord
		return False

	def inversion_exhauster(chord, shorthand, tries, result, polychords):
		"""Recursive helper function"""

		# Determine polychords
		if tries == 1 and not no_polychords:
			polychords += determine_polychords(chord, shorthand)

		def add_result(short):
			result.append((short, tries, chord[0]))

		ch = determine_extended_chord5(chord[:5], True, True, True)
		intval5 = intervals.determine(chord[0], chord[5])

		for c in ch:
			c = c[len(chord[0]):]
			if c == '9':
				if intval5 == 'perfect fourth':
					add_result('11')
				elif intval5 == 'augmented fourth':
					add_result('7#11')
				elif intval5 == 'major sixth':
					add_result('13')
			elif c == 'm9':
				if intval5 == 'perfect fourth':
					add_result('m11')
				elif intval5 == 'major sixth':
					add_result('m13')
			elif c == 'M9':
				if intval5 == 'perfect fourth':
					add_result('M11')
				elif intval5 == 'major sixth':
					add_result('M13')

		if tries != 6 and not no_inversions:
			return inversion_exhauster([chord[-1]] + chord[:-1], \
						shorthand, tries + 1, result, polychords)
		else:
			res = []
			for r in result:
				if shorthand:
					res.append(r[2] + r[0])
				else:
					res.append(r[2] + chord_shorthand_meaning[r[0]] + int_desc(r[1]))
			return res + polychords

	return inversion_exhauster(chord, shorthand, 1, [], [])




def determine_extended_chord7(chord, shorthand = False, no_inversions = False, no_polychords = False):
	"""Determines the names of an 7 note chord"""
	if len(chord) != 7:
		#warning raise exeption: not an extended chord
		return False

	def inversion_exhauster(chord, shorthand, tries, result, polychords):
		"""Recursive helper function"""

		# Determine polychords
		if tries == 1 and not no_polychords:
			polychords += determine_polychords(chord, shorthand)

		def add_result(short):
			result.append((short, tries, chord[0]))

		ch = determine_extended_chord6(chord[:6], True, True, True)
		intval6 = intervals.determine(chord[0], chord[6])

		for c in ch:
			c = c[len(chord[0]):]
			if c == '11':
				if intval6 == 'major sixth':
					add_result('13')
			elif c == 'm11':
				if intval6 == 'major sixth':
					add_result('m13')
			elif c == 'M11':
				if intval6 == 'major sixth':
					add_result('M13')
				

		if tries != 6:
			return inversion_exhauster([chord[-1]] + chord[:-1], \
						shorthand, tries + 1, result, polychords)
		else:
			res = []
			for r in result:
				if shorthand:
					res.append(r[2] + r[0])
				else:
					res.append(r[2] + chord_shorthand_meaning[r[0]] + int_desc(r[1]))
			return res + polychords

	return inversion_exhauster(chord, shorthand, 1, [], [])




def int_desc(tries):
	"""Helper function that returns the inversion of the triad in a string"""
	if tries == 1:
		return ""
	elif tries == 2:
		return ", first inversion"
	elif tries == 3:
		return ", second inversion"
	elif tries == 4:
		return ", third inversion"


def determine_polychords(chord, shorthand = False):
	"""Determines the polychords in chord. Can handle anything from polychords based on two triads to 6 note extended chords."""
	polychords = []

	function_list = [ 
			determine_triad, determine_seventh, 
			determine_extended_chord5, determine_extended_chord6,
			determine_extended_chord7
			]

	# Range tracking. 
	if len(chord) <= 3:
		return []
	elif len(chord) > 14:
		return []
	elif len(chord) - 3 <= 5:
		function_nr = range(0, len(chord) - 3)
	else:
		function_nr = range(0, 5)

	for f in function_nr:
		for f2 in function_nr:
			# The clever part:
			# Try the function_list[f] on the len(chord) - (3 + f)
			# last notes of the chord. Then try the function_list[f2]
			# on the f2 + 3 first notes of the chord. Thus, trying
			# all possible combinations.
			for chord1 in function_list[f](chord[len(chord) -\
				(3 + f):], True, True, True):
					for chord2 in function_list[f2](chord[:f2+3], \
						True, True, True):
						polychords.append("%s|%s" % (chord1, chord2))

	if shorthand:
		for p in polychords:
			p = p + " polychord"

	return polychords
	
# A dictionairy that can be used to present
# chord abbreviations. This dictionairy is also
# used in from_shorthand()
chord_shorthand = {
		# Triads
		"m" : minor_triad,
		"M" : major_triad, 
		"" : major_triad,
		"dim" : diminished_triad,

		# Augmented chords
		"aug" : augmented_triad,
		"+" : augmented_triad,
		"7#5" : augmented_minor_seventh,
		"M7+5" : augmented_minor_seventh,
		"M7+" : augmented_major_seventh,
		"m7+" : augmented_minor_seventh,
		"7+" : augmented_major_seventh,

		# Suspended chords
		"sus47" : suspended_seventh,
		"sus4" : suspended_fourth_triad,
		"sus2" : suspended_second_triad,
		"sus" : suspended_triad,
		"11" : eleventh,
		"sus4b9" : suspended_fourth_ninth,
		"susb9" : suspended_fourth_ninth,

		# Sevenths
		"m7" : minor_seventh,
		"M7" : major_seventh,
		"7" : dominant_seventh,
		"dom7" : dominant_seventh,
		"m7b5" : minor_seventh_flat_five,
		"dim7" : diminished_seventh,
		"m/M7" : minor_major_seventh,
		"mM7" : minor_major_seventh,
		
		
		# Sixths
		"m6" : minor_sixth,
		"M6" : major_sixth,
		"6" : major_sixth, 
		"6/7" : dominant_sixth,
		"67": dominant_sixth,
		"6/9" : sixth_ninth,
		"69" : sixth_ninth,

		# Ninths
		"9" : dominant_ninth,
		"7b9" : dominant_flat_ninth,
		"7#9" : dominant_sharp_ninth,
		"M9" : major_ninth,
		"m9" : minor_ninth,

		# Elevenths
		"7#11" : lydian_dominant_seventh,
		"m11" : minor_eleventh,

		# Thirteenths
		"M13" : major_thirteenth,
		"m13" : minor_thirteenth,

		"13" : dominant_thirteenth,

		# Altered Chords
		"7b5" : dominant_flat_five,
		
		# Special
		"hendrix" : hendrix_chord,
		"7b12" : hendrix_chord,
		"5" : (lambda x: [x, intervals.perfect_fifth(x)])
}


