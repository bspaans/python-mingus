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

class Rest(Note):
    def get_notes(self):
        return []

class NoteGrouping(TransposeMixin, CloneMixin, NotesMixin):
    def __init__(self, notes = None):
        self.notes = []
        self.add(notes)

    def _add_notes_if_copyable(self, notes):
        if hasattr(notes, "get_notes") and hasattr(notes, "clone"):
            self.notes.extend(notes.clone().get_notes())

    def add(self, notes):
        if type(notes) == list:
            for n in notes:
                self._add_notes_if_copyable(n)
        self._add_notes_if_copyable(notes)

    def set_transpose(self, amount):
        for n in self.notes:
            n.set_transpose(amount)
        return self

    def get_notes(self):
        return self.notes

class NotesSequence(TransposeMixin, CloneMixin):
    def __init__(self):
        self.sequence = []

    def add(self, notes):
        self.sequence.append(notes)

    def set_transpose(self, amount):
        for notes in self.sequence:
            notes.set_transpose(amount)
        return self
