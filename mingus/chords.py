#!/usr/bin/env python 

from notes import Note, NoteGrouping


CHORDS = {
  "major_triad": [0, 4, 7],
  "minor_triad": [0, 3, 7],
  "diminished_triad": [0, 3, 6],
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


# Make all the chords static methods on the Chords class
for chord in CHORDS.iterkeys():
    def create_chord_func(on_chord):
        def func(note):
            return _chord_to_notes(on_chord, note)
        setattr(Chords, on_chord, staticmethod(func))
    create_chord_func(chord)

