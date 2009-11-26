#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path += ['../']
import mingus.core.intervals as intervals
import unittest


class test_intervals(unittest.TestCase):

    def setUp(self):
        pass

    def test_seconds(self):
        secs_c = {'C': 'D', 'E': 'F', 'D': 'E'}
        secs_fsharp = {'F#': 'G#', 'A#': 'B', 'E#': 'F#'}
        map(lambda x: self.assertEqual(secs_c[x], intervals.second(x, 'C'),
            'Invalid second for %s in key C' % x), secs_c.keys())
        map(lambda x: self.assertEqual(secs_fsharp[x], intervals.second(x, 'F#'
            ), 'Invalid second for %s in key F#' % x), secs_fsharp.keys())

    def test_minor_unison(self):
        minors = {
            'C': 'Cb',
            'D': 'Db',
            'B': 'Bb',
            'C#': 'C',
            'Cbb': 'Cbbb',
            }
        for x in minors.keys():
            self.assertEqual(minors[x], intervals.minor_unison(x),
                             'The minor unison of %s is not %s, expecting %s'
                              % (x, intervals.minor_unison(x), minors[x]))

    def test_major_unison(self):
        for x in [
            'C',
            'E',
            'F',
            'G',
            'Ab',
            'Dbbb',
            'E####',
            ]:
            self.assertEqual(x, intervals.major_unison(x),
                             'The major unison of %s is not %s, expecting %s'
                              % (x, intervals.major_unison(x), x))

    def test_minor_seconds(self):
        minors = {
            'C': 'Db',
            'Db': 'Ebb',
            'D#': 'E',
            'C#': 'D',
            'E': 'F',
            'F': 'Gb',
            'G': 'Ab',
            'Gb': 'Abb',
            }
        for x in minors.keys():
            self.assertEqual(minors[x], intervals.minor_second(x),
                             'The minor second of %s is not %s, expecting %s'
                              % (x, intervals.minor_second(x), minors[x]))

    def test_major_seconds(self):
        majors = {
            'C': 'D',
            'C#': 'D#',
            'Cb': 'Db',
            'D': 'E',
            'Db': 'Eb',
            'Eb': 'F',
            'E': 'F#',
            'E#': 'F##',
            'A': 'B',
            'Ab': 'Bb',
            'A#': 'B#',
            'Bb': 'C',
            'B': 'C#',
            'B#': 'C##',
            }
        for x in majors.keys():
            self.assertEqual(majors[x], intervals.major_second(x),
                             'The major second of %s is not %s, expecting %s'
                              % (x, intervals.major_second(x), majors[x]))

    def test_minor_thirds(self):
        minors = {
            'C': 'Eb',
            'Cb': 'Ebb',
            'C#': 'E',
            'C##': 'E#',
            'E': 'G',
            'Eb': 'Gb',
            'E#': 'G#',
            'F': 'Ab',
            'Fb': 'Abb',
            'F#': 'A',
            'B': 'D',
            'Bb': 'Db',
            'B#': 'D#',
            }
        for x in minors.keys():
            self.assertEqual(minors[x], intervals.minor_third(x),
                             'The minor third of %s is not %s, expecting %s'
                              % (x, intervals.minor_third(x), minors[x]))

    def test_major_thirds(self):
        majors = {
            'C': 'E',
            'C#': 'E#',
            'Cb': 'Eb',
            'Cbb': 'Ebb',
            'F': 'A',
            'Fb': 'Ab',
            'B': 'D#',
            'Bb': 'D',
            'Bbb': 'Db',
            'B#': 'D##',
            'A': 'C#',
            'Ab': 'C',
            'A#': 'C##',
            }
        for x in majors.keys():
            self.assertEqual(majors[x], intervals.major_third(x),
                             'The major third of %s is not %s, expecting %s'
                              % (x, intervals.major_third(x), majors[x]))

    def test_minor_fourth(self):
        minors = {
            'C': 'Fb',
            'Cb': 'Fbb',
            'C#': 'F',
            'B': 'Eb',
            'Bb': 'Ebb',
            'B#': 'E',
            'F': 'Bbb',
            'F#': 'Bb',
            'F##': 'B',
            }
        for x in minors.keys():
            self.assertEqual(minors[x], intervals.minor_fourth(x),
                             'The minor fourth of %s is not %s, expecting %s'
                              % (x, intervals.minor_fourth(x), minors[x]))

    def test_major_fourth(self):
        majors = {
            'C': 'F',
            'Cb': 'Fb',
            'Cbb': 'Fbb',
            'C#': 'F#',
            'C##': 'F##',
            'B': 'E',
            'A': 'D',
            'F#': 'B',
            'F': 'Bb',
            'Fb': 'Bbb',
            }
        for x in majors.keys():
            self.assertEqual(majors[x], intervals.major_fourth(x),
                             'The major fourth of %s is not %s, expecting %s'
                              % (x, intervals.major_fourth(x), majors[x]))

    def test_minor_fifth(self):
        minors = {
            'C': 'Gb',
            'Cb': 'Gbb',
            'C#': 'G',
            'B': 'F',
            'Bb': 'Fb',
            'B#': 'F#',
            'A': 'Eb',
            'A#': 'E',
            'Ab': 'Ebb',
            }
        for x in minors.keys():
            self.assertEqual(minors[x], intervals.minor_fifth(x),
                             'The minor fifth of %s is not %s, expecting %s'
                              % (x, intervals.minor_fifth(x), minors[x]))

    def test_major_fifth(self):
        majors = {
            'C': 'G',
            'Cb': 'Gb',
            'Cbb': 'Gbb',
            'C#': 'G#',
            'C##': 'G##',
            'B': 'F#',
            'A': 'E',
            'F#': 'C#',
            'F': 'C',
            'Fb': 'Cb',
            }
        for x in majors.keys():
            self.assertEqual(majors[x], intervals.major_fifth(x),
                             'The major fifth of %s is not %s, expecting %s'
                              % (x, intervals.major_fifth(x), majors[x]))

    def test_minor_sixths(self):
        minors = {
            'C': 'Ab',
            'C#': 'A',
            'Cb': 'Abb',
            'E': 'C',
            'Eb': 'Cb',
            'E#': 'C#',
            'F': 'Db',
            'F#': 'D',
            'Fb': 'Dbb',
            }
        for x in minors.keys():
            self.assertEqual(minors[x], intervals.minor_sixth(x),
                             'The minor sixth of %s is not %s, expecting %s'
                              % (x, intervals.minor_sixth(x), minors[x]))

    def test_major_sixth(self):
        majors = {
            'C': 'A',
            'Cb': 'Ab',
            'Cbb': 'Abb',
            'C#': 'A#',
            'C##': 'A##',
            'B': 'G#',
            'A': 'F#',
            'F#': 'D#',
            'F': 'D',
            'Fb': 'Db',
            }
        for x in majors.keys():
            self.assertEqual(majors[x], intervals.major_sixth(x),
                             'The major sixth of %s is not %s, expecting %s'
                              % (x, intervals.major_sixth(x), majors[x]))

    def test_minor_sevenths(self):
        minors = {
            'C': 'Bb',
            'Cb': 'Bbb',
            'C#': 'B',
            'E': 'D',
            'Eb': 'Db',
            'E#': 'D#',
            'E####': 'D####',
            'B': 'A',
            'Bb': 'Ab',
            }
        for x in minors.keys():
            self.assertEqual(minors[x], intervals.minor_seventh(x),
                             'The minor seventh of %s is not %s, expecting %s'
                              % (x, intervals.minor_seventh(x), minors[x]))

    def test_major_seventh(self):
        majors = {
            'C': 'B',
            'Cb': 'Bb',
            'Cbb': 'Bbb',
            'C#': 'B#',
            'C##': 'B##',
            'B': 'A#',
            'A': 'G#',
            'F#': 'E#',
            'F': 'E',
            'Fb': 'Eb',
            }
        for x in majors.keys():
            self.assertEqual(majors[x], intervals.major_seventh(x),
                             'The major seventh of %s is not %s, expecting %s'
                              % (x, intervals.major_seventh(x), majors[x]))

    def test_valid_measure(self):
        self.assertEqual(0, intervals.measure('C', 'C'))
        self.assertEqual(4, intervals.measure('C', 'E'))
        self.assertEqual(8, intervals.measure('E', 'C'))

    def test_determine(self):
        self.assertEqual('major third', intervals.determine('C', 'E'))
        self.assertEqual('minor third', intervals.determine('C', 'Eb'))
        self.assertEqual('diminished third', intervals.determine('C', 'Ebb'))
        self.assertEqual('minor unison', intervals.determine('C', 'Cb'))
        self.assertEqual('augmented unison', intervals.determine('Cb', 'C'))
        self.assertEqual('diminished unison', intervals.determine('C', 'Cbb'))
        self.assertEqual('augmented unison', intervals.determine('Cbb', 'C'))
        self.assertEqual('minor unison', intervals.determine('A', 'Ab'))
        self.assertEqual('diminished unison', intervals.determine('A', 'Abb'))
        self.assertEqual('major unison', intervals.determine('A', 'A'))
        self.assertEqual('augmented unison', intervals.determine('Abb', 'A'))
        self.assertEqual('augmented unison', intervals.determine('A',
                         'A##########'))
        self.assertEqual('major seventh', intervals.determine('Cb', 'Bb'))
        self.assertEqual('major seventh', intervals.determine('Cbb', 'Bbb'))
        self.assertEqual('major seventh', intervals.determine('Cbbb', 'Bbbb'))
        self.assertEqual('major seventh', intervals.determine('Ab', 'G'))

    def test_determine_shorthand(self):
        self.assertEqual('3', intervals.determine('C', 'E', True))
        self.assertEqual('b3', intervals.determine('C', 'Eb', True))
        self.assertEqual('##3', intervals.determine('C', 'E##', True))
        self.assertEqual('bb3', intervals.determine('C', 'Ebb', True))
        self.assertEqual('b1', intervals.determine('C', 'Cb', True))
        self.assertEqual('#1', intervals.determine('Cb', 'C', True))
        self.assertEqual('bb1', intervals.determine('C', 'Cbb', True))

    def test_from_shorthand(self):
        self.assertEqual('C', intervals.from_shorthand('A', 'b3'))
        self.assertEqual('A', intervals.from_shorthand('C', 'b3', False))
        self.assertEqual('A', intervals.from_shorthand('C#', '3', False))
        self.assertEqual('Cb', intervals.from_shorthand('A', 'bb3'))
        self.assertEqual('Cbb', intervals.from_shorthand('A', 'bbb3'))
        self.assertEqual('F###', intervals.from_shorthand('A', 'bbb3', False))
        self.assertEqual('C#', intervals.from_shorthand('A', '3'))
        self.assertEqual('C##', intervals.from_shorthand('A', '#3'))
        self.assertEqual('C###', intervals.from_shorthand('A', '##3'))
        self.assertEqual('E', intervals.from_shorthand('D', '2'))
        self.assertEqual('F#', intervals.from_shorthand('D', '3'))

    def test_invert(self):
        self.assertEqual(['C', 'E'], intervals.invert(['E', 'C']))

    def test_is_consonant(self):
        self.assert_(intervals.is_consonant('C', 'Eb'))
        self.assert_(intervals.is_consonant('C', 'E'))
        self.assert_(intervals.is_consonant('C', 'F'))
        self.assert_(intervals.is_consonant('C', 'G'))
        self.assert_(intervals.is_consonant('C', 'Ab'))
        self.assert_(intervals.is_consonant('C', 'A'))
        self.assert_(intervals.is_consonant('C', 'C'))
        self.assert_(not intervals.is_consonant('C', 'Db'))
        self.assert_(not intervals.is_consonant('C', 'D'))
        self.assert_(not intervals.is_consonant('C', 'F#'))
        self.assert_(not intervals.is_consonant('C', 'Bb'))
        self.assert_(not intervals.is_consonant('C', 'B'))

    def test_is_perfect_consonant(self):
        self.assert_(intervals.is_perfect_consonant('C', 'F'))
        self.assert_(not intervals.is_perfect_consonant('C', 'F', False))

    def test_is_dissonant(self):
        self.assert_(not intervals.is_dissonant('C', 'Eb'))
        self.assert_(not intervals.is_dissonant('C', 'E'))
        self.assert_(not intervals.is_dissonant('C', 'F'))
        self.assert_(not intervals.is_dissonant('C', 'G'))
        self.assert_(not intervals.is_dissonant('C', 'Ab'))
        self.assert_(not intervals.is_dissonant('C', 'A'))
        self.assert_(not intervals.is_dissonant('C', 'C'))
        self.assert_(intervals.is_dissonant('C', 'Db'))
        self.assert_(intervals.is_dissonant('C', 'D'))
        self.assert_(intervals.is_dissonant('C', 'F#'))
        self.assert_(intervals.is_dissonant('C', 'Bb'))
        self.assert_(intervals.is_dissonant('C', 'B'))


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(test_intervals)


