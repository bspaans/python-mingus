"""

================================================================================

	mingus - Music theory Python package, Track module
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

from mt_exceptions import InstrumentRangeError
from mingus.containers.Bar import Bar

class Track:
	"""The Track class can be used to store [refMingusContainersBar Bars] \
and to work on them. The class is also designed to be used with \
[refMingusContainersInstrument Instruments], but this is optional. \
Tracks can be stored together in [refMingusContainersComposition Compositions]"""

	bars = []
	instrument = None
	name = "Untitled" # Will be looked for when saving a MIDI file.
        tuning = None # Used by tablature

	def __init__(self, instrument = None):
		self.bars = []
		self.instrument = instrument

	def add_bar(self, bar):
		"""Adds a [refMingusContainersBar Bar] to the current track"""
		self.bars.append(bar)


	def add_notes(self, note, duration = None):
		"""Adds a [refMingusContainersNote Note], note as string or \
[refMingusContainersNotecontainer NoteContainer] to the last \
[refMingusContainersBar Bar]. If the [refMingusContainersBar Bar] is full, \
a new one will automatically be created. If the [refMingusContainersBar Bar] \
is not full but the note can't fit in, this method will return `False`. \
True otherwise. 

An !InstrumentRangeError exception will be raised if an \
[refMingusContainersInstrument Instrument] is attached to the Track, \
but the note turns out not to be within the range of the \
[refMingusContainersInstrument Instrument]."""

		if self.instrument != None:
			if not(self.instrument.can_play_notes(note)):
				raise InstrumentRangeError,\
					"Note '%s' is not in range of the instrument (%s)"\
					% (note, self.instrument)

		if duration == None:
			duration = 4

		# Check whether the last bar is full,
		# if so create a new bar and add the note there
		if len(self.bars) == 0:
			self.bars.append(Bar())
		last_bar = self.bars[-1]
		if last_bar.is_full():
			self.bars.append(Bar(last_bar.key, last_bar.meter))

		return self.bars[-1].place_notes(note, duration)
	
        def get_tuning(self):
                """Returns a StringTuning object. If an instrument is set and has a \
tuning it will be returned. Otherwise the track's one will be used."""
                if self.instrument and self.instrument.tuning:
                        return self.instrument.tuning
                return self.tuning

        def set_tuning(self, tuning):
                """Sets the tuning attribute on both the Track and its instrument (when available). \
Tuning should be a !StringTuning or derivative object."""
                if self.instrument:
                        self.instrument.tuning = tuning
                self.tuning = tuning
                return self

	def transpose(self, interval, up = True):
		"""Transposes all the notes in the track up or down the interval. Calls transpose() on every [refMingusContainersBar Bar]."""
		for bar in self.bars:
			bar.transpose(interval, up)

	def to_minor(self):
		"""Calls to_minor on all the bars in the Track."""
		for bar in self.bars:
			bar.to_minor()

	def to_major(self):
		"""Calls to_major on all the bars in the Track."""
		for bar in self.bars:
			bar.to_major()

	def augment(self):
		"""Calls augment on all the bars in the Track."""
		for bar in self.bars:
			bar.augment()

	def diminish(self):
		"""Calls diminish on all the bars in the Track."""
		for bar in self.bars:
			bar.diminish()

	def __add__(self, value):
		"""Overloads the + operator for Tracks. Accepts \
[refMingusContainersNote Notes], notes as string, \
[refMingusContainersNotecontainer NoteContainers] and \
[refMingusContainersBar Bars]."""

		if hasattr(value, "bar"):
			return self.add_bar(value)
		elif hasattr(value, "notes"):
			return self.add_notes(value)
		elif hasattr(value, "name") or type(value) == str:
			return self.add_notes(value)

	def test_integrity(self):
		"""Test whether all but the last [refMingusContainersBar Bars] \
contained in this track are full."""
		for b in self.bars[:-1]:
			if not ( b.is_full() ):
				return False
		return True

	def __eq__(self, other):
		"""Overloads the == operator for tracks."""
		for x in range(0, len(self.bars) - 1):
			if self.bars[x] != other.bars[x]:
				return False
		return True

	def __getitem__(self, index):
		"""Overloads the [] notation for Tracks"""
		return self.bars[index]

	def __setitem__(self, index, value):
		"""Overloads the [] = notation for Tracks. Throws an \
!UnexpectedObjectError if the value being set is not a \
[refMingusContainersBar mingus.containers.Bar] object."""

		if not ( hasattr (value, "bar") ):
			raise UnexpectedObjectError,\
				"Unexpected object '%s', expecting a mingus.containers.Bar"\
				"object" % value
		self.bars[index] = value

	def __repr__(self):
		"""The string representation of the class"""
		return str([self.instrument,self.bars])

	def __len__(self):
		"""Overloads the len() function for Tracks."""
		return len(self.bars)
