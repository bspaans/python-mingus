# -*- coding: utf-8 -*-
from __future__ import absolute_import

import unittest

import mingus.extra.tablature as tablature
import mingus.extra.tunings as tunings


class test_Tablature(unittest.TestCase):
    def setUp(self):
        self.guitar = tunings.get_tuning("Guitar", "standard", 6, 1)

    def test__get_qsize(self):
        self.assertTrue(tablature._get_qsize(self.guitar, 4) == 0)
