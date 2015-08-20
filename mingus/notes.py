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

class NoteGrouping(TransposeMixin, CloneMixin, NotesMixin):
    def __init__(self, notes = None):
        self.notes = []
        if type(notes) == list:
            self.notes = notes

    def set_transpose(self, amount):
        for n in self.notes:
            n.set_transpose(amount)
        return self

    def get_notes(self):
        return self.notes

class NoteSequence(object):
    pass
