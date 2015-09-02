#!/usr/bin/env python 

from mingus.notes import NotesSequence, Note
from hamcrest import *

def test_NotesSequence_durations():
    n1 = Note('C4').set_change_duration(8)
    n2 = Note('E4').set_change_duration(8)

    ns = NotesSequence()
    ns.add(Note('C4'))
    ns.add([Note('E4'), Note('C4')])
    ns.set_change_duration(8)

    assert_that(ns[0][0], equal_to(n1))
    assert_that(ns[1][0], equal_to(n1))
    assert_that(ns[1][1], equal_to(n2))
