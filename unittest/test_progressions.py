#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path = ['../'] + sys.path
import unittest
import mingus.core.progressions as progressions


class test_progressions(unittest.TestCase):

    def setUp(self):
        pass

    def test_to_chords(self):
        self.assertEqual([['C', 'E', 'G'], ['G', 'B', 'D']],
                         progressions.to_chords(['I', 'V'], 'C'))
        self.assertEqual([['C', 'E', 'G'], ['G', 'B', 'D', 'F']],
                         progressions.to_chords(['I', 'V7'], 'C'))
        self.assertEqual([['C#', 'E#', 'G#'], ['D#', 'F#', 'A#']],
                         progressions.to_chords(['#I', '#ii']))
        self.assertEqual([['C#', 'E#', 'G#'], ['D#', 'F#', 'A#']],
                         progressions.to_chords(['#I', '#II']))

    def test_to_chords_suffixes(self):
        self.assertEqual(progressions.to_chords(['I7', 'Im7', 'Idim7']), [['C',
                         'E', 'G', 'B'], ['C', 'Eb', 'G', 'Bb'], ['C', 'Eb',
                         'Gb', 'Bbb']])

    def test_parse_string(self):
        self.assertEqual(progressions.parse_string('I'), ('I', 0, ''))
        self.assertEqual(progressions.parse_string('bbbIM7'), ('I', -3, 'M7'))
        self.assertEqual(progressions.parse_string('#b#Im/M7'), ('I', 1, 'm/M7'
                         ))
        self.assertEqual(progressions.parse_string('#####bbVIIM'), ('VII', 3,
                         'M'))

    def test_substitute(self):
        self.assertTrue('III' in progressions.substitute(['I'], 0))
        self.assertTrue('VI' in progressions.substitute(['I'], 0))
        self.assertTrue('V' in progressions.substitute(['VII'], 0))
        self.assertTrue('V7' in progressions.substitute(['VII'], 0))
        self.assertTrue('VII' in progressions.substitute(['V7'], 0))
        self.assertTrue('VIIdim7' in progressions.substitute(['V7'], 0))
        self.assertTrue('IIdim7' in progressions.substitute(['V7'], 0))
        self.assertTrue('IIdim7' in progressions.substitute(['VIIdim7'], 0))
        self.assertTrue('bIIdim7' in progressions.substitute(['bVIIdim7'], 0))
        self.assertTrue('I' in progressions.substitute(['VI'], 0))
        self.assertTrue('IIM' in progressions.substitute(['VIIm'], 0))

    def test_substitute_harmonic(self):
        self.assertTrue('III' in progressions.substitute_harmonic(['I'], 0))
        self.assertTrue([] == progressions.substitute_harmonic(['IM'], 0))
        self.assertTrue('III' in progressions.substitute_harmonic(['IM'], 0, True))

    def test_substitute_minor_for_major(self):
        self.assertTrue('IM' in progressions.substitute_minor_for_major(['VIm'],
                     0))
        self.assertTrue('I' in progressions.substitute_minor_for_major(['VI'], 0))
        self.assertTrue('IM7' in progressions.substitute_minor_for_major(['VIm7'],
                     0))
        self.assertTrue('bIM7' in progressions.substitute_minor_for_major(['bVIm7'
                     ], 0))
        self.assertTrue('#IM7' in progressions.substitute_minor_for_major(['#VIm7'
                     ], 0))

    def test_substitute_major_for_minor(self):
        self.assertTrue('VIm' in progressions.substitute_major_for_minor(['IM'],
                     0))
        self.assertTrue('VIm7' in progressions.substitute_major_for_minor(['IM7'],
                     0))
        self.assertTrue('VI' in progressions.substitute_major_for_minor(['I'], 0))
        self.assertTrue('bVI' in progressions.substitute_major_for_minor(['bI'],
                     0))
        self.assertTrue('#VI' in progressions.substitute_major_for_minor(['#I'],
                     0))

    def test_substitute_diminished_for_diminished(self):
        self.assertTrue(progressions.substitute_diminished_for_diminished(['VII'],
                     0)
                      == progressions.substitute_diminished_for_diminished(['VIIdim'
                     ], 0))
        self.assertTrue('IIdim'
                      in progressions.substitute_diminished_for_diminished(['VII'
                     ], 0))
        self.assertTrue('bIIdim'
                      in progressions.substitute_diminished_for_diminished(['bVII'
                     ], 0))
        self.assertTrue('#IIdim'
                      in progressions.substitute_diminished_for_diminished(['#VII'
                     ], 0))

    def test_substitute_diminished_for_dominant(self):
        self.assertTrue(progressions.substitute_diminished_for_dominant(['VII'], 0)
                      == progressions.substitute_diminished_for_dominant(['VIIdim'
                     ], 0))
        self.assertTrue('Vdom7'
                      in progressions.substitute_diminished_for_dominant(['VII'
                     ], 0))
        self.assertTrue('bVIIdom7'
                      in progressions.substitute_diminished_for_dominant(['VII'
                     ], 0))
        self.assertTrue('bIIdom7'
                      in progressions.substitute_diminished_for_dominant(['VII'
                     ], 0))
        self.assertTrue('bbIIdom7'
                      in progressions.substitute_diminished_for_dominant(['bVII'
                     ], 0))
        self.assertTrue('IVdom7'
                      in progressions.substitute_diminished_for_dominant(['VII'
                     ], 0))
        self.assertTrue('bIVdom7'
                      in progressions.substitute_diminished_for_dominant(['bVII'
                     ], 0))
        self.assertTrue('#IVdom7'
                      in progressions.substitute_diminished_for_dominant(['#VII'
                     ], 0))

    def test_skip(self):
        self.assertEqual(progressions.skip('I'), 'II')
        self.assertEqual(progressions.skip('VII'), 'I')
        self.assertEqual(progressions.skip('VII', 2), 'II')
        self.assertEqual(progressions.skip('VII', 9), 'II')

    def test_determine(self):
        self.assertEqual(['tonic'], progressions.determine(['C', 'E', 'G'], 'C'
                         ))
        self.assertEqual(['tonic seventh'], progressions.determine(['C', 'E',
                         'G', 'B'], 'C'))
        self.assertEqual(['tonic dominant seventh'], progressions.determine(['C'
                         , 'E', 'G', 'Bb'], 'C'))
        self.assertEqual(['I'], progressions.determine(['C', 'E', 'G'], 'C',
                         True))
        self.assertEqual(['I'], progressions.determine(['E', 'G', 'C'], 'C',
                         True))
        self.assertEqual(['I'], progressions.determine(['G', 'C', 'E'], 'C',
                         True))
        self.assertEqual(['V7'], progressions.determine(['G', 'B', 'D', 'F'],
                         'C', True))
        self.assertEqual(['Vm7', 'bviiM6'], progressions.determine(['G', 'Bb',
                         'D', 'F'], 'C', True))
        self.assertEqual([['I'], ['V']], progressions.determine([['C', 'E', 'G'
                         ], ['G', 'B', 'D']], 'C', True))
        self.assertEqual(['bii', 'bIVM6'], progressions.determine(['Db', 'Fb',
                         'Ab'], 'C', True))


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(test_progressions)


