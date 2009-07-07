"""

================================================================================

	mingus - Music theory Python package, Bar class
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

"""

from mingus.core import meter as _meter
from mingus.core import scales, progressions
from NoteContainer import NoteContainer
from Note import Note
from mt_exceptions import MeterFormatError

class Bar:
	"""A Bar is basically a container for \
[refMingusContainersNotecontainer NoteContainers] (a \
!NoteContainerContainer if you will, but you shouldn't). Bars can be \
stored together with [refMingusContainersInstrument Instruments] in \
[refMingusContainersTrack Tracks]."""

	key = 'C'
	meter = (4, 4)
	current_beat = 0.0
	length = 0.0
	bar = []

	def __init__(self, key = 'C', meter=(4,4)):

		#warning should check types
		if type(key) == str:
			key = Note(key)
		self.key = key
		self.set_meter(meter)	
		self.empty()

	def empty(self):
		"""Empties the Bar, removes all the \
[refMingusContainersNotecontainer NoteContainers]"""
		self.bar = []
		self.current_beat = 0.0
		return self.bar

	def set_meter(self, meter):
		"""Meters in mingus are represented by a single tuple. \
This function will set the meter of this bar. If the format \
of the meter is not recognised, a !MeterFormatError will \
be raised."""
		#warning should raise exception
		if _meter.valid_beat_duration(meter[1]):
			self.meter = (meter[0], meter[1])
			self.length = meter[0] * (1.0 / meter[1])
		elif meter == (0, 0):
			self.meter = (0, 0)
			self.length = 0.0
		else:
			raise MeterFormatError, "The meter argument '%s' is not an understood representation of a meter. Expecting a tuple." % meter


	def place_notes(self, notes, duration):
		"""Places the notes on the `current_beat`. Notes can be strings, \
[refMingusContainersNote Notes], list of strings, list of \
[refMingusContainersNote Notes] or a [refMingusContainersNotecontainer \
NoteContainer]. Raises a !MeterFormatError if the duration is not \
valid. Returns True if succesful, False otherwise (ie. the Bar \
hasn't got enough room for a note of that duration.)"""

		# note should be able to be one of strings, lists, 
		# Notes or NoteContainers
		if hasattr(notes, "notes"):
			pass
		elif hasattr(notes, "name"):
			notes = NoteContainer(notes)
		elif type(notes) == str:
			notes = NoteContainer(notes)
		elif type(notes) == list:
			notes = NoteContainer(notes)

		if self.current_beat + 1.0 / duration <= self.length or self.length == 0.0:
			self.bar.append([self.current_beat, duration, notes])
			self.current_beat += 1.0 / duration
			return True
		else:
			return False

	def place_notes_at(self, notes, at):
		"""Places notes at the index `at`"""
		for x in self.bar:
			if x[0] == at:
				x[0][2] += notes

	def place_rest(self, duration):
		"""Places a rest of `duration` on the `current_beat`. The same as \
`place_notes(None, duration)`"""
		return self.place_notes(None, duration)
	
	def remove_last_entry(self):
		"""Removes the last [refMingusContainersNotecontainer NoteContainer] \
in the Bar"""
		self.current_beat -= 1.0 / self.bar[-1][1]
		self.bar = self.bar[:-1]
		return self.current_beat

	def is_full(self):
		"""Returns False if there is room in this Bar for another \
[refMingusContainersNotecontainer NoteContainer], True otherwise."""
		if self.length == 0.0:
			return False
	
		if len(self.bar) == 0:
			return False
		if self.current_beat >= self.length - 0.001:
			return True

		return False

	def change_note_duration(self, at, to):
		"""Changes the note duration at index `at` to duration `to`"""
		if valid_beat_duration(to):
			diff = 0
			for x in self.bar:
				if diff != 0:
					x[0][0] -= diff
				if x[0] == at:
					cur = x[0][1]
					x[0][1] = to
					diff = 1/cur - 1/to

	def get_range(self):
		"""Returns the highest and the lowest note in a tuple"""
		min, max = (100000, -1)
		for cont in self.bar:
			for note in cont[2]:
				if int(note) < int(min):
					min = note
				elif int(note) > int(max):
					max = note
		return (min, max)

        def space_left(self):
                """Returns the space left on the Bar."""
                return self.length  - self.current_beat

        def value_left(self):
                """Returns the value left on the Bar."""
                return 1.0 / self.space_left()

	def augment(self):
		"""Calls augment on the NoteContainers in Bar."""
		for cont in self.bar:
			cont[2].augment()

	def diminish(self):
		"""Calls diminish on the NoteContainers in Bar."""
		for cont in self.bar:
			cont[2].diminish()

	def to_minor(self):
		"""Calls to_minor on the NoteContainers in Bar."""
		for cont in self.bar:
			cont[2].to_minor()

	def to_major(self):
		"""Calls to_major on the NoteContainers in Bar."""
	 	for cont in self.bar:
			cont[2].to_major()

	def transpose(self, interval, up = True):
		"""Transposes the notes in the bar up or down the interval. Calls transpose() on all [refMingusContainersNotecontainer NoteContainers] in the bar."""
		for cont in self.bar:
			cont[2].transpose(interval, up)

	def determine_chords(self, shorthand = False):
		"""Returns a list of lists [place_in_beat, possible_chords]."""

		chords = []
		for x in self.bar:
			chords.append([x[0], x[2].determine(shorthand)])
		return chords

	def determine_progression(self, shorthand = False):
		"""Returns a list of lists [place_in_beat, possible_progressions]."""
		res = []
		for x in self.bar:
			res.append([x[0], progressions.determine(x[2].get_note_names(), self.key.name, shorthand)])
		return res

			

	def get_note_names(self):
		"""Returns a list of unique note names in the Bar."""
		res = []
		for cont in self.bar:
			for x in cont[2].get_note_names():
				if x not in res:
					res.append(x)
		return res

	def __add__(self, note_container):
		"""Enables the '+' operator on Bars"""
		if self.meter[1] != 0:
			return self.place_notes(note_container, self.meter[1])
		else:
			return self.place_notes(note_container, 4)

	def __getitem__(self, index):
		"""Allows you to use `Bar[]` notation on Bars to get the \
item at the index."""
		return self.bar[index]

	def __setitem__(self, index, value):
		"""Allows you to use [] = notation on Bars. The value \
should be a [refMingusContainersNotecontainer NoteContainer], \
or a string/list/[refMingusContainersNote Note] understood \
by the [refMingusContainersNotecontainer NoteContainer]."""

		if hasattr(value, "notes"):
			pass
		elif hasattr(value, "name"):
			value = NoteContainer(value)
		elif type(value) == str:
			value = NoteContainer(value)
		elif type(value) == list:
			res = NoteContainer()
			for x in value:
				res + x
			value = res
		self.bar[index][2] = value

	def __repr__(self):
		"""Enables str() and repr() for Bars"""
		return str(self.bar)

	def __len__(self):
		"""Overloads the len() method for Bars"""
		return len(self.bar)

	def __eq__(self, other):
		"""Overloads the '==' operator for Bars"""
		for b in range(0, len(self.bar) - 1):
			if self.bar[b] != other.bar[b]:
				return False
		return True
