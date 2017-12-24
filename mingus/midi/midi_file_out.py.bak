#!/usr/bin/python
# -*- coding: utf-8 -*-

#    mingus - Music theory Python package, midi_file_out module.
#    Copyright (C) 2008-2009, Bart Spaans
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Functions that can generate MIDI files from the objects in
mingus.containers."""

from midi_track import MidiTrack
from binascii import a2b_hex

class MidiFile(object):

    """A class that generates MIDI files from MidiTracks."""

    tracks = []
    time_division = "\x00\x48"

    def __init__(self, tracks=[]):
        self.reset()
        self.tracks = tracks

    def get_midi_data(self):
        """Collect and return the raw, binary MIDI data from the tracks."""
        tracks = [t.get_midi_data() for t in self.tracks if t.track_data != '']
        return self.header() + ''.join(tracks)

    def header(self):
        """Return a header for type 1 MIDI file."""
        tracks = a2b_hex('%04x' % len([t for t in self.tracks if
            t.track_data != '']))
        return 'MThd\x00\x00\x00\x06\x00\x01' + tracks + self.time_division

    def reset(self):
        """Reset every track."""
        [t.reset() for t in self.tracks]

    def write_file(self, file, verbose=False):
        """Collect the data from get_midi_data and write to file."""
        dat = self.get_midi_data()
        try:
            f = open(file, 'wb')
        except:
            print "Couldn't open '%s' for writing." % file
            return False
        try:
            f.write(dat)
        except:
            print 'An error occured while writing data to %s.' % file
            return False
        f.close()
        if verbose:
            print 'Written %d bytes to %s.' % (len(dat), file)
        return True


def write_Note(file, note, bpm=120, repeat=0, verbose=False):
    """Expect a Note object from mingus.containers and save it into a MIDI
    file, specified in file.

    You can set the velocity and channel in Note.velocity and Note.channel.
    """
    m = MidiFile()
    t = MidiTrack(bpm)
    m.tracks = [t]
    while repeat >= 0:
        t.set_deltatime('\x00')
        t.play_Note(note)
        t.set_deltatime("\x48")
        t.stop_Note(note)
        repeat -= 1
    return m.write_file(file, verbose)

def write_NoteContainer(file, notecontainer, bpm=120, repeat=0, verbose=False):
    """Write a mingus.NoteContainer to a MIDI file."""
    m = MidiFile()
    t = MidiTrack(bpm)
    m.tracks = [t]
    while repeat >= 0:
        t.set_deltatime('\x00')
        t.play_NoteContainer(notecontainer)
        t.set_deltatime("\x48")
        t.stop_NoteContainer(notecontainer)
        repeat -= 1
    return m.write_file(file, verbose)

def write_Bar(file, bar, bpm=120, repeat=0, verbose=False):
    """Write a mingus.Bar to a MIDI file.

    Both the key and the meter are written to the file as well.
    """
    m = MidiFile()
    t = MidiTrack(bpm)
    m.tracks = [t]
    while repeat >= 0:
        t.play_Bar(bar)
        repeat -= 1
    return m.write_file(file, verbose)

def write_Track(file, track, bpm=120, repeat=0, verbose=False):
    """Write a mingus.Track to a MIDI file.

    Write the name to the file and set the instrument if the instrument has
    the attribute instrument_nr, which represents the MIDI instrument
    number. The class MidiInstrument in mingus.containers.Instrument has
    this attribute by default.
    """
    m = MidiFile()
    t = MidiTrack(bpm)
    m.tracks = [t]
    while repeat >= 0:
        t.play_Track(track)
        repeat -= 1
    return m.write_file(file, verbose)

def write_Composition(file, composition, bpm=120, repeat=0, verbose=False):
    """Write a mingus.Composition to a MIDI file."""
    m = MidiFile()
    t = []
    for x in range(len(composition.tracks)):
        t += [MidiTrack(bpm)]
    m.tracks = t
    while repeat >= 0:
        for i in range(len(composition.tracks)):
            m.tracks[i].play_Track(composition.tracks[i])
        repeat -= 1
    return m.write_file(file, verbose)

if __name__ == '__main__':
    from mingus.containers.NoteContainer import NoteContainer
    from mingus.containers.Bar import Bar
    from mingus.containers.Track import Track
    from mingus.containers.Instrument import MidiInstrument
    b = Bar()
    b2 = Bar('Ab', (3, 4))
    n = NoteContainer(['A', 'C', 'E'])
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
    t.name = 'Track Name Test'
    write_NoteContainer('test.mid', n)
    write_Bar('test2.mid', b)
    write_Bar('test3.mid', b, 200)
    write_Bar('test4.mid', b2, 200, 2)
    write_Track('test5.mid', t, 120)

