#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path = ['../'] + sys.path
import mingus.core.notes as notes
from mingus.core.mt_exceptions import RangeError
import unittest


class test_notes(unittest.TestCase):

    def setUp(self):
        self.base_notes = [
            'C',
            'D',
            'E',
            'F',
            'G',
            'A',
            'B',
            ]
        self.sharps = map(lambda x: x + '#', self.base_notes)
        self.flats = map(lambda x: x + 'b', self.base_notes)
        self.exotic = map(lambda x: x + 'b###b#', self.base_notes)

    def test_base_note_validity(self):
        map(lambda x: self.assert_(notes.is_valid_note(x), 'Base notes A-G'),
            self.base_notes)

    def test_sharp_note_validity(self):
        map(lambda x: self.assert_(notes.is_valid_note(x), 'Sharp notes A#-G#'
            ), self.sharps)

    def test_flat_note_validity(self):
        map(lambda x: self.assert_(notes.is_valid_note(x), 'Flat notes Ab-Gb'),
            self.flats)

    def test_exotic_note_validity(self):
        map(lambda x: self.assert_(notes.is_valid_note(x),
            'Exotic notes Ab##b#-Gb###b#'), self.exotic)

    def test_faulty_note_invalidity(self):
        map(lambda x: self.assertEqual(False, notes.is_valid_note(x),
            'Faulty notes'), ['asdasd', 'C###f', 'c', 'd', 'E*'])

    def test_valid_int_to_note(self):
        n = [
            'C',
            'C#',
            'D',
            'D#',
            'E',
            'F',
            'F#',
            'G',
            'G#',
            'A',
            'A#',
            'B',
            ]
        map(lambda x: self.assertEqual(n[x], notes.int_to_note(x),
            'Int to note mapping %d-%s failed.' % (x, n[x])), range(0, 12))

    def test_invalid_int_to_note(self):
        faulty = [-1, 12, 13, 123123, -123]
        map(lambda x: self.assertRaises(RangeError, notes.int_to_note, x),
            faulty)

    def test_to_minor(self):
        known = {
            'C': 'A',
            'E': 'C#',
            'B': 'G#',
            'G': 'E',
            'F': 'D',
            }
        map(lambda x: self.assertEqual(known[x], notes.to_minor(x),
            'The minor of %s is not %s, expecting %s' % (x, notes.to_minor(x),
            known[x])), known.keys())

    def test_to_major(self):
        known = {
            'C': 'Eb',
            'A': 'C',
            'E': 'G',
            'F': 'Ab',
            'D': 'F',
            'B': 'D',
            'B#': 'D#',
            }
        map(lambda x: self.assertEqual(known[x], notes.to_major(x),
            'The major of %s is not %s, expecting %s' % (x, notes.to_major(x),
            known[x])), known.keys())

    def test_augment(self):
        known = {
            'C': 'C#',
            'C#': 'C##',
            'Cb': 'C',
            'Cbb': 'Cb',
            }
        map(lambda x: self.assertEqual(known[x], notes.augment(x),
            'The augmented note of %s is not %s, expecting %s' % (x,
            notes.augment(x), known[x])), known.keys())

    def test_diminish(self):
        known = {
            'C': 'Cb',
            'C#': 'C',
            'C##': 'C#',
            'Cb': 'Cbb',
            }
        map(lambda x: self.assertEqual(known[x], notes.diminish(x),
            'The diminished note of %s is not %s, expecting %s' % (x,
            notes.diminish(x), known[x])), known.keys())


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(test_notes)


