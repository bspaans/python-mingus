#!/usr/bin/env python

from chords import BaseTransposer

class Scale(object):
    def __init__(self, on_note):
        self.on_note = on_note
        self.scale = set([])
        self.build_scale(on_note)
    def build_scale(self, note):
        pass
    def __contains__(self, item):
        return self.is_in_scale(item)
    def is_in_scale(self, item):
        return (item._base_name, item._accidentals) in self.scale

class Diatonic(Scale):
    def build_scale(self, note):
        b = BaseTransposer([0, 2, 4, 5, 7, 9, 11])
        notes = b.transpose_base(note)
        self.scale = [ (n._base_name, n._accidentals) for n in notes ]
