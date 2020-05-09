# -*- coding: utf-8 -*-
from __future__ import absolute_import

import unittest

from pkg_resources import resource_filename

import mingus.extra.fft as fft
from mingus.containers import *


class test_fft(unittest.TestCase):
    def setUp(self):
        (self.data, self.freq, self.bits) = fft.data_from_file(
            resource_filename(__name__, "440_sine_clean.wav")
        )

    def test_find_Note(self):
        self.assertEqual(Note("A"), fft.find_Note(self.data, self.freq, self.bits))

    def test_find_melody(self):
        self.assertEqual(
            [(Note("A-4"), 86), (Note("A-5"), 86)],
            fft.find_melody(resource_filename(__name__, "440_880_clean.wav"), 512)[:2],
        )
