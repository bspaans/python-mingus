#!/usr/bin/env python 

from mixins import TransposeMixin, NotesMixin, CloneMixin, NotesSequenceMixin, CommonEqualityMixin
import re 

NOTE_MATCHER = re.compile("^(A|B|C|D|E|F|G)([#|b]*)([0-9]*)$")
NOTE_OFFSETS = {
    'C': 0,
    'D': 2,
    'E': 4,
    'F': 5,
    'G': 7,
    'A': 9,
    'B': 11
}
LOOKUP_SHARPS = {
  0: ('C', 0),
  1: ('C', 1),
  2: ('D', 0),
  3: ('D', 1),
  4: ('E', 0),
  5: ('F', 0),
  6: ('F', 1),
  7: ('G', 0),
  8: ('G', 1),
  9: ('A', 0),
  10: ('A', 1),
  11: ('B', 0),
}
LOOKUP_FLATS = {
  0: ('C', 0),
  1: ('D', -1),
  2: ('D', 0),
  3: ('E', -1),
  4: ('E', 0),
  5: ('F', 0),
  6: ('G', -1),
  7: ('G', 0),
  8: ('A', -1),
  9: ('A', 0),
  10: ('B', -1),
  11: ('B', 0),
}

def _parse_notes(notes):
    if hasattr(notes, "get_notes") and hasattr(notes, "clone"):
        return notes.clone().get_notes()
    elif type(notes) == int:
        return [Note(notes)]
    elif type(notes) == str:
        return [Note(notes)]
    elif type(notes) == list:
        result = []
        for n in notes:
            result.extend(_parse_notes(n))
        return result
    elif notes is None:
        return []
    raise Exception("Don't know how to parse all these notes: " + str(notes))

class Note(TransposeMixin, NotesMixin, CloneMixin, NotesSequenceMixin, CommonEqualityMixin):

    def __init__(self, note = None):
        self._base_name = 'A'
        self._octave = 4
        self._accidentals = 0
        if type(note) == int:
            self.from_int(note)
        elif type(note) == str:
            self.from_string(note)

    def get_base_name(self):
        return self._base_name
    def get_accidentals(self):
        return self._accidentals
    def get_accidentals_as_string(self):
        return ('#' if self._accidentals > 0 else 'b') * abs(self._accidentals)
    def get_octave(self):
        return self._octave

    def __str__(self):
        accidentals = self.get_accidentals_as_string()
        return "%s%s%d" % (self._base_name, accidentals, self._octave)
    def __repr__(self):
        return str(self)

    def from_int(self, i, use_sharps = True):
        self._octave = (i / 12) - 1
        offset = i - (self._octave + 1) * 12
        lookup = LOOKUP_SHARPS if use_sharps else LOOKUP_FLATS
        self._base_name, self._accidentals = lookup[offset]

    def from_string(self, note):
        m = NOTE_MATCHER.match(note)
        if m is not None:
            name, accidentals, octave = m.group(1), m.group(2), m.group(3)
            self._base_name = name
            self._octave = int(octave)
            self._accidentals = sum(1 if a == '#' else -1 for a in accidentals)
            return
        raise Exception("Unknown note format: " + note)

    def __int__(self):
        result = (int(self._octave) + 1) * 12
        result += NOTE_OFFSETS[self._base_name]
        result += self._accidentals
        return result

    def set_transpose(self, amount):
        acc = self._accidentals
        self.from_int(int(self) - acc + amount)
        self._accidentals = acc
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
        self.walk(lambda n: n.set_transpose(amount))
        return self

    def get_notes(self):
        return self.notes

class NotesSequence(TransposeMixin, CloneMixin, NotesMixin, NotesSequenceMixin):
    def __init__(self):
        self.sequence = []

    def add(self, notes):
        self.sequence.append(notes)

    def set_transpose(self, amount):
        self.walk(lambda n: n.set_transpose(amount))
        return self

    def get_notes(self):
        result = []
        for notes in self.sequence:
            result.extend(notes.get_notes())
        return result

    def get_notes_sequence(self):
        return self.sequence
