#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path += ['../']
import unittest
import mingus.extra.fft as fft
from mingus.containers import *


class test_fft(unittest.TestCase):

    def setUp(self):
        (self.data, self.freq, self.bits) = \
            fft.data_from_file('440_sine_clean.wav')

    def test_find_Note(self):
        self.assertEqual(Note('A'), fft.find_Note(self.data, self.freq,
                         self.bits))

    def test_find_melody(self):
        self.assertEqual([(Note('A-4'), 86), (Note('A-5'), 86)],
                         fft.find_melody('440_880_clean.wav', 512)[:2])


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(test_fft)


