#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path += ['../']
import mingus.core.scales as scales
import unittest

class test_scales(unittest.TestCase):
    def scaleTest(self, answer_dict, scale, name):
        for k in answer_dict.keys():
            if name == 'diatonic scale':
                self.assertEqual(
                        answer_dict[k][0],
                        scale(k[0], k[1]).ascending(),
                        ('The ascending %s of %s, with semitones in %s, '
                            'is not %s; expecting %s' % (name, k[0], k[1],
                                scale(k[0], k[1]).ascending(),
                                answer_dict[k][0])))
                self.assertEqual(
                        answer_dict[k][1],
                        scale(k[0], k[1]).descending(),
                        ('The descending %s of %s, with semitones in %s, '
                            'is not %s; expecting %s' % (name, k[0], k[1],
                                scale(k[0], k[1]).descending(),
                                answer_dict[k][1])))
            else:
                self.assertEqual(
                        answer_dict[k][0],
                        scale(k).ascending(),
                        ('The ascending %s of %s is not %s; '
                            'expecting %s' % (name, k, scale(k).ascending(),
                                answer_dict[k][0])))
                self.assertEqual(
                        answer_dict[k][1],
                        scale(k).descending(),
                        ('The descending %s of %s is not %s; '
                            'expecting %s' % (name, k, scale(k).descending(),
                                answer_dict[k][1])))

    def test_diatonic(self):
        self.scaleTest({
            ('C', (3, 7)): (
                ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'],
                ['C', 'B', 'A', 'G', 'F', 'E', 'D', 'C']),
            ('E', (3, 7)): (
                ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#', 'E'],
                ['E', 'D#', 'C#', 'B', 'A', 'G#', 'F#', 'E']),
            ('B', (3, 7)): (
                ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B'],
                ['B', 'A#', 'G#', 'F#', 'E', 'D#', 'C#', 'B']),
            ('D', (2, 6)): (
                ['D', 'E', 'F', 'G', 'A', 'B', 'C', 'D'],
                ['D', 'C', 'B', 'A', 'G', 'F', 'E', 'D'])
            }, scales.Diatonic, 'diatonic scale')

    def test_ionian(self):
        self.scaleTest({
            'C': (
                ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'],
                ['C', 'B', 'A', 'G', 'F', 'E', 'D', 'C']),
            'E': (
                ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#', 'E'],
                ['E', 'D#', 'C#', 'B', 'A', 'G#', 'F#', 'E']),
            'B': (
                ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B'],
                ['B', 'A#', 'G#', 'F#', 'E', 'D#', 'C#', 'B'])
            }, scales.Ionian, 'ionian mode')

    def test_dorian(self):
        self.scaleTest({
            'D': (
                ['D', 'E', 'F', 'G', 'A', 'B', 'C', 'D'],
                ['D', 'C', 'B', 'A', 'G', 'F', 'E', 'D']),
            'F#': (
                ['F#', 'G#', 'A', 'B', 'C#', 'D#', 'E', 'F#'],
                ['F#', 'E', 'D#', 'C#', 'B', 'A', 'G#', 'F#']),
            'C#': (
                ['C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B', 'C#'],
                ['C#', 'B', 'A#', 'G#', 'F#', 'E', 'D#', 'C#'])
            }, scales.Dorian, 'dorian mode')

    def test_phrygian(self):
        self.scaleTest({
            'E': (
                ['E', 'F', 'G', 'A', 'B', 'C', 'D', 'E'],
                ['E', 'D', 'C', 'B', 'A', 'G', 'F', 'E']),
            'G#': (
                ['G#', 'A', 'B', 'C#', 'D#', 'E', 'F#', 'G#'],
                ['G#', 'F#', 'E', 'D#', 'C#', 'B', 'A', 'G#']),
            'D#': (
                ['D#', 'E', 'F#', 'G#', 'A#', 'B', 'C#', 'D#'],
                ['D#', 'C#', 'B', 'A#', 'G#', 'F#', 'E', 'D#'])
            }, scales.Phrygian, 'phrygian mode')

    def test_lydian(self):
        self.scaleTest({
            'F': (
                ['F', 'G', 'A', 'B', 'C', 'D', 'E', 'F'],
                ['F', 'E', 'D', 'C', 'B', 'A', 'G', 'F']),
            'A': (
                ['A', 'B', 'C#', 'D#', 'E', 'F#', 'G#', 'A'],
                ['A', 'G#', 'F#', 'E', 'D#', 'C#', 'B', 'A']),
            'E': (
                ['E', 'F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E'],
                ['E', 'D#', 'C#', 'B', 'A#', 'G#', 'F#', 'E'])
            }, scales.Lydian, 'lydian mode')

    def test_mixolydian(self):
        self.scaleTest({
            'G': (
                ['G', 'A', 'B', 'C', 'D', 'E', 'F', 'G'],
                ['G', 'F', 'E', 'D', 'C', 'B', 'A', 'G']),
            'B': (
                ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A', 'B'],
                ['B', 'A', 'G#', 'F#', 'E', 'D#', 'C#', 'B']),
            'F#': (
                ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E', 'F#'],
                ['F#', 'E', 'D#', 'C#', 'B', 'A#', 'G#', 'F#'])
            }, scales.Mixolydian, 'mixolydian mode')

    def test_aeolian(self):
        self.scaleTest({
            'A': (
                ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A'],
                ['A', 'G', 'F', 'E', 'D', 'C', 'B', 'A']),
            'C#': (
                ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B', 'C#'],
                ['C#', 'B', 'A', 'G#', 'F#', 'E', 'D#', 'C#']),
            'G#': (
                ['G#', 'A#', 'B', 'C#', 'D#', 'E', 'F#', 'G#'],
                ['G#', 'F#', 'E', 'D#', 'C#', 'B', 'A#', 'G#'])
            }, scales.Aeolian, 'aeolian mode')

    def test_locrian(self):
        self.scaleTest({
            'B': (
                ['B', 'C', 'D', 'E', 'F', 'G', 'A', 'B'],
                ['B', 'A', 'G', 'F', 'E', 'D', 'C', 'B']),
            'D#': (
                ['D#', 'E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],
                ['D#', 'C#', 'B', 'A', 'G#', 'F#', 'E', 'D#']),
            'A#': (
                ['A#', 'B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'],
                ['A#', 'G#', 'F#', 'E', 'D#', 'C#', 'B', 'A#'])
            }, scales.Locrian, 'locrian mode')

    def test_major(self):
        self.scaleTest({
            'C': (
                ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'],
                ['C', 'B', 'A', 'G', 'F', 'E', 'D', 'C']),
            'A': (
                ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#', 'A'],
                ['A', 'G#', 'F#', 'E', 'D', 'C#', 'B', 'A']),
            'F': (
                ['F', 'G', 'A', 'Bb', 'C', 'D', 'E', 'F'],
                ['F', 'E', 'D', 'C', 'Bb', 'A', 'G', 'F'])
            }, scales.Major, 'major scale')
                
    def test_harmonic_major(self):
        self.scaleTest({
            'C': (
                ['C', 'D', 'E', 'F', 'G', 'Ab', 'B', 'C'],
                ['C', 'B', 'Ab', 'G', 'F', 'E', 'D', 'C']),
            'A': (
                ['A', 'B', 'C#', 'D', 'E', 'F', 'G#', 'A'],
                ['A', 'G#', 'F', 'E', 'D', 'C#', 'B', 'A']),
            'F': (
                ['F', 'G', 'A', 'Bb', 'C', 'Db', 'E', 'F'],
                ['F', 'E', 'Db', 'C', 'Bb', 'A', 'G', 'F'])
            }, scales.HarmonicMajor, 'harmonic major scale')

    def test_natural_minor(self):
        self.scaleTest({
            'C': (
                ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb', 'C'],
                ['C', 'Bb', 'Ab', 'G', 'F', 'Eb', 'D', 'C']),
            'E': (
                ['E', 'F#', 'G', 'A', 'B', 'C', 'D', 'E'],
                ['E', 'D', 'C', 'B', 'A', 'G', 'F#', 'E']),
            'B': (
                ['B', 'C#', 'D', 'E', 'F#', 'G', 'A', 'B'],
                ['B', 'A', 'G', 'F#', 'E', 'D', 'C#', 'B'])
            }, scales.NaturalMinor, 'natural minor scale')

    def test_harmonic_minor(self):
        self.scaleTest({
            'C': (
                ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'B', 'C'],
                ['C', 'B', 'Ab', 'G', 'F', 'Eb', 'D', 'C']),
            'E': (
                ['E', 'F#', 'G', 'A', 'B', 'C', 'D#', 'E'],
                ['E', 'D#', 'C', 'B', 'A', 'G', 'F#', 'E']),
            'B': (
                ['B', 'C#', 'D', 'E', 'F#', 'G', 'A#', 'B'],
                ['B', 'A#', 'G', 'F#', 'E', 'D', 'C#', 'B']),
            'F#': (
                ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E#', 'F#'],
                ['F#', 'E#', 'D', 'C#', 'B', 'A', 'G#', 'F#'])
            }, scales.HarmonicMinor, 'harmonic minor scale')

    def test_melodic_minor(self):
        self.scaleTest({
            'C': (
                ['C', 'D', 'Eb', 'F', 'G', 'A', 'B', 'C'],
                ['C', 'Bb', 'Ab', 'G', 'F', 'Eb', 'D', 'C']),
            'E': (
                ['E', 'F#', 'G', 'A', 'B', 'C#', 'D#', 'E'],
                ['E', 'D', 'C', 'B', 'A', 'G', 'F#', 'E']),
            'B': (
                ['B', 'C#', 'D', 'E', 'F#', 'G#', 'A#', 'B'],
                ['B', 'A', 'G', 'F#', 'E', 'D', 'C#', 'B'])
            }, scales.MelodicMinor, 'melodic minor scale')

    def test_bachian(self):
        self.scaleTest({
            'C': (
                ['C', 'D', 'Eb', 'F', 'G', 'A', 'B', 'C'],
                ['C', 'B', 'A', 'G', 'F', 'Eb', 'D', 'C']),
            'E': (
                ['E', 'F#', 'G', 'A', 'B', 'C#', 'D#', 'E'],
                ['E', 'D#', 'C#', 'B', 'A', 'G', 'F#', 'E']),
            'B': (
                ['B', 'C#', 'D', 'E', 'F#', 'G#', 'A#', 'B'],
                ['B', 'A#', 'G#', 'F#', 'E', 'D', 'C#', 'B'])
            }, scales.Bachian, 'Bachian scale')

    def test_minor_neapolitan(self):
        self.scaleTest({
            'A': (
                ['A', 'Bb', 'C', 'D', 'E', 'F', 'G#', 'A'],
                ['A', 'G', 'F', 'E', 'D', 'C', 'Bb', 'A']),
            'C': (
                ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'B', 'C'],
                ['C', 'Bb', 'Ab', 'G', 'F', 'Eb', 'Db', 'C']),
            'B': (
                ['B', 'C', 'D', 'E', 'F#', 'G', 'A#', 'B'],
                ['B', 'A', 'G', 'F#', 'E', 'D', 'C', 'B'])
            }, scales.MinorNeapolitan, 'minor Neapolitan scale')

    def test_chromatic(self):
        self.scaleTest({
            'C': (
                'C C# D D# E F F# G G# A A# B C'.split(),
                'C B Bb A Ab G Gb F E Eb D Db C'.split()),
            'Eb': (
                'Eb E F F# G Ab A Bb B C C# D Eb'.split(),
                'Eb D Db C B Bb A Ab G Gb F E Eb'.split()),
            'b': (
                'B B# C# D D# E E# F# G G# A A# B'.split(),
                'B Bb A Ab G F# F E Eb D C# C B'.split()),
            'f': (
                'F F# G Ab A Bb B C Db D Eb E F'.split(),
                'F E Eb D Db C B Bb A Ab G Gb F'.split()),
            'bb': (
                'Bb B C Db D Eb E F Gb G Ab A Bb'.split(),
                'Bb A Ab G Gb F E Eb D Db C B Bb'.split())
            }, scales.Chromatic, 'chromatic scale')

    def test_whole_tone(self):
        self.scaleTest({
            'C': (
                ['C', 'D', 'E', 'F#', 'G#', 'A#', 'C'],
                ['C', 'A#', 'G#', 'F#', 'E', 'D', 'C']),
            'E': (
                ['E', 'F#', 'G#', 'A#', 'B#', 'C##', 'E'],
                ['E', 'C##', 'B#', 'A#', 'G#', 'F#', 'E']),
            'B': (
                ['B', 'C#', 'D#', 'E#', 'F##', 'G##', 'B'],
                ['B', 'G##', 'F##', 'E#', 'D#', 'C#', 'B'])
            }, scales.WholeTone, 'whole tone scale')

    def test_octatonic(self):
        self.scaleTest({
            'C': (
                ['C', 'D', 'Eb', 'F', 'Gb', 'Ab', 'A', 'B', 'C'],
                ['C', 'B', 'A', 'Ab', 'Gb', 'F', 'Eb', 'D', 'C']),
            'E': (
                ['E', 'F#', 'G', 'A', 'Bb', 'C', 'C#', 'D#', 'E'],
                ['E', 'D#', 'C#', 'C', 'Bb', 'A', 'G', 'F#', 'E']),
            'D': (
                ['D', 'E', 'F', 'G', 'Ab', 'Bb', 'B', 'C#', 'D'],
                ['D', 'C#', 'B', 'Bb', 'Ab', 'G', 'F', 'E', 'D'])
            }, scales.Octatonic, 'octatonic scale')

    def test_equal(self):
        self.assertEqual(scales.NaturalMinor('C'), scales.NaturalMinor('C'))
        self.assertEqual(scales.Major('F'), scales.Major('F'))
        self.assertEqual(scales.Major('Bb'), scales.Ionian('Bb'))
        self.assertEqual(scales.NaturalMinor('E'), scales.Aeolian('E'))

    def test_not_equal(self):
        self.assertNotEqual(scales.NaturalMinor('C'), scales.NaturalMinor('A'))
        self.assertNotEqual(scales.NaturalMinor('A'), scales.MelodicMinor('A'))
        self.assertNotEqual(scales.Major('F'), scales.Major('D'))
        self.assertNotEqual(scales.Ionian('E'), scales.Dorian('E'))

def suite():
    return unittest.TestLoader().loadTestsFromTestCase(test_scales)

