#/usr/bin/env python

from mingus.notes import Note, NoteGrouping, NotesSequence, Rest
from hamcrest import *

def test_NoteGrouping_constructor():
    ng = NoteGrouping()
    assert_that(NoteGrouping().get_notes(), equal_to([]))

    n1 = Note(30)
    assert_that(NoteGrouping(n1).get_notes()[0], equal_to(n1))
    assert_that(NoteGrouping(n1).get_notes()[0], not_(same_instance(n1)))

def test_NoteGrouping_transpose():
    n1 = Note('C4')
    n2 = Note('G4')
    ng = NoteGrouping([n1, n2])
    assert_that(ng.transpose(5).get_notes()[0], equal_to(Note('F4')))
    assert_that(ng.perfect_fourth_up().get_notes()[0], equal_to(Note('F4')))
    assert_that(ng.transpose(5).get_notes()[1], equal_to(Note('C5')))
    assert_that(ng.transpose(-5).get_notes()[0], equal_to(Note('G3')))
    assert_that(ng.transpose(-5).get_notes()[1], equal_to(Note('D4')))
    assert_that(n1, equal_to(Note('C4')))
    assert_that(n2, equal_to(Note('G4')))

def test_NoteGrouping_set_transpose():
    ng = NoteGrouping([20, 'C4'])
    assert_that(ng.set_transpose(5).get_notes()[0], equal_to(Note(25)))
    assert_that(ng.get_notes()[0], equal_to(Note(25)))
    assert_that(ng.get_notes()[1], equal_to(Note(65)))

def test_NoteGrouping_notes_are_sorted():
    n1 = Note('G4')
    n2 = Note('C4')
    ng = NoteGrouping([n1, n2])
    assert_that(ng.get_notes()[0], equal_to(n2))
    assert_that(ng.get_notes()[1], equal_to(n1))
    assert_that(ng[0], equal_to(n2))
    assert_that(ng[1], equal_to(n1))
