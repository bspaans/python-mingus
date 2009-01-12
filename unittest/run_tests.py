#! /usr/bin/env python

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


# mingus.core Tests
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

# MIDI TESTS HERE
# ...

# mingus.extras Tests
import test_LilyPond

# See run_fluidsynth_tests.py for audio tests that will otherwise
# slowdown the development cycle when included in this suite.

# Add new suites here...
suite001 = test_notes.suite()
suite002 = test_diatonic.suite()
suite003 = test_intervals.suite()
suite004 = test_chords.suite()
suite005 = test_scales.suite()
suite006 = test_meter.suite()
suite007 = test_progressions.suite()
suite008 = test_value.suite()

suite101 = test_Note.suite()
suite102 = test_NoteContainers.suite()
suite103 = test_Instrument.suite()
suite104 = test_Bar.suite()
suite105 = test_Track.suite()
suite106 = test_Composition.suite()
suite107 = test_Suite.suite()

suite201 = test_LilyPond.suite()

# ...and here
suite = unittest.TestSuite(\
		[suite001, suite002, suite003, suite004, suite005, suite006, suite007, suite008,\
 		 suite101, suite102, suite103, suite104, suite105, suite106, suite107,\
		 suite201, 
		 ])

unittest.TextTestRunner(verbosity=2).run(suite)
