#!/usr/bin/env python


from mingus.notes import Note, TiedNote, NoteGrouping, NoteSequence

def test_Note_transpose():
    n = Note(60)
    n.transpose(5)
    assert n.transpose(5).note == 65
    assert n.transpose(-5).note == 55
    assert n.set_transpose(5).note == 65
    assert n.set_transpose(-5).note == 60
