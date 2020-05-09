from __future__ import absolute_import

# -*- coding: utf-8 -*-
import sys

sys.path += ["../"]
import mingus.core.meter as meter
import unittest
from six.moves import range


class test_meter(unittest.TestCase):
    def setUp(self):
        self.simple_meters = [
            (2, 4),
            (3, 4),
            (4, 4),
            (6, 4),
            (8, 4),
            (5, 4),
            (2, 2),
            (1, 2),
            (6, 4),
        ]
        self.compound_meters = [
            (6, 4),
            (9, 4),
            (12, 4),
            (6, 8),
            (9, 8),
            (12, 8),
            (6, 16),
            (9, 16),
            (12, 16),
        ]
        self.asymmetrical_meters = [
            (3, 4),
            (5, 4),
            (7, 4),
            (11, 4),
            (1, 8),
            (3, 8),
            (5, 8),
            (7, 8),
            (3, 16),
            (11, 16),
            (15, 16),
            (17, 16),
        ]

    def test_valid_beat_duration(self):
        for x in [
            1,
            2,
            4,
            8,
            16,
            32,
            64,
            128,
            256,
            512,
            1024,
            2048,
        ]:
            self.assertTrue(
                meter.valid_beat_duration(x), "%d should be a valid beat duration" % x
            )

    def test_invalid_beat_duration(self):
        for x in [0, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15,] + list(range(17, 31)):
            self.assertTrue(
                not meter.valid_beat_duration(x),
                "%d should not be a valid beat duration" % x,
            )

    def test_is_compound(self):
        for x in self.compound_meters:
            self.assertTrue(
                meter.is_compound(x), "%d/%d should be a compound meter" % x
            )

    def test_is_simple(self):
        for x in self.simple_meters:
            self.assertTrue(meter.is_simple(x), "%d/%d should be a simple meter" % x)

    def test_is_valid_meter(self):
        for x in self.compound_meters + self.simple_meters:
            self.assertTrue(meter.is_valid(x), "%d/%d should be a valid meter" % x)

    def test_is_asymmetrical(self):
        for x in self.asymmetrical_meters:
            self.assertTrue(
                meter.is_asymmetrical(x), "%d/%d should be a asymmetrical meter" % x
            )

    def test_is_full(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(test_meter)
