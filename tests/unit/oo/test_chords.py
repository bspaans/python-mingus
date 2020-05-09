from mingus.chords import Chords
from mingus.notes import Note
from hamcrest import *
from .common import _chord_tester


def test_Chord_major_triad():
    chord = Chords.major_triad("C4")
    _chord_tester(chord, ["C4", "E4", "G4"])


def test_Chord_major_triad_on_Note():
    chord = Chords.major_triad(Note("C4"))
    _chord_tester(chord, ["C4", "E4", "G4"])


def test_Chord_major_triad_on_int():
    chord = Chords.major_triad(60)
    _chord_tester(chord, ["C4", "E4", "G4"])


def test_Chord_minor_triad():
    chord = Chords.minor_triad("C4")
    _chord_tester(chord, ["C4", "Eb4", "G4"])


def test_Chord_diminished_triad():
    chord = Chords.diminished_triad("C4")
    _chord_tester(chord, ["C4", "Eb4", "Gb4"])


def test_Chord_augmented_triad():
    chord = Chords.augmented_triad("C4")
    _chord_tester(chord, ["C4", "E4", "G#4"])


def test_Chord_augmented_minor_seventh():
    chord = Chords.augmented_minor_seventh("C4")
    _chord_tester(chord, ["C4", "E4", "G#4", "Bb4"])


def test_Chord_augmented_major_seventh():
    chord = Chords.augmented_major_seventh("C4")
    _chord_tester(chord, ["C4", "E4", "G#4", "B4"])


def test_Chord_suspended_triad():
    chord = Chords.suspended_triad("C4")
    _chord_tester(chord, ["C4", "F4", "G4"])


def test_Chord_suspended_fourth_triad():
    chord = Chords.suspended_fourth_triad("C4")
    _chord_tester(chord, ["C4", "F4", "G4"])


def test_Chord_suspended_second_triad():
    chord = Chords.suspended_second_triad("C4")
    _chord_tester(chord, ["C4", "D4", "G4"])


def test_Chord_suspended_seventh():
    chord = Chords.suspended_seventh("C4")
    _chord_tester(chord, ["C4", "F4", "G4", "Bb4"])


def test_Chord_suspended_fourth_ninth():
    chord = Chords.suspended_fourth_ninth("C4")
    _chord_tester(chord, ["C4", "F4", "G4", "Db5"])


def test_Chord_eleventh():
    chord = Chords.eleventh("C4")
    _chord_tester(chord, ["C4", "G4", "Bb4", "F5"])


def test_Chord_minor_eleventh():
    chord = Chords.minor_eleventh("C4")
    _chord_tester(chord, ["C4", "Eb4", "G4", "Bb4", "F5"])


def test_Chord_lydian_dominant_seventh():
    chord = Chords.lydian_dominant_seventh("C4")
    _chord_tester(chord, ["C4", "E4", "G4", "Bb4", "F#5"])


def test_Chord_minor_thirteenth():
    chord = Chords.minor_thirteenth("C4")
    _chord_tester(chord, ["C4", "Eb4", "G4", "Bb4", "D5", "A5"])


def test_Chord_major_thirteenth():
    chord = Chords.major_thirteenth("C4")
    _chord_tester(chord, ["C4", "E4", "G4", "B4", "D5", "A5"])


def test_Chord_dominant_thirteenth():
    chord = Chords.dominant_thirteenth("C4")
    _chord_tester(chord, ["C4", "E4", "G4", "Bb4", "D5", "A5"])


def test_Chord_major_seventh():
    chord = Chords.major_seventh("C4")
    _chord_tester(chord, ["C4", "E4", "G4", "B4"])


def test_Chord_minor_seventh():
    chord = Chords.minor_seventh("C4")
    _chord_tester(chord, ["C4", "Eb4", "G4", "Bb4"])


def test_Chord_dominant_seventh():
    chord = Chords.dominant_seventh("C4")
    _chord_tester(chord, ["C4", "E4", "G4", "Bb4"])


def test_Chord_diminished_seventh():
    chord = Chords.diminished_seventh("C4")
    _chord_tester(chord, ["C4", "Eb4", "Gb4", "Bbb4"])


def test_Chord_half_diminished_seventh():
    chord = Chords.half_diminished_seventh("C4")
    _chord_tester(chord, ["C4", "Eb4", "Gb4", "Bb4"])


def test_Chord_minor_seventh_flat_five():
    chord = Chords.minor_seventh_flat_five("C4")
    _chord_tester(chord, ["C4", "Eb4", "Gb4", "Bb4"])


def test_Chord_minor_major_seventh():
    chord = Chords.minor_major_seventh("C4")
    _chord_tester(chord, ["C4", "Eb4", "G4", "B4"])


def test_Chord_minor_sixth():
    chord = Chords.minor_sixth("C4")
    _chord_tester(chord, ["C4", "Eb4", "G4", "Ab4"])


def test_Chord_major_sixth():
    chord = Chords.major_sixth("C4")
    _chord_tester(chord, ["C4", "E4", "G4", "A4"])


def test_Chord_dominant_sixth():
    chord = Chords.dominant_sixth("C4")
    _chord_tester(chord, ["C4", "E4", "G4", "A4", "Bb4"])


def test_Chord_sixth_ninth():
    chord = Chords.sixth_ninth("C4")
    _chord_tester(chord, ["C4", "E4", "G4", "A4", "D5"])


def test_Chord_minor_ninth():
    chord = Chords.minor_ninth("C4")
    _chord_tester(chord, ["C4", "Eb4", "G4", "Bb4", "D5"])


def test_Chord_dominant_ninth():
    chord = Chords.dominant_ninth("C4")
    _chord_tester(chord, ["C4", "E4", "G4", "Bb4", "D5"])


def test_Chord_dominant_flat_ninth():
    chord = Chords.dominant_flat_ninth("C4")
    _chord_tester(chord, ["C4", "E4", "G4", "Bb4", "Db5"])


def test_Chord_dominant_sharp_ninth():
    chord = Chords.dominant_sharp_ninth("C4")
    _chord_tester(chord, ["C4", "E4", "G4", "Bb4", "D#5"])


def test_Chord_dominant_flat_five():
    chord = Chords.dominant_flat_five("C4")
    _chord_tester(chord, ["C4", "E4", "Gb4", "Bb4"])


def test_Chord_hendrix_chord():
    chord = Chords.hendrix_chord("C4")
    _chord_tester(chord, ["C4", "E4", "G4", "Bb4", "Eb5"])


def test_Chord_from_string():
    _chord_tester(Chords.from_string("Cmaj7"), ["C4", "E4", "G4", "B4"])
    _chord_tester(Chords.from_string("C4maj7"), ["C4", "E4", "G4", "B4"])
    _chord_tester(Chords.from_string("CM7"), ["C4", "E4", "G4", "B4"])
    _chord_tester(Chords.from_string("Cm7"), ["C4", "Eb4", "G4", "Bb4"])
    _chord_tester(Chords.from_string("Cmin7"), ["C4", "Eb4", "G4", "Bb4"])
    _chord_tester(Chords.from_string("Cmi7"), ["C4", "Eb4", "G4", "Bb4"])
    _chord_tester(Chords.from_string("C-7"), ["C4", "Eb4", "G4", "Bb4"])
    _chord_tester(Chords.from_string("C3-7"), ["C3", "Eb3", "G3", "Bb3"])
