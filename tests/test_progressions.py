#!/usr/bin/env python 

from mingus.progressions import Progression
from common import _chord_tester


def test_Progression_triads():
    prog = Progression()
    _chord_tester(prog.first(), ['C4', 'E4', 'G4'])
    _chord_tester(prog.second(), ['D4', 'F4', 'A4'])
    _chord_tester(prog.third(), ['E4', 'G4', 'B4'])
    _chord_tester(prog.fourth(), ['F4', 'A4', 'C5'])
    _chord_tester(prog.fifth(), ['G4', 'B4', 'D5'])
    _chord_tester(prog.sixth(), ['A4', 'C5', 'E5'])
    _chord_tester(prog.seventh(), ['B4', 'D5', 'F5'])

def test_Progression_triads_from_string():
    prog = Progression()
    _chord_tester(prog.from_string('I'), ['C4', 'E4', 'G4'])
    _chord_tester(prog.from_string('II'), ['D4', 'F4', 'A4'])
    _chord_tester(prog.from_string('III'), ['E4', 'G4', 'B4'])
    _chord_tester(prog.from_string('IV'), ['F4', 'A4', 'C5'])
    _chord_tester(prog.from_string('V'), ['G4', 'B4', 'D5'])
    _chord_tester(prog.from_string('VI'), ['A4', 'C5', 'E5'])
    _chord_tester(prog.from_string('VII'), ['B4', 'D5', 'F5'])

def test_Progression_sevenths_from_string():
    prog = Progression()
    _chord_tester(prog.from_string('I7'), ['C4', 'E4', 'G4', 'B4'])
    _chord_tester(prog.from_string('II7'), ['D4', 'F4', 'A4', 'C5'])
    _chord_tester(prog.from_string('III7'), ['E4', 'G4', 'B4', 'D5'])
    _chord_tester(prog.from_string('IV7'), ['F4', 'A4', 'C5', 'E5'])
    _chord_tester(prog.from_string('V7'), ['G4', 'B4', 'D5', 'F5'])
    _chord_tester(prog.from_string('VI7'), ['A4', 'C5', 'E5', 'G5'])
    _chord_tester(prog.from_string('VII7'), ['B4', 'D5', 'F5', 'A5'])

def test_Progression_call_is_from_string():
    prog = Progression()
    _chord_tester(prog('I'), ['C4', 'E4', 'G4'])
    _chord_tester(prog('II'), ['D4', 'F4', 'A4'])
    _chord_tester(prog('III'), ['E4', 'G4', 'B4'])
    _chord_tester(prog('IV'), ['F4', 'A4', 'C5'])
    _chord_tester(prog('V'), ['G4', 'B4', 'D5'])
    _chord_tester(prog('VI'), ['A4', 'C5', 'E5'])
    _chord_tester(prog('VII'), ['B4', 'D5', 'F5'])
