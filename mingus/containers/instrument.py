# -*- coding: utf-8 -*-

from __future__ import absolute_import

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
from mingus.containers.mt_exceptions import UnexpectedObjectError
import six


class Instrument:
    """
    The Instrument class is pretty self explanatory. Instruments can be used
    with Tracks to define which instrument plays what, with the added bonus
    of checking whether the entered notes are in the range of the
    instrument.

    It's probably easiest to subclass your own Instruments (see Piano and
    Guitar for examples).
    """
    def __init__(self, name, note_range=None, clef="bass and treble", tuning=None, bank=0):
        self.name = name
        if note_range is None:
            self.note_range = (Note("C", 0), Note("C", 8))
        self.clef = clef
        self.tuning = tuning
        self.bank = bank

    def set_range(self, note_range):
        """Set the note_rNGE of the instrument.

        A note_range is a tuple of two Notes or note strings.
        """
        if isinstance(note_range[0], six.string_types):
            note_range[0] = Note(note_range[0])
            note_range[1] = Note(note_range[1])
        if not hasattr(note_range[0], "name"):
            raise UnexpectedObjectError(
                "Unexpected object '%s'. " "Expecting a mingus.containers.Note object" % note_range[0]
            )
        self.note_range = note_range

    def note_in_range(self, note):
        """Test whether note is in the note_range of this Instrument.

        Return True if so, False otherwise.
        """
        if isinstance(note, six.string_types):
            note = Note(note)
        if not hasattr(note, "name"):
            raise UnexpectedObjectError(
                "Unexpected object '%s'. " "Expecting a mingus.containers.Note object" % note
            )
        if self.note_range[0] <= note <= self.note_range[1]:
            return True
        return False

    def notes_in_range(self, notes):
        """An alias for can_play_notes."""
        return self.can_play_notes(notes)

    def can_play_notes(self, notes):
        """Test if the notes lie within the note_range of the instrument.

        Return True if so, False otherwise.
        """
        if hasattr(notes, "notes"):
            notes = notes.notes
        if not isinstance(notes, list):
            notes = [notes]
        for n in notes:
            if not self.note_in_range(n):
                return False
        return True

    def __repr__(self):
        """Return a string representing the object."""
        return "%s [%s - %s]" % (self.name, self.note_range[0], self.note_range[1])


class Piano(Instrument):
    name = "Piano"
    note_range = (Note("F", 0), Note("B", 8))


class Guitar(Instrument):
    name = "Guitar"
    note_range = (Note("E", 3), Note("E", 7))
    clef = "Treble"

    def can_play_notes(self, notes):
        if len(notes) > 6:
            return False
        return Instrument.can_play_notes(self, notes)


class MidiInstrument(Instrument):
    names = [
        "Acoustic Grand Piano",
        "Bright Acoustic Piano",
        "Electric Grand Piano",
        "Honky-tonk Piano",
        "Electric Piano 1",
        "Electric Piano 2",
        "Harpsichord",
        "Clavi",
        "Celesta",
        "Glockenspiel",
        "Music Box",
        "Vibraphone",
        "Marimba",
        "Xylophone",
        "Tubular Bells",
        "Dulcimer",
        "Drawbar Organ",
        "Percussive Organ",
        "Rock Organ",
        "Church Organ",
        "Reed Organ",
        "Accordion",
        "Harmonica",
        "Tango Accordion",
        "Acoustic Guitar (nylon)",
        "Acoustic Guitar (steel)",
        "Electric Guitar (jazz)",
        "Electric Guitar (clean)",
        "Electric Guitar (muted)",
        "Overdriven Guitar",
        "Distortion Guitar",
        "Guitar harmonics",
        "Acoustic Bass",
        "Electric Bass (finger)",
        "Electric Bass (pick)",
        "Fretless Bass",
        "Slap Bass 1",
        "Slap Bass 2",
        "Synth Bass 1",
        "Synth Bass 2",
        "Violin",
        "Viola",
        "Cello",
        "Contrabass",
        "Tremolo Strings",
        "Pizzicato Strings",
        "Orchestral Harp",
        "Timpani",
        "String Ensemble 1",
        "String Ensemble 2",
        "SynthStrings 1",
        "SynthStrings 2",
        "Choir Aahs",
        "Voice Oohs",
        "Synth Voice",
        "Orchestra Hit",
        "Trumpet",
        "Trombone",
        "Tuba",
        "Muted Trumpet",
        "French Horn",
        "Brass Section",
        "SynthBrass 1",
        "SynthBrass 2",
        "Soprano Sax",
        "Alto Sax",
        "Tenor Sax",
        "Baritone Sax",
        "Oboe",
        "English Horn",
        "Bassoon",
        "Clarinet",
        "Piccolo",
        "Flute",
        "Recorder",
        "Pan Flute",
        "Blown Bottle",
        "Shakuhachi",
        "Whistle",
        "Ocarina",
        "Lead1 (square)",
        "Lead2 (sawtooth)",
        "Lead3 (calliope)",
        "Lead4 (chiff)",
        "Lead5 (charang)",
        "Lead6 (voice)",
        "Lead7 (fifths)",
        "Lead8 (bass + lead)",
        "Pad1 (new age)",
        "Pad2 (warm)",
        "Pad3 (polysynth)",
        "Pad4 (choir)",
        "Pad5 (bowed)",
        "Pad6 (metallic)",
        "Pad7 (halo)",
        "Pad8 (sweep)",
        "FX1 (rain)",
        "FX2 (soundtrack)",
        "FX 3 (crystal)",
        "FX 4 (atmosphere)",
        "FX 5 (brightness)",
        "FX 6 (goblins)",
        "FX 7 (echoes)",
        "FX 8 (sci-fi)",
        "Sitar",
        "Banjo",
        "Shamisen",
        "Koto",
        "Kalimba",
        "Bag pipe",
        "Fiddle",
        "Shanai",
        "Tinkle Bell",
        "Agogo",
        "Steel Drums",
        "Woodblock",
        "Taiko Drum",
        "Melodic Tom",
        "Synth Drum",
        "Reverse Cymbal",
        "Guitar Fret Noise",
        "Breath Noise",
        "Seashore",
        "Bird Tweet",
        "Telephone Ring",
        "Helicopter",
        "Applause",
        "Gunshot",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number = self.names.index(self.name)
