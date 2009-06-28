"""
================================================================================

	mingus - Music theory Python package, Note class.
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

"""

from mingus.core import notes, intervals
from mt_exceptions import NoteFormatError
from math import log



class Note:
	"""In the mingus.core module, notes are generally represented by \
strings. Most of the times, this is not enough. We want to set \
the octave and maybe the amplitude, vibrato or other dynamics. \
Then we want to store the notes in bars, the bars in tracks, \
the tracks in compositions, etc.\n\nWe could do this with a \
number of lists, but ultimately it is a lot easier to use objects. \
The Note class provides an easy way to deal with notes in an object \
oriented matter.\n\nYou can use the class \
[refMingusContainersNotecontainer NoteContainer] \
to group Notes together in intervals and chords."""

	name = 'C'
	octave = 4
	dynamics = {}

	def __init__(self, name = 'C', octave = 4, dynamics = {}):
                if type(name) == str:
        		self.set_note(name, octave, dynamics)

                # Hardcopy Note object
                elif hasattr(name, "name"):
                        self.set_note(name.name, name.octave, name.dynamics)
                        if hasattr(name, "channel"):
                                self.channel = name.channel
                        if hasattr(name, "velocity"):
                                self.velocity = name.velocity


                # Convert from integer
                elif type(name) == int:
                        self.from_int(int)

                else:
                        raise NoteFormatError, "Don't know what to do with name object: '%s'" % name

	def set_note(self, name = 'C', octave = 4, dynamics = {}):
		"""Sets the note to `name` in `octave` with `dynamics` if \
the name of the note is valid. Returns the objects if it \
succeeded, raises an NoteFormatError otherwise."""
		dash_index = name.split('-')
		if len(dash_index) == 1:
			if notes.is_valid_note(name):
				self.name = name
				self.octave = octave
				self.dynamics = dynamics
				return self
			else:
				raise NoteFormatError,\
					"The string '%s' is not a valid representation"\
					"of a note in mingus" % name
		elif len(dash_index) == 2:
			if notes.is_valid_note(dash_index[0]):
				self.name = dash_index[0]
				self.octave = int(dash_index[1])
				self.dynamics = dynamics
				return True
			else:
				raise NoteFormatError,\
					"The string '%s' is not a valid representation"\
					"of a note in mingus" % name
		return False

	def empty(self):
		"""Removes the data in the instance."""
		self.name = ''
		octave = 0
		dynamics = {}

	def augment(self):
		"""Calls notes.augment with this note as argument"""
		self.name = notes.augment(self.name)
	
	def diminish(self):
		"""Calls notes.diminish with this note as argument"""
		self.name = notes.diminish(self.name)

	def change_octave(self, diff):
		"""Changes the octave of the note to the current `octave` + `diff`"""
		self.octave += diff
		if self.octave < 0:
			self.octave = 0

	def octave_up(self):
		"""Increments the current octave with 1"""
		self.change_octave(1)

	def octave_down(self):
		"""Decrements the current octave with 1"""
		self.change_octave(-1)

	def to_minor(self):
		"""Calls notes.to_minor with this note as argument. \
Doesn't change the octave."""
		self.name = notes.to_minor(self.name)

	def to_major(self):
		"""Calls notes.to_major with this note name as argument. \
Doesn't change the octave."""
		self.name = notes.to_major(self.name)

	def remove_redundant_accidentals(self):
		"""Calls notes.remove_redundant_accidentals on this note's name."""
		self.name = notes.remove_redundant_accidentals(self.name)

	def transpose(self, interval, up = True):
		"""Transposes the note up or down the interval. 
{{{
>>> a = Note("A")
>>> a.transpose("3")
>>> a
'C#-5'
>>> a.transpose("3", False)
>>> a
'A-4'
}}}"""
		old, o_octave = self.name, self.octave
		self.name = intervals.from_shorthand(self.name, interval, up)
		if up:
			if self < Note(old, o_octave):
				self.octave += 1
		else:
			if self > Note(old, o_octave):
				self.octave -= 1


	def from_int(self, integer):
		"""Sets the Note corresponding to the integer. 0 is a C on octave 0, \
12 is a C on octave 1, etc. 
{{{
>>> c = Note()
>>> c.from_int(12)
>>> c
'C-1'
}}}"""
		self.name = notes.int_to_note(integer % 12)
		self.octave = integer / 12
		return self

        def measure(self, other):
                """Returns the number of semitones between this Note and the other.
{{{
>>> Note("C").measure(Note("D"))
2
>>> Note("D").measure(Note("C"))
-2
}}}"""
                return int(other) - int(self)

	def to_hertz(self, standard_pitch = 440):
		"""Returns the Note in Hz. The `standard_pitch` argument can be used \
to set the pitch of A-4, from which the rest is calculated."""

		# int(Note("A")) == 57
		diff = self.__int__() - 57
		return 2 ** (diff / 12.0) * 440

	def from_hertz(self, hertz, standard_pitch = 440):
		"""Sets the Note name and pitch, calculated from the `hertz` value. \
The `standard_pitch` argument can be used to set the pitch of A-4, from \
which the rest is calculated."""

		value = log(float(hertz) / standard_pitch, 2) * 12 + notes.note_to_int("A")
		self.name = notes.int_to_note(int(value) % 12)
		self.octave = int(value / 12) + 4

	def __int__(self):
		"""Returns the current octave multiplied by twelve and adds \
notes.note_to_int to it. This means a C-0 returns 0, C-1 \
returns 12, etc. This method allows you to use int() on Notes."""
		res = self.octave * 12 + notes.note_to_int(self.name[0])
		for n in self.name[1:]:
			if n == '#':
				res += 1
			elif n== 'b':
				res -= 1
		return res
			

	def __cmp__(self, other):
		"""This method allows you to use the comparing operators \
on Notes (>, <, ==, !=, >= and <=). So we can sort() Intervals, etc.
{{{
>>> Note("C", 4) < Note("B", 4) 
True
>>> Note("C", 4) > Note("B", 4)
False
}}}"""
		if other == None:
			return 1
		s = int(self)
		o = int(other)

		if s < o:
			return -1
		elif s > o:
			return 1
		else:
			return 0

	def __repr__(self):
		"""A helpful representation for printing Note classes"""
		return "'%s-%d'" %  (self.name, self.octave)


	
