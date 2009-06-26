import sys
sys.path += ["../"]

import unittest
import mingus.extra.fft as fft

from mingus.containers import *


class test_fft(unittest.TestCase):

        def setUp(self):
                pass

def suite():
        return unittest.TestLoader().loadTestsFromTestCase(test_fft)
