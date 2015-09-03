#!/usr/bin/env python 

from mixins import TransposeMixin, NotesMixin, CloneMixin, NotesSequenceMixin, CommonEqualityMixin, AugmentDiminishMixin
import re 

_NOTE_MATCHER = re.compile("^(A|B|C|D|E|F|G)([#|b]*)([0-9]*)$")
NOTE_OFFSETS = {
    'C': 0,
    'D': 2,
    'E': 4,
    'F': 5,
    'G': 7,
    'A': 9,
    'B': 11
}
_LOOKUP_SHARPS = {
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
_LOOKUP_FLATS = {
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
  11: ('C', -1),
}

class NotesParser(object):
    @staticmethod
    def parse(notes):
        if hasattr(notes, "get_notes") and hasattr(notes, "clone"):
            return notes.clone().get_notes()
        elif type(notes) == int:
            return [Note(notes)]
        elif type(notes) == str:
            return [Note(notes)]
        elif type(notes) == list:
            result = []
            for n in notes:
                result.extend(NotesParser.parse(n))
            return result
        elif notes is None:
            return []
        raise Exception("Don't know how to parse all these notes: " + str(notes))


class Note(TransposeMixin, NotesMixin, CloneMixin, NotesSequenceMixin, CommonEqualityMixin, AugmentDiminishMixin):

    def __init__(self, note = None):
        self._base_name = 'A'
        self._octave = 4
        self._accidentals = 0
        self._infinite_duration = True
        self._duration = 0
        self._parse_note(note)
        
    def _parse_note(self, note):
        if type(note) == int:
            self.from_int(note)
        elif type(note) == str:
            self.from_string(note)
        elif isinstance(note, Note):
            self.from_note(note)

    def set_change_duration(self, duration):
        self._infinite_duration = False
        self._duration = duration
        return self

    def get_duration(self):
        return self._duration

    # TODO
    def get_duration_in_seconds(self, bpm):
        return 0.0
    # TODO
    def get_duration_in_milliseconds(self, bpm):
        return 0

    def set_base_name(self, name):
        if name not in NOTE_OFFSETS.keys():
            raise Exception, "Not a valid base name: %s" % str(name)
        self._base_name = name

    def set_accidentals(self, accidentals):
        self._accidentals = accidentals

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
        lookup = _LOOKUP_SHARPS if use_sharps else _LOOKUP_FLATS
        self._base_name, self._accidentals = lookup[offset]

    def from_string(self, note):
        m = _NOTE_MATCHER.match(note)
        if m is not None:
            name, accidentals, octave = m.group(1), m.group(2), m.group(3)
            self._base_name = name
            octave = octave if octave.isdigit() else "4"
            self._octave = int(octave)
            self._accidentals = sum(1 if a == '#' else -1 for a in accidentals)
            return
        raise Exception("Unknown note format: " + note)

    def from_note(self, note):
        self._base_name = note._base_name
        self._octave = note._octave
        self._accidentals = note._accidentals

    def __int__(self):
        result = (int(self._octave) + 1) * 12
        result += NOTE_OFFSETS[self._base_name]
        result += self._accidentals
        return result

    def set_transpose(self, amount):
        acc = self._accidentals
        transpose_amount = amount if type(amount) == int else amount.amount
        use_sharps = transpose_amount % 12 in [0, 2, 4, 7, 9, 11]
        self.from_int(int(self) - acc + transpose_amount, use_sharps)
        self._accidentals += acc
        if type(amount) != int:
            amount.update(self)
        return self

    def set_augment(self):
        self._accidentals += 1
        return self

    def set_diminish(self):
        self._accidentals -= 1
        return self

    def get_notes(self):
        return [self]

    def __getitem__(self, key):
        if key == 0:
            return self
        raise "keyerror: trying to get element of a Note. This is not a grouping."


class Rest(Note):
    def get_notes(self):
        return []

class NoteGrouping(TransposeMixin, CloneMixin, NotesMixin, NotesSequenceMixin, AugmentDiminishMixin):
    def __init__(self, notes = None):
        self.notes = []
        self.add(notes)

    def add(self, notes):
        self.notes.extend(NotesParser.parse(notes))
        return self

    def append(self, item):
        return self.add(item)

    def set_transpose(self, amount):
        return self.walk(lambda n: n.set_transpose(amount))

    def set_augment(self):
        return self.walk(lambda n: n.set_augment())

    def set_diminish(self):
        return self.walk(lambda n: n.set_diminish())

    def set_change_duration(self, duration):
        return self.walk(lambda n: n.set_change_duration(duration))

    def get_notes(self):
        return sorted(self.notes, key=int)

    def __getitem__(self, key):
        return self.get_notes()[key]
    def __str__(self): 
        return str(self.get_notes())
    def __repr__(self):
        return "%s <%s>" % (type(self).__name__, str(self))
    def __len__(self):
        return len(self.notes)


class NotesSequence(TransposeMixin, CloneMixin, NotesMixin, NotesSequenceMixin, AugmentDiminishMixin):

    def __init__(self, init_with = None):
        self.sequence = []
        self.add(init_with)

    def add(self, notes):
        if notes is None:
            return self
        elif isinstance(notes, NotesSequence):
            self.sequence.extend(notes.get_notes_sequence())
        elif hasattr(notes, "get_notes") or type(notes) is str:
            self.sequence.append(NoteGrouping(notes))
        elif type(notes) is list:
            for n in notes:
                self.add(n)
        else:
            raise Exception("Unsupported type. This could be a bug in mingus.")
        return self

    def append(self, item):
        return self.add(item)

    def set_transpose(self, amount):
        return self.walk(lambda n: n.set_transpose(amount)) 

    def set_augment(self):
        return self.walk(lambda n: n.set_augment())

    def set_diminish(self):
        return self.walk(lambda n: n.set_diminish())

    def set_change_duration(self, duration):
        return self.walk(lambda n: n.set_change_duration(duration))

    def get_notes(self):
        result = []
        for notes in self.sequence:
            result.extend(notes.get_notes())
        return sorted(result, key=int)

    def get_notes_sequence(self):
        return self.sequence

    def __getitem__(self, key):
        return self.sequence[key]
