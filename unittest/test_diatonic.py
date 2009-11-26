#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path += ['../']
import mingus.core.diatonic as diatonic
from mingus.core.mt_exceptions import NoteFormatError, KeyError
import unittest


class test_diatonic(unittest.TestCase):

    def setUp(self):
        self.scale = {
            'C': [
                'C',
                'D',
                'E',
                'F',
                'G',
                'A',
                'B',
                ],
            'F': [
                'F',
                'G',
                'A',
                'Bb',
                'C',
                'D',
                'E',
                ],
            'F#': [
                'F#',
                'G#',
                'A#',
                'B',
                'C#',
                'D#',
                'E#',
                ],
            'Gbbb###b#': [
                'G',
                'A',
                'B',
                'C',
                'D',
                'E',
                'F#',
                ],
            }

    def test_get_notes(self):
        map(lambda x: self.assertEqual(self.scale[x], diatonic.get_notes(x),
            'Invalid notes for key %s' % self.scale[x]), self.scale.keys())

    def test_interval(self):
        self.assertEqual('D', diatonic.interval('C', 'C', 1))
        self.assertEqual('E', diatonic.interval('C', 'C', 2))
        self.assertEqual('F', diatonic.interval('C', 'C', 3))
        self.assertEqual('G', diatonic.interval('C', 'C', 4))
        self.assertEqual('A', diatonic.interval('C', 'C', 5))
        self.assertEqual('B', diatonic.interval('C', 'C', 6))
        self.assertEqual('C', diatonic.interval('C', 'C', 7))
        self.assertEqual('D', diatonic.interval('C', 'C', 8))
        self.assertEqual('C', diatonic.interval('F', 'Bb', 1))

        # Start notes don't have to be in the key:

        self.assertEqual('D', diatonic.interval('C', 'C#', 1))
        self.assertEqual('D', diatonic.interval('C', 'C####', 1))

    def test_int_to_note(self):
        self.assertEqual('G##', diatonic.int_to_note(9, 'A#'))
        self.assertEqual('Bb', diatonic.int_to_note(10, 'F'))
        self.assertEqual('A#', diatonic.int_to_note(10, 'C'))
        self.assertEqual('Bbb', diatonic.int_to_note(9, 'Fb'))
        self.assertEqual('C', diatonic.int_to_note(0, 'D'))


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(test_diatonic)


