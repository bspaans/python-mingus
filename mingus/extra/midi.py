"""

================================================================================

	mingus - Music theory Python package, MIDI sequencer
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

   This module provides an object which can turn your container objects
   into MIDI messages. 

================================================================================

"""

from datetime import datetime

class MIDI:

	output = None
	bpm = 120  # beats per minute
	tick = 500 # ms
	play = False


	def __init__(self, output_function):

		self.output = output_function


	def write(self, msg):
		"""Writes a message to the output function."""
		try:
			self.output(msg)
			return True
		except:
			return False



	def play_Note(self, note, channel = 1, velocity = 100):
		"""Plays a Note object on a channel[1-16] with a velocity[0-127]."""
		return self.write("noteon %d %d %d\n" % (channel, int(note) + 12, velocity))



	def stop_Note(self, note, channel = 1):
		"""Stops a note on a channel."""
		return self.write("noteoff %d %d\n" % (channel, int(note) + 12))




	def play_NoteContainer(self, nc, channel = 1, velocity = 100):
		"""Plays the Notes in the NoteContainer nc."""
		for note in nc:
			if not self.play_Note(note, channel, velocity):
				return False
		return True



	def stop_NoteContainer(self, nc, channel = 1):
		"""Stops playing the notes in NoteContainer nc."""
		for note in nc:
			if not self.stop_Note(note, channel):
				return False
		return True



	def play_Bar(self, bar, channel = 1, duration = 2000):
		"""Plays a Bar object. The duration is the duration of the \
whole bar in milliseconds. The default is set to 2000 ms which is good for \
120 bpm when playing bars in 4/4."""
		for nc in bar:
			n = datetime.now()

			if not self.play_NoteContainer(nc[2], channel, 100):
				return False
			a = datetime.now()
			
			while (a - n).microseconds / 1000.0 < (duration * (1.0 / nc[1])):
				a = datetime.now()

			self.stop_NoteContainer(nc[2], channel)

		return True


	def play_Bars(self, bars, channels, duration = 2000):
		"""Plays several bars at the same time."""
		tick = 0.0
		cur = []
		playing = []

		for x in bars:
			cur.append(0)

		n = datetime.now()
		a = datetime.now()
		
		while tick < bars[0].length:
			for x in range(len(bars)):
				bar = bars[x]
				current_nc = bar[cur[x]]
				if current_nc[0] <= tick and \
					current_nc[0] + \
					(1.0 / current_nc[1]) >= tick \
					and current_nc not in playing:

					print "play", current_nc, tick
					self.play_NoteContainer(current_nc[2])
					playing.append(current_nc)
					if cur[x] != len(bar) - 1:
						cur[x] += 1

			for p in playing:
				if p[0] + (1.0 / p[1]) <= tick:
					print "stop", p, tick
					self.stop_NoteContainer(p[2])
					playing.remove(p)

			a = datetime.now()

			millis = (a - n).microseconds / 1000.0 + (a - n).seconds * 1000.0
			tick = (millis / duration) * bars[0].length
			

		return True





	def play_Track(self, track, channel = 1):
		"""Plays a Track object."""
		for bar in track:
			# bpm attribute needed? Or just another argument?
			if not self.play_Bar(bar, channel, 2000):
				return False
		return True
