from mingus.notes import NotesSequence, Note, NoteGrouping, Rest
from hamcrest import *


def test_NotesSequence_constructor_from_None():
    seq = NotesSequence()
    assert_that(seq.get_notes_sequence(), equal_to([]))


def test_NotesSequence_constructor_from_string():
    seq = NotesSequence("C4")
    assert_that(seq.get_notes_sequence()[0][0], equal_to(Note("C4")))


def test_NotesSequence_constructor_from_Note():
    seq = NotesSequence(Note("C4"))
    assert_that(seq.get_notes_sequence()[0][0], equal_to(Note("C4")))


def test_NotesSequence_constructor_from_NoteGrouping():
    seq = NotesSequence(NoteGrouping(Note("C4")))
    assert_that(seq.get_notes_sequence()[0][0], equal_to(Note("C4")))


def test_NotesSequence_constructor_from_list():
    seq = NotesSequence(["C4", Note("G4"), NoteGrouping(Note("C5"))])
    assert_that(seq.get_notes_sequence()[0][0], equal_to(Note("C4")))
    assert_that(seq.get_notes_sequence()[1][0], equal_to(Note("G4")))
    assert_that(seq.get_notes_sequence()[2][0], equal_to(Note("C5")))


def test_NotesSequence_durations():
    n1 = Note("C4").set_change_duration(8)
    n2 = Note("E4").set_change_duration(8)

    ns = NotesSequence()
    ns.add(Note("C4"))
    ns.add([Note("E4"), Note("C4")])
    ns.set_change_duration(8)

    assert_that(ns[0][0], equal_to(n1))
    assert_that(ns[1][0], equal_to(n2))
    assert_that(ns[2][0], equal_to(n1))


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
    assert_that(ns.transpose(5).sequence[0].get_notes()[0], equal_to(Note(25)))
    assert_that(ns.transpose(5).sequence[2].get_notes()[0], equal_to(Note(45)))
    assert_that(n1, equal_to(Note(20)))


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
    assert_that(ns.set_transpose(5).sequence[0].get_notes()[0], equal_to(Note(25)))
    assert_that(ns.sequence[2].get_notes()[0], equal_to(Note(45)))
