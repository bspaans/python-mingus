"""

================================================================================

	mingus - Music theory Python package, MIDI File
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

   This module holds the class that is used when writing (and in the future reading) midi files.

================================================================================

"""
from binascii import a2b_hex

class MidiFile():
	"""This class generates midi files from MidiTracks. """

	tracks = []
	time_division = "\x00\x48"

	def __init__(self, tracks = []):
		self.reset()
		self.tracks = tracks

	def get_midi_data(self):
		"""Collects and returns the raw, binary MIDI data
		from the tracks."""
		tracks = [ t.get_midi_data() for t in self.tracks if \
				t.track_data != '']
		return self.header() + "".join(tracks)

	def header(self):
		"""Returns a header for type 1 midi file"""
		tracks = a2b_hex("%04x" % len([ t for t in self.tracks if\
						t.track_data != '']))
		return "MThd\x00\x00\x00\x06\x00\x01" + tracks + self.time_division

	def reset(self):
		"""Resets every track."""
		[ t.reset() for t in self.tracks ]

	def write_file(self, file):
		"""Collects the data from get_midi_data and writes to file. """
		"""Returns True on success. False on failure."""
		dat = self.get_midi_data()
		try:
			f = open(file, "wb")
		except:
			print "Couldn't open '%s' for writing." % file
			return False
		try:
			f.write(dat)
		except:
			print "An error occured while writing data to %s." % file
			return False
		f.close()
		print "Written %d bytes to %s." % (len(dat), file)
		return True
