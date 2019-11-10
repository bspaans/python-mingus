from __future__ import absolute_import

# -*- coding: utf-8 -*-
import sys

sys.path += ["../"]
from mingus.containers.suite import Suite
import unittest


class test_Suite(unittest.TestCase):
    def setUp(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(test_Suite)
