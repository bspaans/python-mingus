# -*- coding: utf-8 -*-
from __future__ import absolute_import

import unittest

from mingus.containers.instrument import Instrument, Piano, Guitar
from mingus.containers.track import Track


class test_Track(unittest.TestCase):
    def setUp(self):
        self.i = Track(Instrument())
        self.p = Track(Piano())
        self.g = Track(Guitar())
        self.tr = Track()

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
