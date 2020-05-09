from hamcrest import *
from mingus.notes import Note, NoteGrouping, NotesSequence
from mingus.scales import Diatonic

def _test_transpose_up_sharp(obj_Csharp4):
    assert_that(obj_Csharp4.minor_second_up().get_notes()[0], equal_to(Note('Db#4')))
    assert_that(obj_Csharp4.major_second_up().get_notes()[0], equal_to(Note('D#4')))
    assert_that(obj_Csharp4.minor_third_up().get_notes()[0], equal_to(Note('Eb#4')))
    assert_that(obj_Csharp4.major_third_up().get_notes()[0], equal_to(Note('E#4')))
    assert_that(obj_Csharp4.major_fourth_up().get_notes()[0], equal_to(Note('F#4')))
    assert_that(obj_Csharp4.minor_fifth_up().get_notes()[0], equal_to(Note('Gb#4')))
    assert_that(obj_Csharp4.major_fifth_up().get_notes()[0], equal_to(Note('G#4')))
    assert_that(obj_Csharp4.minor_sixth_up().get_notes()[0], equal_to(Note('Ab#4')))
    assert_that(obj_Csharp4.major_sixth_up().get_notes()[0], equal_to(Note('A#4')))
    assert_that(obj_Csharp4.minor_seventh_up().get_notes()[0], equal_to(Note('Bb#4')))
    assert_that(obj_Csharp4.major_seventh_up().get_notes()[0], equal_to(Note('B#4')))
    assert_that(obj_Csharp4.octave_up().get_notes()[0], equal_to(Note('C#5')))

def _test_transpose_up_flat(obj_Cb4):
    assert_that(obj_Cb4.minor_second_up().get_notes()[0], equal_to(Note('Dbb4')))
    assert_that(obj_Cb4.major_second_up().get_notes()[0], equal_to(Note('Db4')))
    assert_that(obj_Cb4.minor_third_up().get_notes()[0], equal_to(Note('Ebb4')))
    assert_that(obj_Cb4.major_third_up().get_notes()[0], equal_to(Note('Eb4')))
    assert_that(obj_Cb4.major_fourth_up().get_notes()[0], equal_to(Note('Fb4')))
    assert_that(obj_Cb4.minor_fifth_up().get_notes()[0], equal_to(Note('Gbb4')))
    assert_that(obj_Cb4.major_fifth_up().get_notes()[0], equal_to(Note('Gb4')))
    assert_that(obj_Cb4.minor_sixth_up().get_notes()[0], equal_to(Note('Abb4')))
    assert_that(obj_Cb4.major_sixth_up().get_notes()[0], equal_to(Note('Ab4')))
    assert_that(obj_Cb4.minor_seventh_up().get_notes()[0], equal_to(Note('Bbb4')))
    assert_that(obj_Cb4.major_seventh_up().get_notes()[0], equal_to(Note('Bb4')))
    assert_that(obj_Cb4.octave_up().get_notes()[0], equal_to(Note('Cb5')))

def _test_transpose_by_int(obj_C4):
    assert_that(obj_C4.transpose(0).get_notes()[0], equal_to(Note('C4')))
    assert_that(obj_C4.transpose(1).get_notes()[0], equal_to(Note('Db4')))
    assert_that(obj_C4.transpose(2).get_notes()[0], equal_to(Note('D4')))
    assert_that(obj_C4.transpose(3).get_notes()[0], equal_to(Note('Eb4')))
    assert_that(obj_C4.transpose(4).get_notes()[0], equal_to(Note('E4')))
    assert_that(obj_C4.transpose(5).get_notes()[0], equal_to(Note('F4')))
    assert_that(obj_C4.transpose(6).get_notes()[0], equal_to(Note('Gb4')))
    assert_that(obj_C4.transpose(7).get_notes()[0], equal_to(Note('G4')))
    assert_that(obj_C4.transpose(8).get_notes()[0], equal_to(Note('Ab4')))
    assert_that(obj_C4.transpose(9).get_notes()[0], equal_to(Note('A4')))
    assert_that(obj_C4.transpose(10).get_notes()[0], equal_to(Note('Bb4')))
    assert_that(obj_C4.transpose(11).get_notes()[0], equal_to(Note('B4')))
    assert_that(obj_C4.transpose(12).get_notes()[0], equal_to(Note('C5')))

def _test_transpose_up_no_accidentals(obj_C4):
    assert_that(obj_C4.minor_second_up().get_notes()[0], equal_to(Note('Db4')))
    assert_that(obj_C4.major_second_up().get_notes()[0], equal_to(Note('D4')))
    assert_that(obj_C4.minor_third_up().get_notes()[0], equal_to(Note('Eb4')))
    assert_that(obj_C4.major_third_up().get_notes()[0], equal_to(Note('E4')))
    assert_that(obj_C4.major_fourth_up().get_notes()[0], equal_to(Note('F4')))
    assert_that(obj_C4.minor_fifth_up().get_notes()[0], equal_to(Note('Gb4')))
    assert_that(obj_C4.major_fifth_up().get_notes()[0], equal_to(Note('G4')))
    assert_that(obj_C4.minor_sixth_up().get_notes()[0], equal_to(Note('Ab4')))
    assert_that(obj_C4.major_sixth_up().get_notes()[0], equal_to(Note('A4')))
    assert_that(obj_C4.minor_seventh_up().get_notes()[0], equal_to(Note('Bb4')))
    assert_that(obj_C4.major_seventh_up().get_notes()[0], equal_to(Note('B4')))
    assert_that(obj_C4.octave_up().get_notes()[0], equal_to(Note('C5')))


def _test_transpose_mixin_contract(obj_C4, obj_Cb4, obj_Csharp4):
    _test_transpose_up_flat(obj_Cb4)
    _test_transpose_up_sharp(obj_Csharp4)
    _test_transpose_by_int(obj_C4)
    _test_transpose_up_no_accidentals(obj_C4)

def test_Note_transpose_mixin():
    obj_C4 = Note('C4')
    obj_Cb4 = Note('Cb4')
    obj_Csharp4 = Note('C#4')
    _test_transpose_mixin_contract(obj_C4, obj_Cb4, obj_Csharp4)

def test_NoteGrouping_transpose_mixin():
    obj_C4 = NoteGrouping('C4')
    obj_Cb4 = NoteGrouping('Cb4')
    obj_Csharp4 = NoteGrouping('C#4')
    _test_transpose_mixin_contract(obj_C4, obj_Cb4, obj_Csharp4)

def test_NoteSequence_transpose_mixin():
    obj_C4 = NotesSequence('C4')
    obj_Cb4 = NotesSequence('Cb4')
    obj_Csharp4 = NotesSequence('C#4')
    _test_transpose_mixin_contract(obj_C4, obj_Cb4, obj_Csharp4)

def test_Diatonic_tranpose_mixin():
    obj_C4 = Diatonic('C4')
    obj_Cb4 = Diatonic('Cb4')
    obj_Csharp4 = Diatonic('C#4')
    _test_transpose_mixin_contract(obj_C4, obj_Cb4, obj_Csharp4)

