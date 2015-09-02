#!/usr/bin/env python

from chords import BaseTransposer
from notes import Note

class Scale(object):
    def __init__(self, on_note):
        self.on_note = Note(on_note)
        self.scale = set([])
        self.build_scale(self.on_note)
    def _scale_builder(self, intervals, base_note):
        notes = BaseTransposer(intervals).transpose_base(base_note)
        self.scale = [ (n._base_name, n._accidentals) for n in notes ]
    def __contains__(self, item):
        return self.is_in_scale(item)
    def is_in_scale(self, item):
        return (item._base_name, item._accidentals) in self.scale
    def build_scale(self, note):
        pass
    def next(self, note):
        note = Note(note)
        lookup = (note._base_name, note._accidentals)
        if lookup in self.scale:
            ix = self.scale.index(lookup)
            next_ix = (ix + 1) % (len(self.scale))
        else:
            # best guess. raise exception instead?
            for ix, n in enumerate(self.scale):
                if n[0] == note._base_name:
                    next_ix = (ix + 1) % (len(self.scale))
        next_note = self.scale[next_ix]
        new_note = Note()
        new_note._base_name = next_note[0]
        new_note._accidentals = next_note[1]
        while int(new_note) < int(note):
            new_note.set_octave_up()
        return new_note

    def triad(self, note):
        note = Note(note)
        third = self.next(self.next(note))
        fifth = self.next(self.next(third))
        return [note, third, fifth]

    def triads(self):
        n = self.on_note
        triads = []
        while int(n) - int(self.on_note) < 12:
            triads.append(self.triad(n))
            n = self.next(n)
        return triads

class Diatonic(Scale):
    def build_scale(self, note):
        self._scale_builder([0, 2, 4, 5, 7, 9, 11], note)
