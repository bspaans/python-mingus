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

   MidiFile contains two classes and some methods that can generate 
   MIDI files from the objects in mingus.containers.

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
	print m
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
	print m
	t = MidiTrack(bpm)
	m.tracks = [t]
	while repeat >= 0:
		t.play_Bar(channel, bar)
		repeat -= 1
	return m.write_file(file)

def write_Track(file, channel, track, bpm = 120, repeat = 0):
	"""Writes a mingus.Track to a midi file."""
	m = MidiFile()
	print m
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


if __name__ == '__main__':
	from mingus.containers.Bar import Bar
	from mingus.containers.Track import Track
	from mingus.containers.Composition import Composition

	b = Bar()
	c = Bar()

	b + 'C'
	b + 'E'
	b + 'G'
	b + ['B', 'F']

	c + 'Bb'
	c + 'F#'
	c + 'G#'
	c + 'Db'


	t = Track()
	s = Track()
	t + b
	t + c
	s + c
	s + b

	a = Composition()
	a + t
	a + s
	write_Bar("testmingus.mid", 1, b, 120, 10)
	write_NoteContainer("testmingus2.mid", 1, [50, 54, 57], 120, 0)
	write_Track("testmingus3.mid", 1, t, 120, 0)
	write_Composition("testmingus4.mid", [1, 2], a, 120, 0)

