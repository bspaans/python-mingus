#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path += ['../']
from mingus.core.keys import Key
from mingus.containers.bar import Bar
from mingus.containers.note import Note
from mingus.containers.note_container import NoteContainer
from mingus.containers.mt_exceptions import MeterFormatError
import unittest


class test_Bar(unittest.TestCase):

    def setUp(self):
        self.b = Bar('C', (4, 4))
        self.c = Bar('E', (2, 2))
        self.meterless = Bar('C', (0, 0))

    def test_place_notes_types(self):
        self.assertEqual(True, self.meterless + NoteContainer(['A', 'C']))
        self.assertEqual(True, self.meterless + 'A')
        self.assertEqual(True, self.meterless + Note('A'))
        self.assertEqual(True, self.meterless + ['A', 'B'])
        self.assertEqual(True, self.meterless + [Note('A'), Note('B')])

    def test_get_range(self):
        self.b + NoteContainer(['C', 'E'])
        self.assertEqual((Note('C'), Note('E')), self.b.get_range())

    def test_set_item(self):
        b = Bar()
        b + ['A', 'C', 'E']
        c = Bar()
        c + ['A', 'C', 'E']
        self.assertEqual(b, c)
        c[0] = NoteContainer(['A', 'C', 'E'])
        self.assertEqual(b, c)
        c[0] = ['A', 'C', 'E']
        self.assertEqual(b, c)
        c[0] = Note('A')
        c[0] = c[0][2] + NoteContainer(['C', 'E'])
        self.assertEqual(b, c)
        c[0] = Note('A')
        c[0] = c[0][2] + 'C'
        c[0] = c[0][2] + 'E'
        self.assertEqual(b, c)

    def test_key(self):
        self.assertEqual(self.b.key, Key('C'))
        self.assertEqual(self.c.key, Key('E'))

    def test_transpose(self):
        b = Bar()
        c = Bar()
        b + ['C', 'E', 'G']
        c + ['E', 'G#', 'B']
        b + ['F', 'A', 'C']
        c + ['A', 'C#', 'E']
        b.transpose('3', True)
        self.assertEqual(b, c)
        b.transpose('3', False)
        b.transpose('3')
        self.assertEqual(b, c)

    def test_augment(self):
        b = Bar()
        c = Bar()
        d = Bar()
        b + 'A'
        c + 'A#'
        d + 'A##'
        b.augment()
        self.assertEqual(b, c)
        b.augment()
        self.assertEqual(b, d)
        c.augment()
        self.assertEqual(c, d)

    def test_diminish(self):
        b = Bar()
        c = Bar()
        b + 'A'
        c + 'Ab'
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
        b + 'C'
        b + 'A'
        self.assertEqual(['C', 'A'], b.get_note_names())

    def test_determine_chords(self):
        b = Bar()
        b + ['C', 'E', 'G']
        b + ['F', 'A', 'C']
        self.assertEqual([[0.0, ['C major triad']], [0.25, ['F major triad']]],
                         b.determine_chords())

    def test_determine_progression(self):
        b = Bar()
        b + ['C', 'E', 'G']
        b + ['F', 'A', 'C']
        self.assertEqual([[0.0, ['I']], [0.25, ['IV']]],
                         b.determine_progression(True))


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(test_Bar)


