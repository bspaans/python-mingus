#!/usr/bin/env python 

import copy

class TransposeMixin(object):
    def set_transpose(self, amount):
        return self
    def transpose(self, amount):
        return self.clone().set_transpose(amount)
    def set_octave_up(self):
        return self.set_transpose(12)
    def octave_up(self):
        return self.transpose(12)
    def set_octave_down(self):
        return self.set_transpose(-12)
    def octave_down(self):
        return self.transpose(-12)

class NotesMixin(object):
    def get_notes(self):
        return []

class CloneMixin(object):
    def clone(self):
        return copy.deepcopy(self)
