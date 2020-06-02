from __future__ import absolute_import

import doctest
import unittest

import mingus.containers.track
from mingus.containers.instrument import Instrument, Piano, Guitar
from mingus.containers.track import Track


class test_Track(unittest.TestCase):
    def setUp(self):
        self.i = Track(Instrument())
        self.p = Track(Piano())
        self.g = Track(Guitar())
        self.tr = Track()

    def test_equality(self):
        self.assertEqual(self.i, self.p)
        self.assertEqual(self.i, self.g)
        self.assertEqual(self.i, self.tr)

        t = Track()
        t + "C"
        t + "E"
        s = Track()
        s + "E"
        s + "G#"
        self.assertNotEqual(t, s)
        u = Track()
        u + "E"
        u + "G#"
        self.assertEqual(s, u)

    def test_add(self):
        pass

    def test_transpose(self):
        t = Track()
        t + "C"
        t + "E"
        t.transpose("3")
        s = Track()
        s + "E"
        s + "G#"
        self.assertEqual(s, t)


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(mingus.containers.note))
    return tests
