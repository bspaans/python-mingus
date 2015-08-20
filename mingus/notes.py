#!/usr/bin/env python 

from mixins import TransposeMixin, NotesMixin, CloneMixin, NotesSequenceMixin
import re 

NOTE_MATCHER = re.compile("^(A|B|C|D|E|F|G)([#|b]*)([0-9]*)$")

def _parse_notes(notes):
    if hasattr(notes, "get_notes") and hasattr(notes, "clone"):
        return notes.clone().get_notes()
    elif type(notes) == int:
        return [Note(notes)]
    elif type(notes) == list:
        result = []
        for n in notes:
            result.extend(_parse_notes(n))
        return result
    elif notes is None:
        return []
    raise Exception("Don't know how to parse all these notes: " + str(notes))

class Note(TransposeMixin, NotesMixin, CloneMixin, NotesSequenceMixin):

    def __init__(self, note = None):
        self.note = 69 # A4
        if type(note) == int:
            self.note = note
        elif type(note) == str:
            self.note = self._parse_note(note)

    def _parse_note(self, note):
        note_dict = {
            'C': 0,
            'D': 2,
            'E': 4,
            'F': 5,
            'G': 7,
            'A': 9,
            'B': 11
        }
        m = NOTE_MATCHER.match(note)
        if m is not None:
            name = m.group(1)
            accidentals = m.group(2)
            octave = int(m.group(3))
            base = (octave + 1) * 12
            offset = note_dict[name]
            for a in accidentals:
                if a == '#':
                    offset += 1
                else:
                    offset += -1
            return base + offset

    def set_transpose(self, amount):
        self.note += amount
        return self

    def get_notes(self):
        return [self]


class Rest(Note):
    def get_notes(self):
        return []


class NoteGrouping(TransposeMixin, CloneMixin, NotesMixin, NotesSequenceMixin):
    def __init__(self, notes = None):
        self.notes = []
        self.add(notes)

    def add(self, notes):
        self.notes.extend(_parse_notes(notes))

    def set_transpose(self, amount):
        for n in self.notes:
            n.set_transpose(amount)
        return self

    def get_notes(self):
        return self.notes

class NotesSequence(TransposeMixin, CloneMixin, NotesMixin, NotesSequenceMixin):
    def __init__(self):
        self.sequence = []

    def add(self, notes):
        self.sequence.append(notes)

    def set_transpose(self, amount):
        for notes in self.sequence:
            notes.set_transpose(amount)
        return self

    def get_notes(self):
        result = []
        for notes in self.sequence:
            result.extend(notes.get_notes())
        return result

    def get_notes_sequence(self):
        return self.sequence
