#!/usr/bin/python
# -*- coding: utf-8 -*-
import mingus.core.value as value
import unittest


class test_value(unittest.TestCase):

    def setUp(self):
        pass

    def test_add(self):
        self.assertEqual(value.add(4, 4), 2)
        self.assertEqual(value.add(4, 8), 8 / 3.0)
        self.assertEqual(value.add(8, 4), 8 / 3.0)

    def test_dots(self):
        self.assertEqual(value.dots(4, 0), 4)
        self.assertEqual(value.dots(4, 1), 8 / 3.0)
        self.assertEqual(value.dots(4, 1), value.add(8, 4))
        self.assertEqual(value.dots(4, 2), value.add(value.add(8, 4), 16))
        self.assertEqual(value.dots(8, 0), 8)
        self.assertEqual(value.dots(8, 1), 16 / 3.0)
        self.assertEqual(value.dots(8, 1), value.add(8, 16))
        self.assertEqual(value.dots(8, 2), value.add(value.add(8, 16), 32))

    def test_determine(self):
        self.assertEqual(value.determine(7), (4, 0, 7, 4))
        self.assertEqual(value.determine(8), (8, 0, 1, 1))
        self.assertEqual(value.determine(10), (8, 0, 5, 4))
        self.assertEqual(value.determine(12), (8, 0, 3, 2))
        self.assertEqual(value.determine(14), (8, 0, 7, 4))
        for x in value.base_values:
            self.assertEqual(value.determine(x), (x, 0, 1, 1))
            self.assertEqual(value.determine(value.dots(x, 1)), (x, 1, 1, 1))
            self.assertEqual(value.determine(value.dots(x, 2)), (x, 2, 1, 1))
            self.assertEqual(value.determine(value.dots(x, 3)), (x, 3, 1, 1))
            self.assertEqual(value.determine(value.dots(x, 4)), (x, 4, 1, 1))
        for (s, x) in enumerate(value.base_triplets):
            self.assertEqual(value.determine(x), (value.base_values[s], 0, 3,
                             2))
        for (s, x) in enumerate(value.base_quintuplets):
            self.assertEqual(value.determine(x), (value.base_values[s], 0, 5,
                             4))
        for (s, x) in enumerate(value.base_septuplets):
            self.assertEqual(value.determine(x), (value.base_values[s], 0, 7,
                             4))

    def test_determine_imperfect(self):
        self.assertEqual(value.determine(9), (8, 0, 1, 1))
        self.assertEqual(value.determine(4.5), (4, 0, 1, 1))

    def test_triplet(self):
        self.assertEqual(value.triplet(1), 1.5)
        self.assertEqual(value.triplet(2), 3)
        self.assertEqual(value.triplet(4), 6)
        self.assertEqual(value.triplet(8), 12)
        self.assertEqual(value.triplet(16), 24)
        self.assertEqual(value.triplet(32), 48)
        self.assertEqual(value.triplet(64), 96)
        self.assertEqual(value.triplet(128), 192)

    def test_quintuplet(self):
        self.assertEqual(value.quintuplet(1), 1.25)
        self.assertEqual(value.quintuplet(2), 2.5)
        self.assertEqual(value.quintuplet(4), 5)
        self.assertEqual(value.quintuplet(8), 10)
        self.assertEqual(value.quintuplet(16), 20)
        self.assertEqual(value.quintuplet(32), 40)
        self.assertEqual(value.quintuplet(64), 80)
        self.assertEqual(value.quintuplet(128), 160)

    def test_septuplet(self):
        self.assertEqual(value.septuplet(1), 1.75)
        self.assertEqual(value.septuplet(2), 3.5)
        self.assertEqual(value.septuplet(4), 7)
        self.assertEqual(value.septuplet(8), 14)
        self.assertEqual(value.septuplet(16), 28)
        self.assertEqual(value.septuplet(32), 56)
        self.assertEqual(value.septuplet(64), 112)
        self.assertEqual(value.septuplet(128), 224)
        self.assertEqual(value.septuplet(1, False), 0.875)
        self.assertEqual(value.septuplet(2, False), 1.75)
        self.assertEqual(value.septuplet(4, False), 3.5)
        self.assertEqual(value.septuplet(8, False), 7)
        self.assertEqual(value.septuplet(16, False), 14)
        self.assertEqual(value.septuplet(32, False), 28)
        self.assertEqual(value.septuplet(64, False), 56)
        self.assertEqual(value.septuplet(128, False), 112)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(test_value)


