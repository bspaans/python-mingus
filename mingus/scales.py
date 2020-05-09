#!/usr/bin/env python

from .notes import Note, NoteGrouping
from .mixins import StepMixin, NotesMixin, CloneMixin, TransposeMixin, Aug, Dim

class Scale(StepMixin, NotesMixin, CloneMixin, TransposeMixin):

    def __init__(self, on_note):
        self.on_note = Note(on_note)
        self._scale = set([])
        self.build_scale(self.on_note)

    def get_base_note(self):
        return self.on_note

    def _notes_to_scale_representation(self, intervals, base_note):
        notes = base_note.transpose_list(intervals)
        self._scale = [ (n.get_base_name(), n.get_accidentals()) for n in notes ]

    def __contains__(self, item):
        return self.is_in_scale(item)

    def _get_note_index_in_scale(self, note):
        if note in self:
            lookup = (note.get_base_name(), note.get_accidentals())
            return self._scale.index(lookup)

        # this is a best guess that fails when the base name 
        # of the note is not in the scale at all.
        # have to decide what to do in that case...
        for ix, n in enumerate(self._scale):
            if n[0] == note.get_base_name():
                return ix
        raise Exception("Next note not found. This is a bug and should be raised")

    def _note_from_scale_representation(self, scale_note):
        new_note = Note(self.on_note)
        new_note.set_base_name(scale_note[0])
        new_note.set_accidentals(scale_note[1])
        return new_note

    def next(self, note, step = 1):
        if step > len(self._scale):
            raise Exception("Unsupported step size")
        note = Note(note)
        index = self._get_note_index_in_scale(note)
        next_ix = (index + step) % (len(self._scale))
        next_note = self._scale[next_ix]
        new_note = self._note_from_scale_representation(next_note)
        while int(new_note) < int(note):
            new_note.set_octave_up()
        return new_note

    def triad(self, note):
        note = Note(note)
        third = self.third_up(note)
        fifth = self.fifth_up(note)
        return NoteGrouping([note, third, fifth])

    def seventh(self, note):
        note = Note(note)
        third = self.third_up(note)
        fifth = self.fifth_up(note)
        seventh = self.seventh_up(note)
        return NoteGrouping([note, third, fifth, seventh])

    def walk_octave(self, func):
        n = self.on_note
        result = []
        while int(n) - int(self.on_note) < 12:
            result.append(func(n))
            n = self.next(n)
        return result

    def triads(self):
        return self.walk_octave(lambda n: self.triad(n))

    def sevenths(self):
        return self.walk_octave(lambda n: self.seventh(n))

    def get_notes(self):
        return self.walk_octave(lambda n: n)

    def get_notes_sequence(self):
        return self.walk_octave(lambda n: [n])

    def set_change_duration(self, duration):
        self.on_note.set_change_duration(duration)
        return self

    def set_transpose(self, amount):
        self.on_note.set_transpose(amount)
        self.build_scale(self.on_note)
        return self

    def __str__(self): 
        return str(self.get_notes())

    def __repr__(self):
        return "%s scale <%s>" % (type(self).__name__, str(self))

    def is_in_scale(self, item):
        return (item.get_base_name(), item.get_accidentals()) in self._scale

    def build_scale(self, note):
        self._notes_to_scale_representation([0], note)


class Diatonic(Scale):
    def build_scale(self, note):
        self._notes_to_scale_representation([0, 2, 4, 5, 7, 9, 11], note)

class Ionian(Diatonic):
    pass

class Dorian(Scale):
    def build_scale(self, note):
        self._notes_to_scale_representation([0, 2, 3, 5, 7, 9, 10], note)

class Phrygian(Scale):
    def build_scale(self, note):
        self._notes_to_scale_representation([0, 1, 3, 5, 7, 8, 10], note)

class Lydian(Scale):
    def build_scale(self, note):
        self._notes_to_scale_representation([0, 2, 4, Aug(5), 7, 9, 11], note)

class Mixolydian(Scale):
    def build_scale(self, note):
        self._notes_to_scale_representation([0, 2, 4, 5, 7, 9, 10], note)

class Aeolian(Scale):
    def build_scale(self, note):
        self._notes_to_scale_representation([0, 2, 3, 5, 7, 8, 10], note)

class Locrian(Scale):
    def build_scale(self, note):
        self._notes_to_scale_representation([0, 1, 3, 5, 6, 8, 10], note)
