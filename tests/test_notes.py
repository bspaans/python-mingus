#!/usr/bin/env python

from mingus.notes import Note, NoteGrouping, NotesSequence, Rest
from hamcrest import *

def test_Note_constructor():
    assert_that(Note().note, equal_to(69))
    assert_that(Note('C4').note, equal_to(60))
    assert_that(Note('C#4').note, equal_to(61))
    assert_that(Note('Db4').note, equal_to(61))
    assert_that(Note('D4').note, equal_to(62))
    assert_that(Note('D#4').note, equal_to(63))
    assert_that(Note('Eb4').note, equal_to(63))
    assert_that(Note('E4').note, equal_to(64))
    assert_that(Note('F4').note, equal_to(65))
    assert_that(Note('F#4').note, equal_to(66))
    assert_that(Note('Gb4').note, equal_to(66))
    assert_that(Note('G4').note, equal_to(67))
    assert_that(Note('G#4').note, equal_to(68))
    assert_that(Note('Ab4').note, equal_to(68))
    assert_that(Note('A4').note, equal_to(69))
    assert_that(Note('A#4').note, equal_to(70))
    assert_that(Note('Bb4').note, equal_to(70))
    assert_that(Note('B4').note, equal_to(71))
    assert_that(Note('C5').note, equal_to(72))

def test_Note_transpose():
    n = Note(60)
    assert_that(n.perfect_fourth_up().note, equal_to(65))
    assert_that(n.perfect_fourth_down().note, equal_to(55))
    assert_that(n.note, equal_to(60))

def test_Note_set_transpose():
    n = Note(60)
    assert_that(n.set_transpose(5).note, equal_to(65))
    assert_that(n.set_transpose(-10).note, equal_to(55))
    assert_that(n.note, equal_to(55))

def test_NoteGrouping_constructor():
    ng = NoteGrouping()
    assert_that(NoteGrouping().get_notes(), equal_to([]))

    n1 = Note(30)
    assert_that(NoteGrouping(n1).get_notes()[0].note, equal_to(n1.note))
    assert_that(NoteGrouping(n1).get_notes()[0], not_(same_instance(n1)))

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
    ng = NoteGrouping([20, 100])
    assert_that(ng.set_transpose(5).get_notes()[0].note, equal_to(25))
    assert_that(ng.get_notes()[0].note, equal_to(25))
    assert_that(ng.get_notes()[1].note, equal_to(105))

def test_NotesSequence_transpose():
    n1 = Note(20)
    n2 = Note(100)
    ng = NoteGrouping([40])
    r = Rest()
    ns = NotesSequence()
    ns.add(n1)
    ns.add(n2)
    ns.add(ng)
    ns.add(r)
    assert_that(ns.transpose(5).sequence[0].get_notes()[0].note, equal_to(25))
    assert_that(ns.transpose(5).sequence[2].get_notes()[0].note, equal_to(45))
    assert_that(n1.note, equal_to(20))

def test_NotesSequence_set_transpose():
    n1 = Note(20)
    n2 = Note(100)
    ng = NoteGrouping([40])
    r = Rest()
    ns = NotesSequence()
    ns.add(n1)
    ns.add(n2)
    ns.add(ng)
    ns.add(r)
    assert_that(ns.set_transpose(5).sequence[0].get_notes()[0].note, equal_to(25))
    assert_that(ns.sequence[2].get_notes()[0].note, equal_to(45))
