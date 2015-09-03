#!/usr/bin/env python 

from mingus.notes import NotesSequence, Note, NoteGrouping
from hamcrest import *

def test_NotesSequence_constructor_from_None():
    seq = NotesSequence()
    assert_that(seq.get_notes_sequence(), equal_to([]))

def test_NotesSequence_constructor_from_string():
    seq = NotesSequence('C4')
    assert_that(seq.get_notes_sequence()[0][0], equal_to(Note('C4')))

def test_NotesSequence_constructor_from_Note():
    seq = NotesSequence(Note('C4'))
    assert_that(seq.get_notes_sequence()[0][0], equal_to(Note('C4')))

def test_NotesSequence_constructor_from_NoteGrouping():
    seq = NotesSequence(NoteGrouping(Note('C4')))
    assert_that(seq.get_notes_sequence()[0][0], equal_to(Note('C4')))

def test_NotesSequence_constructor_from_list():
    seq = NotesSequence(['C4', Note('G4'), NoteGrouping(Note('C5'))])
    assert_that(seq.get_notes_sequence()[0][0], equal_to(Note('C4')))
    assert_that(seq.get_notes_sequence()[1][0], equal_to(Note('G4')))
    assert_that(seq.get_notes_sequence()[2][0], equal_to(Note('C5')))


def test_NotesSequence_durations():
    n1 = Note('C4').set_change_duration(8)
    n2 = Note('E4').set_change_duration(8)

    ns = NotesSequence()
    ns.add(Note('C4'))
    ns.add([Note('E4'), Note('C4')])
    ns.set_change_duration(8)

    assert_that(ns[0][0], equal_to(n1))
    assert_that(ns[1][0], equal_to(n2))
    assert_that(ns[2][0], equal_to(n1))
