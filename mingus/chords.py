#!/usr/bin/env python 

from notes import Note, NoteGrouping
from mixins import TransposeMixin, CloneMixin

class BaseTransposer(TransposeMixin, CloneMixin):
    def __init__(self, transpose_with):
        self.transpose_with = transpose_with
    def transpose_base(self, base):
        return [base.transpose(x) for x in self.transpose_with]
    def set_transpose(self, amount):
        self.transpose_with = [ t + amount for t in self.transpose_with ]
        return self

CHORDS = {
  "major_triad": BaseTransposer([0, 4, 7]),
  "minor_triad": BaseTransposer([0, 3, 7]),
  "diminished_triad": BaseTransposer([0, 3, 6]),
  "major_seventh": BaseTransposer([0, 4, 7, 11]),
  "minor_seventh": BaseTransposer([0, 3, 7, 10]),
  "dominant_seventh": BaseTransposer([0, 4, 7, 10]),
  "half_diminished_seventh": BaseTransposer([0, 3, 6, 10]),
  "minor_seventh_flat_five": BaseTransposer([0, 3, 6, 10]),
  "minor_major_seventh": BaseTransposer([0, 3, 7, 11]),
  "minor_sixth": BaseTransposer([0, 3, 7, 8]),
  "major_sixth": BaseTransposer([0, 4, 7, 9]),
  "dominant_sixth": BaseTransposer([0, 4, 7, 9, 10]),
  "sixth_ninth": BaseTransposer([0, 4, 7, 9, 14]),
  "minor_ninth": BaseTransposer([0, 3, 7, 10, 14]),
  "major_ninth": BaseTransposer([0, 4, 7, 11, 14]),
  "dominant_ninth": BaseTransposer([0, 4, 7, 10, 14]),
  "dominant_flat_ninth": BaseTransposer([0, 4, 7, 10, 13]),
}

def _chord_to_notes(chord, on_note):
    base = Note(on_note)
    return NoteGrouping(CHORDS[chord].transpose_base(base))

class Chords(object):
    pass

for chord in CHORDS.iterkeys():
    def create_chord_func(on_chord):
        def func(note):
            return _chord_to_notes(on_chord, note)
        setattr(Chords, on_chord, staticmethod(func))
    create_chord_func(chord)

