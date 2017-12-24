#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path = ['../'] + sys.path
import mingus.core.notes as notes
from mingus.core.mt_exceptions import RangeError
import unittest

class test_notes(unittest.TestCase):
    def setUp(self):
        self.base_notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        self.sharps = [x + '#' for x in self.base_notes]
        self.flats = [x + 'b' for x in self.base_notes]
        self.exotic = [x + 'b###b#' for x in self.base_notes]

    def test_base_note_validity(self):
        list(map(lambda x: self.assertTrue(notes.is_valid_note(x), 'Base notes A-G'),
                self.base_notes))

    def test_sharp_note_validity(self):
        list(map(lambda x: self.assertTrue(notes.is_valid_note(x), 'Sharp notes A#-G#'
            ), self.sharps))

    def test_flat_note_validity(self):
        list(map(lambda x: self.assertTrue(notes.is_valid_note(x), 'Flat notes Ab-Gb'),
                self.flats))

    def test_exotic_note_validity(self):
        list(map(lambda x: self.assertTrue(notes.is_valid_note(x),
            'Exotic notes Ab##b#-Gb###b#'), self.exotic))

    def test_faulty_note_invalidity(self):
        list(map(lambda x: self.assertEqual(False, notes.is_valid_note(x),
            'Faulty notes'), ['asdasd', 'C###f', 'c', 'd', 'E*']))

    def test_int_to_note(self):
        known = {
                (0, '#'): 'C',
                (3, '#'): 'D#',
                (8, '#'): 'G#',
                (11, '#'): 'B',
                (0, 'b'): 'C',
                (3, 'b'): 'Eb',
                (8, 'b'): 'Ab',
                (11, 'b'): 'B'
                }
        for k in list(known.keys()):
            self.assertEqual(known[k], notes.int_to_note(k[0], k[1]),
                    '%s with "%s" not corrisponding to %s, expecting %s' % (
                        k[0], k[1], notes.int_to_note(k[0], k[1]), known[k]))

    def test_invalid_int_to_note(self):
        faulty = [-1, 12, 13, 123123, -123]
        list(map(lambda x: self.assertRaises(RangeError, notes.int_to_note, x),
            faulty))

    def test_reduce_accidentals(self):
        known = {
                'C': 'C',
                'F#': 'F#',
                'Bb': 'Bb',
                'G##': 'A',
                'Abb': 'G',
                'B##': 'C#',
                'C####': 'E'
                }
        for k in list(known.keys()):
            self.assertEqual(known[k], notes.reduce_accidentals(k),
                    'The reduced note of %s is not %s, expecting %s' % (k,
                        notes.reduce_accidentals(k), known[k]))

    def test_remove_redundant_accidentals(self):
        known = {
                'C##b': 'C#',
                'Eb##b': 'E'
                }
        for k in list(known.keys()):
            self.assertEqual(known[k], notes.remove_redundant_accidentals(k),
                    'The simplified note of %s is not %s, expecting %s' % (k,
                        notes.remove_redundant_accidentals(k), known[k]))

    def test_augment(self):
        known = {
                'C': 'C#',
                'C#': 'C##',
                'Cb': 'C',
                'Cbb': 'Cb'
                }
        list(map(lambda x: self.assertEqual(known[x], notes.augment(x),
            'The augmented note of %s is not %s, expecting %s' % (x,
                notes.augment(x), known[x])), list(known.keys())))

    def test_diminish(self):
        known = {
                'C': 'Cb',
                'C#': 'C',
                'C##': 'C#',
                'Cb': 'Cbb'
                }
        list(map(lambda x: self.assertEqual(known[x], notes.diminish(x),
            'The diminished note of %s is not %s, expecting %s' % (x,
                notes.diminish(x), known[x])), list(known.keys())))


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(test_notes)

