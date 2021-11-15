# -*- coding: utf-8 -*-
from __future__ import absolute_import

import unittest

from mingus.containers.bar import Bar
from mingus.containers.note import Note
from mingus.containers.note_container import NoteContainer
from mingus.core.keys import Key


class test_Bar(unittest.TestCase):
    def setUp(self):
        self.b = Bar("C", (4, 4))
        self.c = Bar("E", (2, 2))
        self.meterless = Bar("C", (0, 0))

    def test_equality(self):
        self.assertEqual(self.b, self.c)
        self.assertEqual(self.b, self.meterless)
        self.assertEqual(self.c, self.meterless)

        b1 = Bar("C", (4, 4))
        b1 + ["A", "C"]
        b1 + ["D"]
        b2 = Bar("C", (4, 4))
        b2 + ["A", "C"]
        b2 + ["D"]
        self.assertEqual(b1, b2)

        self.assertNotEqual(b1, self.b)

    def test_place_notes_types(self):
        self.assertEqual(True, self.meterless + NoteContainer(["A", "C"]))
        self.assertEqual(True, self.meterless + "A")
        self.assertEqual(True, self.meterless + Note("A"))
        self.assertEqual(True, self.meterless + ["A", "B"])
        self.assertEqual(True, self.meterless + [Note("A"), Note("B")])

    def test_get_range(self):
        self.b + NoteContainer(["C", "E"])
        self.assertEqual((Note("C"), Note("E")), self.b.get_range())

    def test_set_item(self):
        b = Bar()
        b + ["A", "C", "E"]  # A4 C5 E5
        c = Bar()
        c + ["A", "C", "E"]
        self.assertEqual(b, c)
        c[0] = NoteContainer(["A", "C", "E"])
        self.assertEqual(b, c)
        c[0] = ["A", "C", "E"]
        self.assertEqual(b, c)
        c[0] = Note("A")
        c[0] = c[0][2] + NoteContainer(["C", "E"])  # C4 E4
        self.assertNotEqual(b, c)
        c[0] = Note("A")
        c[0] = c[0][2] + NoteContainer(["C-5", "E"])  # C5 E5
        self.assertEqual(b, c)
        c[0] = Note("A")
        c[0] = c[0][2] + "C"
        c[0] = c[0][2] + "E"
        self.assertEqual(b, c)

    def test_key(self):
        self.assertEqual(self.b.key, Key("C"))
        self.assertEqual(self.c.key, Key("E"))

    def test_transpose(self):
        b = Bar()
        c = Bar()
        b + ["C", "E", "G"]
        c + ["E", "G#", "B"]
        b + ["F", "A", "C"]
        c + ["A", "C#", "E"]
        b.transpose("3", True)
        self.assertEqual(b, c)
        b.transpose("3", False)
        b.transpose("3")
        self.assertEqual(b, c)

    def test_transpose_rest(self):
        b = Bar()
        b.place_notes('C-4', 4)
        b.place_rest(4)
        c = Bar()
        c.place_notes('E-4', 4)
        c.place_rest(4)
        b.transpose("3", True)
        self.assertEqual(b, c)

    def test_augment(self):
        b = Bar()
        c = Bar()
        d = Bar()
        b + "A"
        c + "A#"
        d + "A##"
        b.augment()
        self.assertEqual(b, c)
        b.augment()
        self.assertEqual(b, d)
        c.augment()
        self.assertEqual(c, d)

    def test_augment_rest(self):
        b = Bar()
        b.place_notes('C-4', 4)
        b.place_rest(4)
        c = Bar()
        c.place_notes('C#-4', 4)
        c.place_rest(4)
        b.augment()
        self.assertEqual(b, c)

    def test_diminish(self):
        b = Bar()
        c = Bar()
        b + "A"
        c + "Ab"
        b.diminish()
        self.assertEqual(b, c)

    def test_diminish_rest(self):
        b = Bar()
        b.place_notes('C#-4', 4)
        b.place_rest(4)
        c = Bar()
        c.place_notes('C-4', 4)
        c.place_rest(4)
        b.diminish()
        self.assertEqual(b, c)

    #    def test_to_minor(self):
    #        b = Bar()
    #        c = Bar()
    #        b + 'C'
    #        c + 'A'
    #        b.to_minor()
    #        self.assertEqual(b, c)
    #
    #    def test_to_major(self):
    #        b = Bar()
    #        c = Bar()
    #        b + 'C'
    #        c + 'A'
    #        c.to_major()
    #        self.assertEqual(b, c)

    def test_get_note_names(self):
        b = Bar()
        b + "C"
        b + "A"
        self.assertEqual(["C", "A"], b.get_note_names())

    def test_determine_chords(self):
        b = Bar()
        b + ["C", "E", "G"]
        b + ["F", "A", "C"]
        self.assertEqual(
            [[0.0, ["C major triad"]], [0.25, ["F major triad"]]], b.determine_chords()
        )

    def test_determine_progression(self):
        b = Bar()
        b + ["C", "E", "G"]
        b + ["F", "A", "C"]
        self.assertEqual([[0.0, ["I"]], [0.25, ["IV"]]], b.determine_progression(True))
