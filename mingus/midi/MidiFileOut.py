"""

================================================================================

	mingus - Music theory Python package, MIDI File Out
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

   MidiFileOut contains methods that can generate MIDI files from the 
   objects in mingus.containers.

================================================================================

"""
from MidiTrack import MidiTrack
from MidiFile import MidiFile


def write_Note(file, channel, note, bpm = 120, repeat = 0):
	"""Expects a Note object from mingus.containers and \
saves it into a midi file, specified in file."""
	m = MidiFile()
	t = MidiTrack(bpm)
	m.tracks = [t]
	while repeat >= 0:
		t.set_deltatime("\x00")
		t.play_Note(channel, note)
		t.set_deltatime("\x48")
		t.stop_Note(channel, note)
		repeat -= 1
	return m.write_file(file)

def write_NoteContainer(file, channel, notecontainer, bpm = 120, repeat = 0):
	"""Writes a mingus.NoteContainer to a midi file."""
	m = MidiFile()
	t = MidiTrack(bpm)
	m.tracks = [t]
	while repeat >= 0:
		t.set_deltatime("\x00")
		t.play_NoteContainer(channel, notecontainer)
		t.set_deltatime("\x48")
		t.stop_NoteContainer(channel, notecontainer)
		repeat -= 1
	return m.write_file(file)

def write_Bar(file, channel, bar, bpm = 120, repeat = 0):
	"""Writes a mingus.Bar to a midi file."""
	m = MidiFile()
	t = MidiTrack(bpm)
	m.tracks = [t]
	while repeat >= 0:
		t.play_Bar(channel, bar)
		repeat -= 1
	return m.write_file(file)

def write_Track(file, channel, track, bpm = 120, repeat = 0):
	"""Writes a mingus.Track to a midi file."""
	m = MidiFile()
	t = MidiTrack(bpm)
	m.tracks = [t]
	while repeat >= 0:
		t.play_Track(channel, track)
		repeat -= 1
	return m.write_file(file)

def write_Composition(file, channels, composition, bpm = 120, repeat = 0):
	"""Writes a mingus.Composition to a midi file."""
	m = MidiFile()
	t=[]
	for x in range(len(composition.tracks)):
		t += [MidiTrack(bpm)]
	m.tracks = t
	assert len(channels) >= len(composition.tracks)
	assert len(m.tracks) == len(channels)

	while repeat >= 0:
		for i in range(len(composition.tracks)):
			m.tracks[i].play_Track(channels[i], composition.tracks[i])
		repeat -= 1
	return m.write_file(file)

if __name__ == "__main__":
	from mingus.containers.NoteContainer import NoteContainer
	from mingus.containers.Bar import Bar
	from mingus.containers.Track import Track
	from mingus.containers.Instrument import MidiInstrument
	b = Bar()
	b2 = Bar('Ab', (3,4))
	n = NoteContainer(["A", "C", "E"])
	t = Track()
	b + n
	b + []
	b + n
	b + n
	b2 + n
	b2 + n
	b2 + []
	t + b
	t + b
	m = MidiInstrument()
	m.instrument_nr = 13
	t.instrument = m
	write_NoteContainer("test.mid", 1, n)
	write_Bar("test2.mid", 2, b)
	write_Bar("test3.mid", 2, b, 200)
	write_Bar("test4.mid", 2, b2, 200, 2)
	write_Track("test5.mid", 1, t, 120)
