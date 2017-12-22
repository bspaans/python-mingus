#!/usr/bin/python
# -*- coding: utf-8 -*-

#    mingus - Music theory Python package, instrument module.
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

from mingus.containers.note import Note
from .mt_exceptions import UnexpectedObjectError

class Instrument(object):

    """An instrument object.

    The Instrument class is pretty self explanatory. Instruments can be used
    with Tracks to define which instrument plays what, with the added bonus
    of checking whether the entered notes are in the range of the
    instrument.

    It's probably easiest to subclass your own Instruments (see Piano and
    Guitar for examples).
    """

    name = 'Instrument'
    range = (Note('C', 0), Note('C', 8))
    clef = 'bass and treble'
    tuning = None  # optional StringTuning object

    def __init__(self):
        pass

    def set_range(self, range):
        """Set the range of the instrument.

        A range is a tuple of two Notes or note strings.
        """
        if type(range[0]) == str:
            range[0] = Note(range[0])
            range[1] = Note(range[1])
        if not hasattr(range[0], 'name'):
            raise UnexpectedObjectError("Unexpected object '%s'. "
                    "Expecting a mingus.containers.Note object" % range[0])
        self.range = range

    def note_in_range(self, note):
        """Test whether note is in the range of this Instrument.

        Return True if so, False otherwise.
        """
        if type(note) == str:
            note = Note(note)
        if not hasattr(note, 'name'):
            raise UnexpectedObjectError("Unexpected object '%s'. "
                    "Expecting a mingus.containers.Note object" % note)
        if note >= self.range[0] and note <= self.range[1]:
            return True
        return False

    def notes_in_range(self, notes):
        """An alias for can_play_notes."""
        return can_play_notes(notes)

    def can_play_notes(self, notes):
        """Test if the notes lie within the range of the instrument.

        Return True if so, False otherwise.
        """
        if hasattr(notes, 'notes'):
            notes = notes.notes
        if type(notes) != list:
            notes = [notes]
        for n in notes:
            if not self.note_in_range(n):
                return False
        return True

    def __repr__(self):
        """Return a string representing the object."""
        return '%s [%s - %s]' % (self.name, self.range[0], self.range[1])


class Piano(Instrument):

    name = 'Piano'
    range = (Note('F', 0), Note('B', 8))

    def __init__(self):
        Instrument.__init__(self)


class Guitar(Instrument):

    name = 'Guitar'
    range = (Note('E', 3), Note('E', 7))
    clef = 'Treble'

    def __init__(self):
        Instrument.__init__(self)

    def can_play_notes(self, notes):
        if len(notes) > 6:
            return False
        return Instrument.can_play_notes(self, notes)


class MidiInstrument(Instrument):

    range = (Note('C', 0), Note('B', 8))
    instrument_nr = 1
    name = ''
    names = [
        'Acoustic Grand Piano',
        'Bright Acoustic Piano',
        'Electric Grand Piano',
        'Honky-tonk Piano',
        'Electric Piano 1',
        'Electric Piano 2',
        'Harpsichord',
        'Clavi',
        'Celesta',
        'Glockenspiel',
        'Music Box',
        'Vibraphone',
        'Marimba',
        'Xylophone',
        'Tubular Bells',
        'Dulcimer',
        'Drawbar Organ',
        'Percussive Organ',
        'Rock Organ',
        'Church Organ',
        'Reed Organ',
        'Accordion',
        'Harmonica',
        'Tango Accordion',
        'Acoustic Guitar (nylon)',
        'Acoustic Guitar (steel)',
        'Electric Guitar (jazz)',
        'Electric Guitar (clean)',
        'Electric Guitar (muted)',
        'Overdriven Guitar',
        'Distortion Guitar',
        'Guitar harmonics',
        'Acoustic Bass',
        'Electric Bass (finger)',
        'Electric Bass (pick)',
        'Fretless Bass',
        'Slap Bass 1',
        'Slap Bass 2',
        'Synth Bass 1',
        'Synth Bass 2',
        'Violin',
        'Viola',
        'Cello',
        'Contrabass',
        'Tremolo Strings',
        'Pizzicato Strings',
        'Orchestral Harp',
        'Timpani',
        'String Ensemble 1',
        'String Ensemble 2',
        'SynthStrings 1',
        'SynthStrings 2',
        'Choir Aahs',
        'Voice Oohs',
        'Synth Voice',
        'Orchestra Hit',
        'Trumpet',
        'Trombone',
        'Tuba',
        'Muted Trumpet',
        'French Horn',
        'Brass Section',
        'SynthBrass 1',
        'SynthBrass 2',
        'Soprano Sax',
        'Alto Sax',
        'Tenor Sax',
        'Baritone Sax',
        'Oboe',
        'English Horn',
        'Bassoon',
        'Clarinet',
        'Piccolo',
        'Flute',
        'Recorder',
        'Pan Flute',
        'Blown Bottle',
        'Shakuhachi',
        'Whistle',
        'Ocarina',
        'Lead1 (square)',
        'Lead2 (sawtooth)',
        'Lead3 (calliope)',
        'Lead4 (chiff)',
        'Lead5 (charang)',
        'Lead6 (voice)',
        'Lead7 (fifths)',
        'Lead8 (bass + lead)',
        'Pad1 (new age)',
        'Pad2 (warm)',
        'Pad3 (polysynth)',
        'Pad4 (choir)',
        'Pad5 (bowed)',
        'Pad6 (metallic)',
        'Pad7 (halo)',
        'Pad8 (sweep)',
        'FX1 (rain)',
        'FX2 (soundtrack)',
        'FX 3 (crystal)',
        'FX 4 (atmosphere)',
        'FX 5 (brightness)',
        'FX 6 (goblins)',
        'FX 7 (echoes)',
        'FX 8 (sci-fi)',
        'Sitar',
        'Banjo',
        'Shamisen',
        'Koto',
        'Kalimba',
        'Bag pipe',
        'Fiddle',
        'Shanai',
        'Tinkle Bell',
        'Agogo',
        'Steel Drums',
        'Woodblock',
        'Taiko Drum',
        'Melodic Tom',
        'Synth Drum',
        'Reverse Cymbal',
        'Guitar Fret Noise',
        'Breath Noise',
        'Seashore',
        'Bird Tweet',
        'Telephone Ring',
        'Helicopter',
        'Applause',
        'Gunshot',
        ]

    def __init__(self, name=''):
        self.name = name

class MidiPercussionInstrument(Instrument):
    def __init__(self):
        super(MidiPercussionInstrument, self).__init__()
        self.name = "Midi Percussion"
        self.mapping = {
            35: "Acoustic Bass Drum",
            36: "Bass Drum 1",
            37: "Side Stick",
            38: "Acoustic Snare",
            39: "Hand Clap",
            40: "Electric Snare",
            41: "Low Floor Tom",
            42: "Closed Hi Hat",
            43: "High Floor Tom",
            44: "Pedal Hi-Hat",
            45: "Low Tom",
            46: "Open Hi-Hat",
            47: "Low-Mid Tom",
            48: "Hi Mid Tom",
            49: "Crash Cymbal 1",
            50: "High Tom",
            51: "Ride Cymbal 1",
            52: "Chinese Cymbal",
            53: "Ride Bell",
            54: "Tambourine",
            55: "Splash Cymbal",
            56: "Cowbell",
            57: "Crash Cymbal 2",
            58: "Vibraslap",
            59: "Ride Cymbal 2",
            60: "Hi Bongo",
            61: "Low Bongo",
            62: "Mute Hi Conga",
            63: "Open Hi Conga",
            64: "Low Conga",
            65: "High Timbale",
            66: "Low Timbale",
            67: "High Agogo",
            68: "Low Agogo",
            69: "Cabasa",
            70: "Maracas",
            71: "Short Whistle",
            72: "Long Whistle",
            73: "Short Guiro",
            74: "Long Guiro",
            75: "Claves",
            76: "Hi Wood Block",
            77: "Low Wood Block",
            78: "Mute Cuica",
            79: "Open Cuica",
            80: "Mute Triangle",
            81: "Open Triangle"
        }

    def acoustic_bass_drum(self):
        return Note(35 - 12)

    def bass_drum_1(self):
        return Note(36 - 12)

    def side_stick(self):
        return Note(37 - 12)

    def acoustic_snare(self):
        return Note(38 - 12)

    def hand_clap(self):
        return Note(39 - 12)

    def electric_snare(self):
        return Note(40 - 12)

    def low_floor_tom(self):
        return Note(41 - 12)

    def closed_hi_hat(self):
        return Note(42 - 12)

    def high_floor_tom(self):
        return Note(43 - 12)

    def pedal_hi_hat(self):
        return Note(44 - 12)

    def low_tom(self):
        return Note(45 - 12)

    def open_hi_hat(self):
        return Note(46 - 12)

    def low_mid_tom(self):
        return Note(47 - 12)

    def hi_mid_tom(self):
        return Note(48 - 12)

    def crash_cymbal_1(self):
        return Note(49 - 12)

    def high_tom(self):
        return Note(50 - 12)

    def ride_cymbal_1(self):
        return Note(51 - 12)

    def chinese_cymbal(self):
        return Note(52 - 12)

    def ride_bell(self):
        return Note(53 - 12)

    def tambourine(self):
        return Note(54 - 12)

    def splash_cymbal(self):
        return Note(55 - 12)

    def cowbell(self):
        return Note(56 - 12)

    def crash_cymbal_2(self):
        return Note(57 - 12)

    def vibraslap(self):
        return Note(58 - 12)

    def ride_cymbal_2(self):
        return Note(59 - 12)

    def hi_bongo(self):
        return Note(60 - 12)

    def low_bongo(self):
        return Note(61 - 12)

    def mute_hi_conga(self):
        return Note(62 - 12)

    def open_hi_conga(self):
        return Note(63 - 12)

    def low_conga(self):
        return Note(64 - 12)

    def high_timbale(self):
        return Note(65 - 12)

    def low_timbale(self):
        return Note(66 - 12)

    def high_agogo(self):
        return Note(67 - 12)

    def low_agogo(self):
        return Note(68 - 12)

    def cabasa(self):
        return Note(69 - 12)

    def maracas(self):
        return Note(70 - 12)

    def short_whistle(self):
        return Note(71 - 12)

    def long_whistle(self):
        return Note(72 - 12)

    def short_guiro(self):
        return Note(73 - 12)

    def long_guiro(self):
        return Note(74 - 12)

    def claves(self):
        return Note(75 - 12)

    def hi_wood_block(self):
        return Note(76 - 12)

    def low_wood_block(self):
        return Note(77 - 12)

    def mute_cuica(self):
        return Note(78 - 12)

    def open_cuica(self):
        return Note(79 - 12)

    def mute_triangle(self):
        return Note(80 - 12)

    def open_triangle(self):
        return Note(81 - 12)

