#!/usr/bin/env python 

from mixins import TransposeMixin, NotesMixin, CloneMixin

class Note(TransposeMixin, NotesMixin, CloneMixin):

    def __init__(self, note = None):
        self.note = 0
        if type(note) == int:
            self.note = note

    def set_transpose(self, amount):
        self.note += amount
        return self

    def get_notes(self):
        return [self]

class TiedNote(Note):
    pass

class NoteGrouping(object):
    pass

class NoteSequence(object):
    pass
