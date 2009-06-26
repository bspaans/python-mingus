import sys
sys.path += ["../"]

import unittest
import mingus.extra.fft as fft

from mingus.containers import *


class test_fft(unittest.TestCase):

        def setUp(self):
                self.data, self.freq, self.bits = fft.data_from_file("440_sine_clean.wav")

        def test_is_most_likely(self):
                self.assertEqual(Note("A"), fft.is_most_likely(self.data, self.freq, self.bits))

def suite():
        return unittest.TestLoader().loadTestsFromTestCase(test_fft)
