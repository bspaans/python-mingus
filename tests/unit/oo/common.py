from mingus.notes import Note
from hamcrest import *


def _chord_tester(chord, notes):
    assert_that(len(chord) < len(notes), not_(True), "missing notes in chord")
    assert_that(len(chord) > len(notes), not_(True), "more notes in chord than expected")
    for ix, note in enumerate(notes):
        assert_that(
            chord[ix],
            equal_to(Note(note)),
            "Note %d of %s should be %s" % (ix, str(chord), note),
        )
