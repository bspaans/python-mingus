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

def test_Note_from_Note_constructor():
    assert_that(Note(Note('B9')), equal_to(Note('B9')))

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

def test_Note_transpose_up_no_accidentals():
    assert_that(Note('C4').minor_second_up(), equal_to(Note('Db4')))
    assert_that(Note('C4').major_second_up(), equal_to(Note('D4')))
    assert_that(Note('C4').minor_third_up(), equal_to(Note('Eb4')))
    assert_that(Note('C4').major_third_up(), equal_to(Note('E4')))
    assert_that(Note('C4').major_fourth_up(), equal_to(Note('F4')))
    assert_that(Note('C4').minor_fifth_up(), equal_to(Note('Gb4')))
    assert_that(Note('C4').major_fifth_up(), equal_to(Note('G4')))
    assert_that(Note('C4').minor_sixth_up(), equal_to(Note('Ab4')))
    assert_that(Note('C4').major_sixth_up(), equal_to(Note('A4')))
    assert_that(Note('C4').minor_seventh_up(), equal_to(Note('Bb4')))
    assert_that(Note('C4').major_seventh_up(), equal_to(Note('B4')))
    assert_that(Note('C4').octave_up(), equal_to(Note('C5')))

def test_Note_transpose_up_sharp():
    assert_that(Note('C#4').minor_second_up(), equal_to(Note('Db#4')))
    assert_that(Note('C#4').major_second_up(), equal_to(Note('D#4')))
    assert_that(Note('C#4').minor_third_up(), equal_to(Note('Eb#4')))
    assert_that(Note('C#4').major_third_up(), equal_to(Note('E#4')))
    assert_that(Note('C#4').major_fourth_up(), equal_to(Note('F#4')))
    assert_that(Note('C#4').minor_fifth_up(), equal_to(Note('Gb#4')))
    assert_that(Note('C#4').major_fifth_up(), equal_to(Note('G#4')))
    assert_that(Note('C#4').minor_sixth_up(), equal_to(Note('Ab#4')))
    assert_that(Note('C#4').major_sixth_up(), equal_to(Note('A#4')))
    assert_that(Note('C#4').minor_seventh_up(), equal_to(Note('Bb#4')))
    assert_that(Note('C#4').major_seventh_up(), equal_to(Note('B#4')))
    assert_that(Note('C#4').octave_up(), equal_to(Note('C#5')))

def test_Note_transpose_up_flat():
    assert_that(Note('Cb4').minor_second_up(), equal_to(Note('Dbb4')))
    assert_that(Note('Cb4').major_second_up(), equal_to(Note('Db4')))
    assert_that(Note('Cb4').minor_third_up(), equal_to(Note('Ebb4')))
    assert_that(Note('Cb4').major_third_up(), equal_to(Note('Eb4')))
    assert_that(Note('Cb4').major_fourth_up(), equal_to(Note('Fb4')))
    assert_that(Note('Cb4').minor_fifth_up(), equal_to(Note('Gbb4')))
    assert_that(Note('Cb4').major_fifth_up(), equal_to(Note('Gb4')))
    assert_that(Note('Cb4').minor_sixth_up(), equal_to(Note('Abb4')))
    assert_that(Note('Cb4').major_sixth_up(), equal_to(Note('Ab4')))
    assert_that(Note('Cb4').minor_seventh_up(), equal_to(Note('Bbb4')))
    assert_that(Note('Cb4').major_seventh_up(), equal_to(Note('Bb4')))
    assert_that(Note('Cb4').octave_up(), equal_to(Note('Cb5')))

def test_Note_transpose_by_int():
    assert_that(Note('C4').transpose(0), equal_to(Note('C4')))
    assert_that(Note('C4').transpose(1), equal_to(Note('Db4')))
    assert_that(Note('C4').transpose(2), equal_to(Note('D4')))
    assert_that(Note('C4').transpose(3), equal_to(Note('Eb4')))
    assert_that(Note('C4').transpose(4), equal_to(Note('E4')))
    assert_that(Note('C4').transpose(5), equal_to(Note('F4')))
    assert_that(Note('C4').transpose(6), equal_to(Note('Gb4')))
    assert_that(Note('C4').transpose(7), equal_to(Note('G4')))
    assert_that(Note('C4').transpose(8), equal_to(Note('Ab4')))
    assert_that(Note('C4').transpose(9), equal_to(Note('A4')))
    assert_that(Note('C4').transpose(10), equal_to(Note('Bb4')))
    assert_that(Note('C4').transpose(11), equal_to(Note('B4')))
    assert_that(Note('C4').transpose(12), equal_to(Note('C5')))

def test_Note_set_transpose():
    n = Note(60)
    assert_that(n.set_transpose(5), equal_to(Note(65)))
    assert_that(n.set_transpose(-10), equal_to(Note(55)))
    assert_that(n, equal_to(Note(55)))


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
