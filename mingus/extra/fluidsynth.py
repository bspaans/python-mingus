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


fluid = None

def init_fluidsynth(server="localhost", port=9800):
	"""Initializes a connection to the fluidsynth server."""
	global fluid
	try:
		fluid = Telnet(server, port)
		return True
	except:
		return False


def play_Note(note, duration = 100, channel = 1):
	"""Sends a Note object as midi signal to the fluidsynth server."""
	try:
		fluid.write("noteon %d %d %d\n" % (channel, int(note), duration))
		return True
	except:
		return False


def stop_Note(note, channel = 1):
	"""Stops the Note playing at channel."""
	try:
		fluid.write("noteoff %d %d\n" % (channel, int(note)))
		return True
	except:
		return False

def play_NoteContainer(nc, duration = 100, channel = 1):
	"""Plays the Notes in the NoteContainer nc."""
	for note in nc:
		if not play_Note(note, duration, channel):
			return False
	return True

def stop_NoteContainer(nc, channel = 1):
	"""Stops playing the notes in NoteContainer nc."""
	for note in nc:
		if not stop_Note(note, channel):
			return False
	return True

def play_Bar(bar):
	"""Not implemented yet."""
	pass

def play_Track(track):
	"""Not implemented yet."""
	pass

def play_Song(song):
	"""Not implemented yet."""
	pass
