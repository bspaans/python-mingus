#!/usr/bin/env python 

from notes import Note, NoteGrouping
from mixins import Dim, Aug


CHORDS = {
  "major_triad": [0, 4, 7],
  "minor_triad": [0, 3, 7],
  "diminished_triad": [0, 3, 6],
  "augmented_triad": [0, 4, Aug(7)],
  "major_seventh": [0, 4, 7, 11],
  "minor_seventh": [0, 3, 7, 10],
  "dominant_seventh": [0, 4, 7, 10],
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
}
def _chord_to_notes(chord, on_note):
    return NoteGrouping(Note(on_note).transpose_list(CHORDS[chord]))

class Chords(object):
    pass


# Make all the chords in CHORDS into static methods on the Chords class
for chord in CHORDS.iterkeys():
    def create_chord_func(on_chord):
        def func(note):
            return _chord_to_notes(on_chord, note)
        setattr(Chords, on_chord, staticmethod(func))
    create_chord_func(chord)

SHORTHAND = { 
    # Triads
    'm': Chords.minor_triad,
    'M': Chords.major_triad,
    '': Chords.major_triad,
    'dim': Chords.diminished_triad,
    # Augmented 
    'aug': Chords.augmented_triad,
    '+': Chords.augmented_triad,
    #'7#5': Chords.augmented_minor_seventh,
    #'M7+5': Chords.augmented_minor_seventh,
    #'M7+': Chords.augmented_major_seventh,
    #'m7+': Chords.augmented_minor_seventh,
    #'7+': Chords.augmented_major_seventh,
    # Suspended
    #'sus47': Chords.suspended_seventh,
    #'sus4': Chords.suspended_fourth_triad,
    #'sus2': Chords.suspended_second_triad,
    #'sus': Chords.suspended_triad,
    #'11': Chords.eleventh,
    #'sus4b9': Chords.suspended_fourth_ninth,
    #'susb9': Chords.suspended_fourth_ninth,
    # Sevenths
    'm7': Chords.minor_seventh,
    'M7': Chords.major_seventh,
    '7': Chords.dominant_seventh,
    'dom7': Chords.dominant_seventh,
    'm7b5': Chords.minor_seventh_flat_five,
    #'dim7': Chords.diminished_seventh,
    'm/M7': Chords.minor_major_seventh,
    'mM7': Chords.minor_major_seventh,
    # Sixths
    'm6': Chords.minor_sixth,
    'M6': Chords.major_sixth,
    '6': Chords.major_sixth,
    '6/7': Chords.dominant_sixth,
    '67': Chords.dominant_sixth,
    # Ninths
    '6/9': Chords.sixth_ninth,
    '69': Chords.sixth_ninth,
    '9': Chords.dominant_ninth,
    '7b9': Chords.dominant_flat_ninth,
    #'7#9': Chords.dominant_sharp_ninth,
    'M9': Chords.major_ninth,
    'm9': Chords.minor_ninth,
    # Elevenths
    #'7#11': Chords.lydian_dominant_seventh,
    #'m11': Chords.minor_eleventh,
    # Thirteenths
    #'M13': Chords.major_thirteenth,
    #'m13': Chords.minor_thirteenth,
    #'13': Chords.dominant_thirteenth,
    # Altered chords
    #'7b5': Chords.dominant_flat_five,
    #'hendrix': Chords.hendrix_chord,
    #'7b12': Chords.hendrix_chord,
    }

