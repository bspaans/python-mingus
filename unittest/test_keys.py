#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path += ['../']
import mingus.core.keys as keys
from mingus.core.mt_exceptions import NoteFormatError, KeyError
import unittest

class test_keys(unittest.TestCase):
    def setUp(self):
        self.scale = {
            'C': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
            'F': ['F', 'G', 'A', 'Bb', 'C', 'D', 'E'],
            'd#': ['D#', 'E#', 'F#', 'G#', 'A#', 'B', 'C#']
            }

    def test_get_key(self):
        self.assertEqual(('C', 'a'), keys.get_key())
        self.assertEqual(('C', 'a'), keys.get_key(0))
        self.assertEqual(('Eb', 'c'), keys.get_key(-3))
        self.assertEqual(('C#', 'a#'), keys.get_key(7))

    def test_get_key_signature(self):
        self.assertEqual(0, keys.get_key_signature())
        self.assertEqual(0, keys.get_key_signature('a'))
        self.assertEqual(-3, keys.get_key_signature('Eb'))
        self.assertEqual(7, keys.get_key_signature('a#'))

    def test_get_key_signature_accidentals(self):
        self.assertEqual([], keys.get_key_signature_accidentals())
        self.assertEqual([], keys.get_key_signature_accidentals('C'))
        self.assertEqual(['Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb', 'Fb'],
                keys.get_key_signature_accidentals('Cb'))

    def test_get_notes(self):
        for k in self.scale.keys():
            self.assertEqual(self.scale[k], keys.get_notes(k),
            'Invalid notes for key %s' % self.scale[k])

    def test_relative_major(self):
        known = {
                'c': 'Eb',
                'a': 'C',
                'e': 'G',
                'f': 'Ab',
                'd': 'F',
                'b': 'D',
                }
        for k in known.keys():
            self.assertEqual(known[k], keys.relative_major(k),
                    'The major of %s is not %s, expecting %s' % (k,
                        keys.relative_major(k), known[k]))

    def test_relative_minor(self):
        known = {
                'C': 'a',
                'E': 'c#',
                'B': 'g#',
                'G': 'e',
                'F': 'd'
                }
        for k in known.keys():
            self.assertEqual(known[k], keys.relative_minor(k),
                    'The minor of %s is not %s, expecting %s' % (k,
                        keys.relative_minor(k), known[k]))


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(test_keys)

