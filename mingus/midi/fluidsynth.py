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

   fluidsynth is a software MIDI synthesizer which allows you to play the containers 
   in mingus.containers real-time. To work with this module, you'll 
   need fluidsynth and a nice instrument collection (look here: http://www.hammersound.net, go to Sounds -> Soundfont Library -> Collections).
   mingus uses the fluidsynth server to send the MIDI signals. To start a server
   instance of fluidsynth, use a command like this: 
   
   	fluidsynth -is -m alsa_seq ./nameofinstrbank.sf2

================================================================================

"""

from telnetlib import Telnet
from datetime import datetime
from MidiSequencer import MidiSequencer


fluid = None
midi = None


def init(server="localhost", port=9800):
	"""Initializes a connection to the fluidsynth server. 
	You have to call this function when you want the rest to work."""
	global fluid, midi
	try:
		fluid = Telnet(server, port)
		midi = MidiSequencer(fluid.write)
		return True
	except:
		return False


def init_fluidsynth(server="localhost", port=9800):
	"""Same as init(). Held for bugwards compatibility."""
	return init(server, port)


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

def play_Bars(bars, channels):
	"""Plays a list of bars on the given list of channels."""
	return midi.play_Bars(bars, channels)

def play_Track(track, channel = 1):
	"""Plays a Track object."""
	return midi.play_Track(track, channel)

def play_Tracks(tracks, channels):
	"""Plays a list of Tracks on the given list of channels."""
	return midi.play_Tracks(tracks, channels)

def play_Composition(composition, channels = None):
	"""Plays a composition."""
	return midi.play_Composition(composition, channels)

def control_change(channel, control, value):
	"""Sends a control change event on channel."""
	return midi.control_change(channel, control, value)


def set_instrument(channel, midi_instr):
	"""Sets the midi instrument on channel."""
	return midi.set_instrument(channel, midi_instr)

def stop_everything():
	"""Stops all the playing notes on all channels"""
	return midi.stop_everything()

def modulation(channel, value):
	return midi.modulation(channel, value)

def pan(channel, value):
	return midi.pan(channel, value)

def main_volume(channel, value):
	return midi.main_volume(channel, value)

def enable_reverb():
	return midi.write("reverb on\nrev_setroomsize 1\n")

def disable_reverb():
	return midi.write("reverb off\n")
