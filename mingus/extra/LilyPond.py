"""

================================================================================

	mingus - Music theory Python package, LilyPond module
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

	The !LilyPond module provides some methods to help you generate files
	in the !LilyPond format. This allows you to create sheet music from some of the objects in mingus.containers

================================================================================

"""

from mingus.containers.Note import Note
from mingus.containers.mt_exceptions import NoteFormatError, UnexpectedObjectError
import mingus.core.value as value
import os

def from_Note(note, process_octaves = True):
	"""Expects a [refMingusContainersNote Note] object and returns \
the !LilyPond equivalent in a string. If process_octaves is set to False, \
all data regarding octaves will be ignored."""
	# Throw exception
	if not( hasattr(note, "name")):
		return False

	# Lower the case of the name
	result = note.name[0].lower()

	# Convert #'s and b's to 'is' and 'es' suffixes
	for accidental in note.name[1:]:
		if accidental == '#':
			result += 'is'
		elif accidental == 'b':
			result += 'es'

	# Place ' and , for octaves
	if process_octaves:
		oct = note.octave
		if oct >= 4:
			while (oct > 3):
				result += "'"
				oct -= 1
		else:
			while (oct < 4):
				result += ","
				oct += 1
	return result

def from_NoteContainer(nc, duration = None):
	"""Expects a [refMingusContainersNotecontainer NoteContainer] object \
and returns the !LilyPond equivalent in a string. The second argument \
determining the duration of the NoteContainer is optional."""

	# Throw exception
	if not ( hasattr ( nc, "notes" ) ):
		return False

	# Return rests for None or empty lists
	if len(nc.notes) == 0 or len(nc.notes) == 0:
		result = "r"
	# Return a single note if the list contains only 
	# one note
	elif len(nc.notes) == 1:
		result = from_Note(nc.notes[0])

	# Return the notes grouped in '<' and '>'
	else:
		result = "<"
		for notes in nc.notes:
			result += from_Note(notes) + " "
		result = result[:-1] + ">"

	# Add the duration
	if duration != None:
		parsed_value = value.determine(duration)
		result += str(parsed_value[0])
		for i in range(parsed_value[1]):
			result += "."
	return result

def from_Bar(bar, showkey = True, showtime = True):
	"""Expects a [refMingusContainersBar Bar] object and returns the \
!LilyPond equivalent in a string. showkey and showtime can be set to \
determine whether the key and the time should be shown."""
	# Throw exception
	if not ( hasattr ( bar , "bar" ) ):
		return False

	# Process the key
	if showkey:
		key = "\\key %s \\major " %  from_Note(bar.key, False)
		result = key
	else:
		result = ""

	# Handle the NoteContainers
	latest_ratio = (1, 1)
	ratio_has_changed = False
	for bar_entry in bar.bar:
		parsed_value = value.determine(bar_entry[1])
		ratio = parsed_value[2:]
		if ratio == latest_ratio:
			result += from_NoteContainer(bar_entry[2], bar_entry[1]) + " "
		else:
			if ratio_has_changed:
				result += "}"
			result += "\\times %d/%d {" % (ratio[1], ratio[0])
			result += from_NoteContainer(bar_entry[2], bar_entry[1]) + " "
			latest_ratio = ratio
			ratio_has_changed = True
	if ratio_has_changed:
		result += "}"

	# Process the time
	if showtime:
		return "{ \\time %d/%d %s}"\
			% (bar.meter[0], bar.meter[1], result)
	else:
		return "{ %s}" % result
	

def from_Track(track):
	"""Processes a [refMingusContainersTrack Track] object and returns \
the Lilypond equivalent in a string."""
	# Throw exception
	if not ( hasattr ( track, "bars" ) ):
		return False

	lastkey = Note("C")
	lasttime = (4, 4)

	# Handle the Bars:
	result = ""
	for bar in track.bars:
		if lastkey != bar.key:
			showkey = True
		else:
			showkey = False
		if lasttime != bar.meter:
			showtime = True
		else:
			showtime = False

		result += from_Bar(bar, showkey, showtime ) + " "
		lastkey = bar.key
		lasttime = bar.meter
	return "{ %s}" % result


def from_Composition(composition):
	"""Returns the !LilyPond equivalent of a \
[refMingusContainersComposition Composition] in a string"""
	#warning Throw exception
	if not ( hasattr ( composition, "tracks" ) ):
		return False

	result = "\\header { title = \"%s\" composer = \"%s\" opus = \"%s\" } "\
				% (composition.title, composition.author, composition.subtitle)
	for track in composition.tracks:
		result += from_Track(track) + " "

	return result[:-1]

def from_Suite(suite):
	pass


def to_png(ly_string, filename):
	"""Saves a string in LilyPonds format to a PNG. Needs LilyPond in the \
$PATH."""
	return save_string_and_execute_LilyPond(ly_string, filename, "-fpng")

def to_pdf(ly_string, filename):
	"""Saves a string in LilyPonds format to a PDF. Needs LilyPond in the \
$PATH."""
	return save_string_and_execute_LilyPond(ly_string, filename, "-fpdf")

def save_string_and_execute_LilyPond(ly_string, filename, command):
	"""A helper function for to_png and to_pdf. Should not be used directly"""
	ly_string = "\\version \"2.10.33\"\n" + ly_string
	if filename[-4] in [".pdf" or ".png"]:
		filename = filename[:-4]
	try:
		f = open(filename + ".ly", 'w')
		f.write(ly_string)
		f.close()
	except:
		return False
	command = "lilypond " + command + " -o " + filename + " " + filename + ".ly"
	print "Executing: %s" % command
	os.system(command)
	os.remove(filename + ".ly")
	return True

