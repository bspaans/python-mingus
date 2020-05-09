from mingus.progressions import Progression
from mingus.notes import Note
from .common import _chord_tester
from hamcrest import *

def test_Progression_constructor_from_None():
    prog = Progression()
    assert_that(prog.get_scale().get_base_note(), equal_to(Note('C4')))

def test_Progression_constructor_from_string_with_octave():
    prog = Progression('A5')
    assert_that(prog.get_scale().get_base_note(), equal_to(Note('A5')))

def test_Progression_constructor_from_string_without_octave():
    prog = Progression('A')
    assert_that(prog.get_scale().get_base_note(), equal_to(Note('A4')))

def test_Progression_constructor_from_note():
    prog = Progression(Note('A5'))
    assert_that(prog.get_scale().get_base_note(), equal_to(Note('A5')))


def test_Progression_triads():
    prog = Progression()
    _chord_tester(prog.first(), ['C4', 'E4', 'G4'])
    _chord_tester(prog.second(), ['D4', 'F4', 'A4'])
    _chord_tester(prog.third(), ['E4', 'G4', 'B4'])
    _chord_tester(prog.fourth(), ['F4', 'A4', 'C5'])
    _chord_tester(prog.fifth(), ['G4', 'B4', 'D5'])
    _chord_tester(prog.sixth(), ['A4', 'C5', 'E5'])
    _chord_tester(prog.seventh(), ['B4', 'D5', 'F5'])

def test_Progression_triads_roman_numerals():
    prog = Progression()
    _chord_tester(prog.I(), ['C4', 'E4', 'G4'])
    _chord_tester(prog.II(), ['D4', 'F4', 'A4'])
    _chord_tester(prog.III(), ['E4', 'G4', 'B4'])
    _chord_tester(prog.IV(), ['F4', 'A4', 'C5'])
    _chord_tester(prog.V(), ['G4', 'B4', 'D5'])
    _chord_tester(prog.VI(), ['A4', 'C5', 'E5'])
    _chord_tester(prog.VII(), ['B4', 'D5', 'F5'])

def test_Progression_triads_from_string():
    prog = Progression()
    _chord_tester(prog.from_string('I'), ['C4', 'E4', 'G4'])
    _chord_tester(prog.from_string('II'), ['D4', 'F4', 'A4'])
    _chord_tester(prog.from_string('III'), ['E4', 'G4', 'B4'])
    _chord_tester(prog.from_string('IV'), ['F4', 'A4', 'C5'])
    _chord_tester(prog.from_string('V'), ['G4', 'B4', 'D5'])
    _chord_tester(prog.from_string('VI'), ['A4', 'C5', 'E5'])
    _chord_tester(prog.from_string('VII'), ['B4', 'D5', 'F5'])

def test_Progression_sevenths():
    prog = Progression()
    _chord_tester(prog.first_seventh(), ['C4', 'E4', 'G4', 'B4'])
    _chord_tester(prog.second_seventh(), ['D4', 'F4', 'A4', 'C5'])
    _chord_tester(prog.third_seventh(), ['E4', 'G4', 'B4', 'D5'])
    _chord_tester(prog.fourth_seventh(), ['F4', 'A4', 'C5', 'E5'])
    _chord_tester(prog.fifth_seventh(), ['G4', 'B4', 'D5', 'F5'])
    _chord_tester(prog.sixth_seventh(), ['A4', 'C5', 'E5', 'G5'])
    _chord_tester(prog.seventh_seventh(), ['B4', 'D5', 'F5', 'A5'])

def test_Progression_sevenths_roman_numerals():
    prog = Progression()
    _chord_tester(prog.I7(), ['C4', 'E4', 'G4', 'B4'])
    _chord_tester(prog.II7(), ['D4', 'F4', 'A4', 'C5'])
    _chord_tester(prog.III7(), ['E4', 'G4', 'B4', 'D5'])
    _chord_tester(prog.IV7(), ['F4', 'A4', 'C5', 'E5'])
    _chord_tester(prog.V7(), ['G4', 'B4', 'D5', 'F5'])
    _chord_tester(prog.VI7(), ['A4', 'C5', 'E5', 'G5'])
    _chord_tester(prog.VII7(), ['B4', 'D5', 'F5', 'A5'])

def test_Progression_sevenths_from_string():
    prog = Progression()
    _chord_tester(prog.from_string('I7'), ['C4', 'E4', 'G4', 'B4'])
    _chord_tester(prog.from_string('II7'), ['D4', 'F4', 'A4', 'C5'])
    _chord_tester(prog.from_string('III7'), ['E4', 'G4', 'B4', 'D5'])
    _chord_tester(prog.from_string('IV7'), ['F4', 'A4', 'C5', 'E5'])
    _chord_tester(prog.from_string('V7'), ['G4', 'B4', 'D5', 'F5'])
    _chord_tester(prog.from_string('VI7'), ['A4', 'C5', 'E5', 'G5'])
    _chord_tester(prog.from_string('VII7'), ['B4', 'D5', 'F5', 'A5'])

def test_Progression_other_chords_from_string():
    prog = Progression()
    _chord_tester(prog.from_string('Im7'), ['C4', 'Eb4', 'G4', 'Bb4'])
    _chord_tester(prog.from_string('Idom7'), ['C4', 'E4', 'G4', 'Bb4'])
    _chord_tester(prog.from_string('II9'), ['D4', 'F#4', 'A4', 'C5', 'E5'])

def test_Progression_call_is_from_string():
    prog = Progression()
    _chord_tester(prog('I'), ['C4', 'E4', 'G4'])
    _chord_tester(prog('II'), ['D4', 'F4', 'A4'])
    _chord_tester(prog('III'), ['E4', 'G4', 'B4'])
    _chord_tester(prog('IV'), ['F4', 'A4', 'C5'])
    _chord_tester(prog('V'), ['G4', 'B4', 'D5'])
    _chord_tester(prog('VI'), ['A4', 'C5', 'E5'])
    _chord_tester(prog('VII'), ['B4', 'D5', 'F5'])

def test_Progression_from_string_list():
    prog = Progression()
    chords = prog.from_string_list(["Im7", "V7"])
    _chord_tester(chords[0], ['C4', 'Eb4', 'G4', 'Bb4'])
    _chord_tester(chords[1], ['G4', 'B4', 'D5', 'F5'])

def test_Progression_from_string_list_returns_NotesSequence():
    prog = Progression()
    chords = prog.from_string_list(["Im7", "V7"])
    chords.set_perfect_fifth_up()
    _chord_tester(chords[0], ['G4', 'Bb4', 'D5', 'F5'])
    _chord_tester(chords[1], ['D5', 'F#5', 'A5', 'C6'])
