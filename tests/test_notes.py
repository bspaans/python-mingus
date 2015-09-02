#/usr/bin/env python

from mingus.notes import Note, NoteGrouping, NotesSequence, Rest
from hamcrest import *

def test_Note_int_constructor():
    assert_that(Note(), equal_to(Note(69)))
    assert_that(Note('C0'), equal_to(Note(12)))
    assert_that(Note('C1'), equal_to(Note(24)))
    assert_that(Note('C2'), equal_to(Note(36)))
    assert_that(Note('C3'), equal_to(Note(48)))
    assert_that(Note('C4'), equal_to(Note(60)))
    assert_that(Note('C#4'), equal_to(Note(61)))
    assert_that(Note('D4'), equal_to(Note(62)))
    assert_that(Note('D#4'), equal_to(Note(63)))
    assert_that(Note('E4'), equal_to(Note(64)))
    assert_that(Note('F4'), equal_to(Note(65)))
    assert_that(Note('F#4'), equal_to(Note(66)))
    assert_that(Note('G4'), equal_to(Note(67)))
    assert_that(Note('G#4'), equal_to(Note(68)))
    assert_that(Note('A4'), equal_to(Note(69)))
    assert_that(Note('A#4'), equal_to(Note(70)))
    assert_that(Note('B4'), equal_to(Note(71)))
    assert_that(Note('C5'), equal_to(Note(72)))
    assert_that(Note('C6'), equal_to(Note(84)))
    assert_that(Note('C7'), equal_to(Note(96)))

def test_Note_flat_sharp_difference():
    assert_that(Note('Db4'), not_(equal_to(Note('C#4'))))
    assert_that(Note('Eb4'), not_(equal_to(Note('D#4'))))
    assert_that(Note('Gb4'), not_(equal_to(Note('F#4'))))
    assert_that(Note('Ab4'), not_(equal_to(Note('G#4'))))
    assert_that(Note('Bb4'), not_(equal_to(Note('A#4'))))

def test_Note_flat_enharmonics():
    assert_that(int(Note('Cb4')), equal_to(int(Note('B3'))))
    assert_that(int(Note('C4')), equal_to(int(Note('B#3'))))
    assert_that(int(Note('Db4')), equal_to(int(Note('C#4'))))
    assert_that(int(Note('Eb4')), equal_to(int(Note('D#4'))))
    assert_that(int(Note('Fb4')), equal_to(int(Note('E4'))))
    assert_that(int(Note('F4')), equal_to(int(Note('E#4'))))
    assert_that(int(Note('Gb4')), equal_to(int(Note('F#4'))))
    assert_that(int(Note('Ab4')), equal_to(int(Note('G#4'))))
    assert_that(int(Note('Bb4')), equal_to(int(Note('A#4'))))

def test_Note_get_octave():
    assert_that(Note('C4').get_octave(), equal_to(4))
    assert_that(Note('B4').get_octave(), equal_to(4))
    assert_that(Note('Cb5').get_octave(), equal_to(5))

def test_Note_transpose():
    n = Note('C4')
    assert_that(n.perfect_fourth_up(), equal_to(Note('F4')))
    assert_that(n.perfect_fourth_down(), equal_to(Note('G3')))
    assert_that(n, equal_to(Note('C4')))

    n = Note('C#4')
    assert_that(n.perfect_fourth_up(), equal_to(Note('F#4')))
    assert_that(n.perfect_fourth_down(), equal_to(Note('G#3')))

    n = Note('C##4')
    assert_that(n.perfect_fourth_up(), equal_to(Note('F##4')))
    assert_that(n.perfect_fourth_down(), equal_to(Note('G##3')))

    n = Note('C###4')
    assert_that(n.perfect_fourth_up(), equal_to(Note('F###4')))
    assert_that(n.perfect_fourth_down(), equal_to(Note('G###3')))

    n = Note('Cb4')
    assert_that(n.perfect_fourth_up(), equal_to(Note('Fb4')))
    assert_that(n.perfect_fourth_down(), equal_to(Note('Gb3')))

    n = Note('Cbb4')
    assert_that(n.perfect_fourth_up(), equal_to(Note('Fbb4')))
    assert_that(n.perfect_fourth_down(), equal_to(Note('Gbb3')))

    n = Note('Cbbb4')
    assert_that(n.perfect_fourth_up(), equal_to(Note('Fbbb4')))
    assert_that(n.perfect_fourth_down(), equal_to(Note('Gbbb3')))

def test_Note_set_transpose():
    n = Note(60)
    assert_that(n.set_transpose(5), equal_to(Note(65)))
    assert_that(n.set_transpose(-10), equal_to(Note(55)))
    assert_that(n, equal_to(Note(55)))

def test_NoteGrouping_constructor():
    ng = NoteGrouping()
    assert_that(NoteGrouping().get_notes(), equal_to([]))

    n1 = Note(30)
    assert_that(NoteGrouping(n1).get_notes()[0], equal_to(n1))
    assert_that(NoteGrouping(n1).get_notes()[0], not_(same_instance(n1)))

def test_NoteGrouping_transpose():
    n1 = Note(20)
    n2 = Note(100)
    ng = NoteGrouping([n1, n2])
    assert_that(ng.transpose(5).get_notes()[0], equal_to(Note(25)))
    assert_that(ng.transpose(5).get_notes()[1], equal_to(Note(105)))
    assert_that(ng.transpose(-5).get_notes()[0], equal_to(Note(15)))
    assert_that(ng.transpose(-5).get_notes()[1], equal_to(Note(95)))
    assert_that(n1, equal_to(Note(20)))
    assert_that(n2, equal_to(Note(100)))

def test_NoteGrouping_set_transpose():
    ng = NoteGrouping([20, 'C4'])
    assert_that(ng.set_transpose(5).get_notes()[0], equal_to(Note(25)))
    assert_that(ng.get_notes()[0], equal_to(Note(25)))
    assert_that(ng.get_notes()[1], equal_to(Note(65)))

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
