#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    mingus - Music theory Python package, run_fluidsynth_tests module.
#    Copyright (C) 2008, Bart Spaans
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Separated fluidsynth tests.

Remember: you need a running fluidsynth server process listening at port
9800 to pass this test.
"""
from __future__ import absolute_import

import unittest
import test_fluidsynth

suite = unittest.TestSuite([test_fluidsynth.suite()])
unittest.TextTestRunner(verbosity=2).run(suite)
