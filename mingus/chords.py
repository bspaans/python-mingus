from .notes import Note, NoteGrouping
from .mixins import Dim, Aug
import re


CHORDS = {
    "major_triad": [0, 4, 7],
    "minor_triad": [0, 3, 7],
    "diminished_triad": [0, 3, 6],
    "augmented_triad": [0, 4, Aug(7)],
    "augmented_minor_seventh": [0, 4, Aug(7), 10],
    "augmented_major_seventh": [0, 4, Aug(7), 11],
    "suspended_triad": [0, 5, 7],
    "suspended_fourth_triad": [0, 5, 7],
    "suspended_second_triad": [0, 2, 7],
    "suspended_seventh": [0, 5, 7, 10],
    "suspended_fourth_ninth": [0, 5, 7, 13],
    "major_seventh": [0, 4, 7, 11],
    "minor_seventh": [0, 3, 7, 10],
    "dominant_seventh": [0, 4, 7, 10],
    "diminished_seventh": [0, 3, 6, Dim(10)],
    "half_diminished_seventh": [0, 3, 6, 10],
    "minor_seventh_flat_five": [0, 3, 6, 10],
    "minor_major_seventh": [0, 3, 7, 11],
    "minor_sixth": [0, 3, 7, 8],
    "major_sixth": [0, 4, 7, 9],
    "dominant_sixth": [0, 4, 7, 9, 10],
    "sixth_ninth": [0, 4, 7, 9, 14],
    "minor_ninth": [0, 3, 7, 10, 14],
    "major_ninth": [0, 4, 7, 11, 14],
    "dominant_ninth": [0, 4, 7, 10, 14],
    "dominant_flat_ninth": [0, 4, 7, 10, 13],
    "dominant_sharp_ninth": [0, 4, 7, 10, Aug(14)],
    "eleventh": [0, 7, 10, 17],
    "minor_eleventh": [0, 3, 7, 10, 17],
    "lydian_dominant_seventh": [0, 4, 7, 10, Aug(17)],
    "minor_thirteenth": [0, 3, 7, 10, 14, 21],
    "major_thirteenth": [0, 4, 7, 11, 14, 21],
    "dominant_thirteenth": [0, 4, 7, 10, 14, 21],
    "dominant_flat_five": [0, 4, 6, 10],
    "hendrix_chord": [0, 4, 7, 10, 15],
}


def _chord_to_notes(chord, on_note):
    return NoteGrouping(Note(on_note).transpose_list(CHORDS[chord]))


_CHORD_MATCHER = re.compile("^(A|B|C|D|E|F|G)([#|b]*)([0-9]*)(.*)$")


class Chords(object):
    @staticmethod
    def normalize_shorthand_extension(extension):
        extension = extension.replace("min", "m")
        extension = extension.replace("mi", "m")
        extension = extension.replace("-", "m")
        extension = extension.replace("maj", "M")
        extension = extension.replace("ma", "M")
        return extension

    @staticmethod
    def from_string(shorthand):
        m = _CHORD_MATCHER.match(shorthand)
        if m is None:
            raise Exception("Unknown chord format: " + shorthand)

        base_name, accidentals, octave, extension = (
            m.group(1),
            m.group(2),
            m.group(3),
            m.group(4),
        )
        extension = Chords.normalize_shorthand_extension(extension)
        if extension not in SHORTHAND:
            raise Exception("Unknown chord extensions: " + extension)

        note = Note("%s%s%s" % (base_name, accidentals, octave))
        return SHORTHAND[extension](note)


# Make all the chords in CHORDS into static methods on the Chords class
for chord in CHORDS.keys():

    def create_chord_func(on_chord):
        def func(note):
            return _chord_to_notes(on_chord, note)

        setattr(Chords, on_chord, staticmethod(func))

    create_chord_func(chord)

SHORTHAND = {
    # Triads
    "m": Chords.minor_triad,
    "M": Chords.major_triad,
    "": Chords.major_triad,
    "dim": Chords.diminished_triad,
    # Augmented
    "aug": Chords.augmented_triad,
    "+": Chords.augmented_triad,
    "7#5": Chords.augmented_minor_seventh,
    "M7+5": Chords.augmented_minor_seventh,
    "M7+": Chords.augmented_major_seventh,
    "m7+": Chords.augmented_minor_seventh,
    "7+": Chords.augmented_major_seventh,
    # Suspended
    "sus47": Chords.suspended_seventh,
    "sus4": Chords.suspended_fourth_triad,
    "sus2": Chords.suspended_second_triad,
    "sus": Chords.suspended_triad,
    "sus4b9": Chords.suspended_fourth_ninth,
    "susb9": Chords.suspended_fourth_ninth,
    # Sevenths
    "m7": Chords.minor_seventh,
    "M7": Chords.major_seventh,
    "7": Chords.dominant_seventh,
    "dom7": Chords.dominant_seventh,
    "m7b5": Chords.minor_seventh_flat_five,
    "dim7": Chords.diminished_seventh,
    "m/M7": Chords.minor_major_seventh,
    "mM7": Chords.minor_major_seventh,
    # Sixths
    "m6": Chords.minor_sixth,
    "M6": Chords.major_sixth,
    "6": Chords.major_sixth,
    "6/7": Chords.dominant_sixth,
    "67": Chords.dominant_sixth,
    # Ninths
    "6/9": Chords.sixth_ninth,
    "69": Chords.sixth_ninth,
    "9": Chords.dominant_ninth,
    "7b9": Chords.dominant_flat_ninth,
    "7#9": Chords.dominant_sharp_ninth,
    "M9": Chords.major_ninth,
    "m9": Chords.minor_ninth,
    # Elevenths
    "11": Chords.eleventh,
    "m11": Chords.minor_eleventh,
    "7#11": Chords.lydian_dominant_seventh,
    # Thirteenths
    "M13": Chords.major_thirteenth,
    "m13": Chords.minor_thirteenth,
    "13": Chords.dominant_thirteenth,
    # Altered chords
    "7b5": Chords.dominant_flat_five,
    "hendrix": Chords.hendrix_chord,
    "7b12": Chords.hendrix_chord,
}
