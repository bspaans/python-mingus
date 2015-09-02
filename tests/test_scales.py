#!/usr/bin/env python

from mingus.scales import Diatonic
from mingus.notes import Note
from hamcrest import *

NOTES_SET = set(['C4', 'C#4', 'Db4', 'D4', 'D#4',
    'Eb4', 'E4', 'E#4', 'Fb4', 'F#4',
    'Gb4', 'G4', 'G#4', 'Ab4', 'A4',
    'A#4', 'Bb4', 'B4', 'B#4', 'Cb5', 
    'C5'])

def _scale_tester(scale, notes_in_scale):
    for s in notes_in_scale:
        assert_that(Note(s) in scale, 
        "Note %s should be part of this scale" % s)
    for s in NOTES_SET - set(notes_in_scale):
        assert_that(Note(s) not in scale, 
        "Note %s should not be part of this scale" % s)

def test_Diatonic_on_C4():
    scale = Diatonic(Note('C4'))
    in_scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'C6', 'C0']
    _scale_tester(scale, in_scale)

def test_Diatonic_on_F4():
    scale = Diatonic(Note('F4'))
    in_scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'Bb4', 'C5', 'C6', 'C0']
    _scale_tester(scale, in_scale)

def test_Diatonic_on_Bb4():
    scale = Diatonic(Note('Bb4'))
    in_scale = ['C4', 'D4', 'Eb4', 'F4', 'G4', 'A4', 'Bb4', 'C5', 'C6', 'C0']
    _scale_tester(scale, in_scale)

def test_Diatonic_on_Eb4():
    scale = Diatonic(Note('Eb4'))
    in_scale = ['C4', 'D4', 'Eb4', 'F4', 'G4', 'Ab4', 'Bb4', 'C5', 'C6', 'C0']
    _scale_tester(scale, in_scale)

def test_Diatonic_on_Ab4():
    scale = Diatonic(Note('Ab4'))
    in_scale = ['C4', 'Db4', 'Eb4', 'F4', 'G4', 'Ab4', 'Bb4', 'C5', 'C6', 'C0']
    _scale_tester(scale, in_scale)

def test_Diatonic_on_Db4():
    scale = Diatonic(Note('Db4'))
    in_scale = ['C4', 'Db4', 'Eb4', 'F4', 'Gb4', 'Ab4', 'Bb4', 'C5', 'C6', 'C0']
    _scale_tester(scale, in_scale)
    
def test_Diatonic_on_Gb4():
    scale = Diatonic(Note('Gb4'))
    in_scale = ['Cb4', 'Db4', 'Eb4', 'F4', 'Gb4', 'Ab4', 'Bb4', 'Cb5', 'Cb6', 'Cb0']
    _scale_tester(scale, in_scale)

def test_Diatonic_on_G4():
    scale = Diatonic(Note('G4'))
    in_scale = ['C4', 'D4', 'E4', 'F#4', 'G4', 'A4', 'B4', 'C5', 'C6', 'C0']
    _scale_tester(scale, in_scale)

def test_Diatonic_on_D4():
    scale = Diatonic(Note('D4'))
    in_scale = ['C#4', 'D4', 'E4', 'F#4', 'G4', 'A4', 'B4', 'C#5', 'C#6', 'C#0']
    _scale_tester(scale, in_scale)

def test_Diatonic_on_A4():
    scale = Diatonic(Note('A4'))
    in_scale = ['C#4', 'D4', 'E4', 'F#4', 'G#4', 'A4', 'B4', 'C#5', 'C#6', 'C#0']
    _scale_tester(scale, in_scale)

def test_Diatonic_on_E4():
    scale = Diatonic(Note('E4'))
    in_scale = ['C#4', 'D#4', 'E4', 'F#4', 'G#4', 'A4', 'B4', 'C#5', 'C#6', 'C#0']
    _scale_tester(scale, in_scale)

def test_Diatonic_on_B4():
    scale = Diatonic(Note('B4'))
    in_scale = ['C#4', 'D#4', 'E4', 'F#4', 'G#4', 'A#4', 'B4', 'C#5', 'C#6', 'C#0']
    _scale_tester(scale, in_scale)

def test_Diatonic_on_Fsharp4():
    scale = Diatonic(Note('F#4'))
    in_scale = ['C#4', 'D#4', 'E#4', 'F#4', 'G#4', 'A#4', 'B4', 'C#5', 'C#6', 'C#0']
    _scale_tester(scale, in_scale)

def test_Diatonic_next():
    scale = Diatonic(Note('C4'))
    assert_that(scale.next(Note('C5')), equal_to(Note('D5')))
    assert_that(scale.next(Note('D5')), equal_to(Note('E5')))
    assert_that(scale.next(Note('E5')), equal_to(Note('F5')))
    assert_that(scale.next(Note('F5')), equal_to(Note('G5')))
    assert_that(scale.next(Note('G5')), equal_to(Note('A5')))
    assert_that(scale.next(Note('A5')), equal_to(Note('B5')))
    assert_that(scale.next(Note('B5')), equal_to(Note('C6')))
    assert_that(scale.next(Note('G#5')), equal_to(Note('A5')))

def _chord_tester(triad, notes):
    for ix, note in enumerate(notes):
        assert_that(triad[ix], equal_to(Note(note)),
            "Note %d of %s should be %s" % (ix, str(triad), note))

def test_Diatonic_triad():
    scale = Diatonic(Note('C4'))
    _chord_tester(scale.triad('C4'), ['C4', 'E4', 'G4'])
    _chord_tester(scale.triad('D4'), ['D4', 'F4', 'A4'])
    _chord_tester(scale.triad('E4'), ['E4', 'G4', 'B4'])
    _chord_tester(scale.triad('F4'), ['F4', 'A4', 'C5'])
    _chord_tester(scale.triad('G4'), ['G4', 'B4', 'D5'])
    _chord_tester(scale.triad('A4'), ['A4', 'C5', 'E5'])
    _chord_tester(scale.triad('B4'), ['B4', 'D5', 'F5'])

def test_Diatonic_triads():
    scale = Diatonic(Note('C4'))
    triads = scale.triads()
    _chord_tester(triads[0], ['C4', 'E4', 'G4'])
    _chord_tester(triads[1], ['D4', 'F4', 'A4'])
    _chord_tester(triads[2], ['E4', 'G4', 'B4'])
    _chord_tester(triads[3], ['F4', 'A4', 'C5'])
    _chord_tester(triads[4], ['G4', 'B4', 'D5'])
    _chord_tester(triads[5], ['A4', 'C5', 'E5'])
    _chord_tester(triads[6], ['B4', 'D5', 'F5'])

def test_Diatonic_seventh():
    scale = Diatonic(Note('C4'))
    _chord_tester(scale.seventh('C4'), ['C4', 'E4', 'G4', 'B4'])
    _chord_tester(scale.seventh('D4'), ['D4', 'F4', 'A4', 'C5'])
    _chord_tester(scale.seventh('E4'), ['E4', 'G4', 'B4', 'D5'])
    _chord_tester(scale.seventh('F4'), ['F4', 'A4', 'C5', 'E5'])
    _chord_tester(scale.seventh('G4'), ['G4', 'B4', 'D5', 'F5'])
    _chord_tester(scale.seventh('A4'), ['A4', 'C5', 'E5', 'G5'])
    _chord_tester(scale.seventh('B4'), ['B4', 'D5', 'F5', 'A5'])

def test_Diatonic_sevenths():
    scale = Diatonic(Note('C4'))
    sevenths = scale.sevenths()
    _chord_tester(sevenths[0], ['C4', 'E4', 'G4', 'B4'])
    _chord_tester(sevenths[1], ['D4', 'F4', 'A4', 'C5'])
    _chord_tester(sevenths[2], ['E4', 'G4', 'B4', 'D5'])
    _chord_tester(sevenths[3], ['F4', 'A4', 'C5', 'E5'])
    _chord_tester(sevenths[4], ['G4', 'B4', 'D5', 'F5'])
    _chord_tester(sevenths[5], ['A4', 'C5', 'E5', 'G5'])
    _chord_tester(sevenths[6], ['B4', 'D5', 'F5', 'A5'])

def test_Diatonic_transpose():
    scale = Diatonic(Note('C4'))
    assert_that(Note('Bb4') not in scale)
    scale = scale.major_fourth_up()
    assert_that(Note('Bb4') in scale)
