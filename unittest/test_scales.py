#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path += ['../']
import mingus.core.scales as scales
import unittest


class test_scales(unittest.TestCase):

    def setUp(self):
        pass

    def scaleTest(
        self,
        answer_dict,
        scale_func,
        name,
        ):
        map(lambda x: self.assertEqual(answer_dict[x], scale_func(x),
            'The %s of %s is not %s, expecting %s' % (name, x, scale_func(x),
            answer_dict[x])), answer_dict.keys())

    def test_diatonic(self):
        self.scaleTest({'C': [
            'C',
            'D',
            'E',
            'F',
            'G',
            'A',
            'B',
            ], 'E': [
            'E',
            'F#',
            'G#',
            'A',
            'B',
            'C#',
            'D#',
            ], 'B': [
            'B',
            'C#',
            'D#',
            'E',
            'F#',
            'G#',
            'A#',
            ]}, scales.diatonic, 'diatonic scale')

    def test_ionian(self):
        self.scaleTest({'C': [
            'C',
            'D',
            'E',
            'F',
            'G',
            'A',
            'B',
            ], 'E': [
            'E',
            'F#',
            'G#',
            'A',
            'B',
            'C#',
            'D#',
            ], 'B': [
            'B',
            'C#',
            'D#',
            'E',
            'F#',
            'G#',
            'A#',
            ]}, scales.ionian, 'ionian mode')

    def test_dorian(self):
        self.scaleTest({'D': [
            'D',
            'E',
            'F',
            'G',
            'A',
            'B',
            'C',
            ], 'F#': [
            'F#',
            'G#',
            'A',
            'B',
            'C#',
            'D#',
            'E',
            ], 'C#': [
            'C#',
            'D#',
            'E',
            'F#',
            'G#',
            'A#',
            'B',
            ]}, scales.dorian, 'dorian mode')

    def test_phrygian(self):
        self.scaleTest({'E': [
            'E',
            'F',
            'G',
            'A',
            'B',
            'C',
            'D',
            ], 'G#': [
            'G#',
            'A',
            'B',
            'C#',
            'D#',
            'E',
            'F#',
            ], 'D#': [
            'D#',
            'E',
            'F#',
            'G#',
            'A#',
            'B',
            'C#',
            ]}, scales.phrygian, 'phrygian mode')

    def test_lydian(self):
        self.scaleTest({'F': [
            'F',
            'G',
            'A',
            'B',
            'C',
            'D',
            'E',
            ], 'A': [
            'A',
            'B',
            'C#',
            'D#',
            'E',
            'F#',
            'G#',
            ], 'E': [
            'E',
            'F#',
            'G#',
            'A#',
            'B',
            'C#',
            'D#',
            ]}, scales.lydian, 'lydian mode')

    def test_mixolydian(self):
        self.scaleTest({'G': [
            'G',
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            ], 'B': [
            'B',
            'C#',
            'D#',
            'E',
            'F#',
            'G#',
            'A',
            ], 'F#': [
            'F#',
            'G#',
            'A#',
            'B',
            'C#',
            'D#',
            'E',
            ]}, scales.mixolydian, 'mixolydian mode')

    def test_aeolian(self):
        self.scaleTest({'A': [
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            ], 'C#': [
            'C#',
            'D#',
            'E',
            'F#',
            'G#',
            'A',
            'B',
            ], 'G#': [
            'G#',
            'A#',
            'B',
            'C#',
            'D#',
            'E',
            'F#',
            ]}, scales.aeolian, 'aeolian mode')

    def test_locrian(self):
        self.scaleTest({'B': [
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'A',
            ], 'D#': [
            'D#',
            'E',
            'F#',
            'G#',
            'A',
            'B',
            'C#',
            ], 'A#': [
            'A#',
            'B',
            'C#',
            'D#',
            'E',
            'F#',
            'G#',
            ]}, scales.locrian, 'locrian mode')

    def test_natural_minor(self):
        self.scaleTest({'C': [
            'C',
            'D',
            'Eb',
            'F',
            'G',
            'Ab',
            'Bb',
            ], 'E': [
            'E',
            'F#',
            'G',
            'A',
            'B',
            'C',
            'D',
            ], 'B': [
            'B',
            'C#',
            'D',
            'E',
            'F#',
            'G',
            'A',
            ]}, scales.natural_minor, 'natural minor scale')

    def test_harmonic_minor(self):
        self.scaleTest({
            'C': [
                'C',
                'D',
                'Eb',
                'F',
                'G',
                'Ab',
                'B',
                ],
            'E': [
                'E',
                'F#',
                'G',
                'A',
                'B',
                'C',
                'D#',
                ],
            'B': [
                'B',
                'C#',
                'D',
                'E',
                'F#',
                'G',
                'A#',
                ],
            'F#': [
                'F#',
                'G#',
                'A',
                'B',
                'C#',
                'D',
                'E#',
                ],
            }, scales.harmonic_minor, 'harmonic minor scale')

    def test_melodic_minor(self):
        self.scaleTest({'C': [
            'C',
            'D',
            'Eb',
            'F',
            'G',
            'A',
            'B',
            ], 'E': [
            'E',
            'F#',
            'G',
            'A',
            'B',
            'C#',
            'D#',
            ], 'B': [
            'B',
            'C#',
            'D',
            'E',
            'F#',
            'G#',
            'A#',
            ]}, scales.melodic_minor, 'melodic minor scale')

    def test_whole_note(self):
        self.scaleTest({'C': [
            'C',
            'D',
            'E',
            'F#',
            'G#',
            'A#',
            ], 'E': [
            'E',
            'F#',
            'G#',
            'A#',
            'B#',
            'C##',
            ], 'B': [
            'B',
            'C#',
            'D#',
            'E#',
            'F##',
            'G##',
            ]}, scales.whole_note, 'whole note scale')

    def test_diminished_scale(self):
        self.scaleTest({'C': [
            'C',
            'D',
            'Eb',
            'F',
            'Gb',
            'Ab',
            'A',
            'B',
            ], 'E': [
            'E',
            'F#',
            'G',
            'A',
            'Bb',
            'C',
            'C#',
            'D#',
            ], 'D': [
            'D',
            'E',
            'F',
            'G',
            'Ab',
            'Bb',
            'B',
            'C#',
            ]}, scales.diminished, 'diminished scale')

    def test_determine(self):
        self.assertEqual(['C ionian'], scales.determine([
            'C',
            'D',
            'E',
            'F',
            'G',
            'A',
            'B',
            ]))
        self.assertEqual(['C aeolian', 'C natural minor'],
                         scales.determine(scales.natural_minor('C')))


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(test_scales)


