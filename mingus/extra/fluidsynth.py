"""

================================================================================

	mingus - Music theory Python package, fluidsynth module
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

   fluidsynth is a software MIDI synthesizer. To work with this module, you'll 
   need fluidsynth and a nice instrument collection (look here: *lookup url*).
   mingus uses the fluidsynth server to send the MIDI signals. To start a server
   instance of fluidsynth, use a command like this: 
   
   	fluidsynth -m alsa_seq ./nameofinstrbank.sf2 -i -s

   ** This module is in an experimental stage **

================================================================================

"""

from telnetlib import Telnet
from datetime import datetime
from midi import MIDI


fluid = None
midi = None


def init_fluidsynth(server="localhost", port=9800):
	"""Initializes a connection to the fluidsynth server."""
	global fluid, midi
	try:
		fluid = Telnet(server, port)
		midi = MIDI(fluid.write)
		return True
	except:
		return False


def play_Note(note, velocity = 100, channel = 1):
	"""Sends a Note object as midi signal to the fluidsynth server."""
	return midi.play_Note(note, channel, velocity)


def stop_Note(note, channel = 1):
	"""Stops the Note playing at channel."""
	return midi.stop_Note(note, channel)


def play_NoteContainer(nc, velocity = 100, channel = 1):
	"""Plays the Notes in the NoteContainer nc."""
	return midi.play_NoteContainer(nc, channel, velocity)

def stop_NoteContainer(nc, channel = 1):
	"""Stops playing the notes in NoteContainer nc."""
	return midi.stop_NoteContainer(nc, channel)

def play_Bar(bar, duration = 2000, channel = 1):
	"""Plays a Bar object. The duration is the duration of the whole bar in milliseconds.\
The default is set to 2000 ms which is good for 120bpm when playing 4/4 bars."""
	return midi.play_Bar(bar, channel, duration)

def play_Track(track, channel = 1):
	"""Plays a Track object."""
	return midi.play_Track(track, channel)

def play_Composition(song):
	"""Plays a composition."""
	pass
