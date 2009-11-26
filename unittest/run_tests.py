#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

================================================================================

    Music theory Python package, test suite
    Copyright (C) 2008, Bart Spaans

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

================================================================================

    Test suite for the music theory package. Invoke this file from the
    command line, from within the `unittest` directory to run all the
    testcases.

================================================================================
"""

import unittest

import test_notes
import test_diatonic
import test_intervals
import test_chords
import test_scales
import test_meter
import test_progressions
import test_value

# mingus.containers Tests

import test_Note
import test_NoteContainers
import test_Instrument
import test_Bar
import test_Track
import test_Composition
import test_Suite

# MIDI TESTS HERE ...

import test_fft
import test_tablature
import test_tunings
import test_MusicXML

# See run_fluidsynth_tests.py for FluidSynth audio tests See
# run_lilypond_tests.py to generate some pdf's
#
# Add new suites here...

core = [
    test_notes,
    test_diatonic,
    test_intervals,
    test_chords,
    test_scales,
    test_meter,
    test_progressions,
    test_value,
    ]
containers = [
    test_Note,
    test_NoteContainers,
    test_Instrument,
    test_Bar,
    test_Track,
    test_Composition,
    test_Suite,
    ]
extra = [
        test_fft, 
        test_tunings, 
        test_tablature, 
        test_MusicXML
        ]

# Run all tests

suite = unittest.TestSuite([x.suite() for x in core + containers + extra])
unittest.TextTestRunner(verbosity=2).run(suite)
