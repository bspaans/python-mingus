#!/usr/bin/env python


from mingus.notes import Note, TiedNote, NoteGrouping, NoteSequence
from hamcrest import *

def test_Note_transpose():
    n = Note(60)
    assert_that(n.transpose(5).note, equal_to(65))
    assert_that(n.transpose(-5).note, equal_to(55))
    assert_that(n.note, equal_to(60))

def test_Note_set_transpose():
    n = Note(60)
    assert_that(n.set_transpose(5).note, equal_to(65))
    assert_that(n.set_transpose(-10).note, equal_to(55))
    assert_that(n.note, equal_to(55))


def test_NoteGrouping_transpose():
    n1 = Note(20)
    n2 = Note(100)
    ng = NoteGrouping([n1, n2])
    assert_that(ng.transpose(5).get_notes()[0].note, equal_to(25))
    assert_that(ng.transpose(5).get_notes()[1].note, equal_to(105))
    assert_that(ng.transpose(-5).get_notes()[0].note, equal_to(15))
    assert_that(ng.transpose(-5).get_notes()[1].note, equal_to(95))
    assert_that(n1.note, equal_to(20))
    assert_that(n2.note, equal_to(100))

def test_NoteGrouping_set_transpose():
    n1 = Note(20)
    n2 = Note(100)
    ng = NoteGrouping([n1, n2])
    assert_that(ng.set_transpose(5).get_notes()[0].note, equal_to(25))
    assert_that(ng.get_notes()[1].note, equal_to(105))
    assert_that(n1.note, equal_to(25))
    assert_that(n2.note, equal_to(105))
