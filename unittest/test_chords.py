#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path = ['../'] + sys.path
import mingus.core.chords as chords
from mingus.core.mt_exceptions import RangeError, FormatError, NoteFormatError
import unittest


class test_chords(unittest.TestCase):

    def setUp(self):
        pass

    def test_triad(self):
        self.assertEqual(['C', 'E', 'G'], chords.triad('C', 'C'))
        self.assertEqual(['C', 'Eb', 'G'], chords.triad('C', 'Eb'))

    def test_major_triad(self):
        self.assertEqual(['C', 'E', 'G'], chords.major_triad('C'))
        self.assertEqual(['E', 'G#', 'B'], chords.major_triad('E'))
        self.assertEqual(['Eb', 'G', 'Bb'], chords.major_triad('Eb'))

    def test_minor_triad(self):
        self.assertEqual(['C', 'Eb', 'G'], chords.minor_triad('C'))
        self.assertEqual(['E', 'G', 'B'], chords.minor_triad('E'))
        self.assertEqual(['B', 'D', 'F#'], chords.minor_triad('B'))

    def test_diminished_triad(self):
        self.assertEqual(['C', 'Eb', 'Gb'], chords.diminished_triad('C'))
        self.assertEqual(['E', 'G', 'Bb'], chords.diminished_triad('E'))
        self.assertEqual(['B', 'D', 'F'], chords.diminished_triad('B'))

    def test_augmented_triad(self):
        self.assertEqual(['C', 'E', 'G#'], chords.augmented_triad('C'))
        self.assertEqual(['E', 'G#', 'B#'], chords.augmented_triad('E'))
        self.assertEqual(['B', 'D#', 'F##'], chords.augmented_triad('B'))

    def test_suspended_triad(self):
        self.assertEqual(['C', 'F', 'G'], chords.suspended_triad('C'))
        self.assertEqual(['E', 'A', 'B'], chords.suspended_triad('E'))
        self.assertEqual(['B', 'E', 'F#'], chords.suspended_triad('B'))

    def test_seventh(self):
        self.assertEqual(['C', 'E', 'G', 'B'], chords.seventh('C', 'C'))
        self.assertEqual(['E', 'G', 'B', 'D'], chords.seventh('E', 'C'))
        self.assertEqual(['B', 'D', 'F', 'A'], chords.seventh('B', 'C'))
        self.assertEqual(['B', 'D#', 'F#', 'A#'], chords.seventh('B', 'B'))

    def test_major_seventh(self):
        self.assertEqual(['C', 'E', 'G', 'B'], chords.major_seventh('C'))
        self.assertEqual(['E', 'G#', 'B', 'D#'], chords.major_seventh('E'))
        self.assertEqual(['B', 'D#', 'F#', 'A#'], chords.major_seventh('B'))

    def test_minor_seventh(self):
        self.assertEqual(['C', 'Eb', 'G', 'Bb'], chords.minor_seventh('C'))
        self.assertEqual(['E', 'G', 'B', 'D'], chords.minor_seventh('E'))
        self.assertEqual(['B', 'D', 'F#', 'A'], chords.minor_seventh('B'))

    def test_dominant_seventh(self):
        self.assertEqual(['C', 'E', 'G', 'Bb'], chords.dominant_seventh('C'))
        self.assertEqual(['E', 'G#', 'B', 'D'], chords.dominant_seventh('E'))
        self.assertEqual(['B', 'D#', 'F#', 'A'], chords.dominant_seventh('B'))

    def test_half_diminished_seventh(self):
        self.assertEqual(['C', 'Eb', 'Gb', 'Bb'],
                         chords.half_diminished_seventh('C'))

    def test_diminished_seventh(self):
        self.assertEqual(['C', 'Eb', 'Gb', 'Bbb'], chords.diminished_seventh('C'
                         ))

    def test_minor_major_seventh(self):
        self.assertEqual(['C', 'Eb', 'G', 'B'], chords.minor_major_seventh('C'))

    def test_augmented_major_seventh(self):
        self.assertEqual(['C', 'E', 'G#', 'B'],
                         chords.augmented_major_seventh('C'))

    def test_augmented_minor_seventh(self):
        self.assertEqual(['C', 'E', 'G#', 'Bb'],
                         chords.augmented_minor_seventh('C'))
        self.assertEqual(['E', 'G#', 'B#', 'D'],
                         chords.augmented_minor_seventh('E'))

    def test_tonic(self):
        tonic_dict = {'C': ['C', 'E', 'G'], 'E': ['E', 'G#', 'B'], 'B': ['B',
                      'D#', 'F#']}
        map(lambda x: self.assertEqual(chords.tonic(x), tonic_dict[x]),
            tonic_dict.keys())

    def test_tonic7(self):
        tonic_dict = {'C': ['C', 'E', 'G', 'B'], 'E': ['E', 'G#', 'B', 'D#'],
                      'B': ['B', 'D#', 'F#', 'A#']}
        map(lambda x: self.assertEqual(chords.tonic7(x), tonic_dict[x]),
            tonic_dict.keys())

    def test_dominant(self):
        tonic_dict = {'C': ['G', 'B', 'D'], 'E': ['B', 'D#', 'F#'], 'B': ['F#',
                      'A#', 'C#']}
        map(lambda x: self.assertEqual(chords.dominant(x), tonic_dict[x]),
            tonic_dict.keys())

    def test_dominant7(self):
        tonic_dict = {'C': ['G', 'B', 'D', 'F'], 'E': ['B', 'D#', 'F#', 'A'],
                      'B': ['F#', 'A#', 'C#', 'E']}
        map(lambda x: self.assertEqual(chords.dominant7(x), tonic_dict[x]),
            tonic_dict.keys())

    def test_subdominant(self):
        tonic_dict = {'C': ['F', 'A', 'C'], 'E': ['A', 'C#', 'E'], 'B': ['E',
                      'G#', 'B']}
        map(lambda x: self.assertEqual(chords.subdominant(x), tonic_dict[x]),
            tonic_dict.keys())

    def test_subdominant7(self):
        tonic_dict = {'C': ['F', 'A', 'C', 'E'], 'E': ['A', 'C#', 'E', 'G#'],
                      'B': ['E', 'G#', 'B', 'D#']}
        map(lambda x: self.assertEqual(chords.subdominant7(x), tonic_dict[x]),
            tonic_dict.keys())

    def test_submediant(self):
        tonic_dict = {'C': ['A', 'C', 'E'], 'E': ['C#', 'E', 'G#'], 'B': ['G#',
                      'B', 'D#']}
        map(lambda x: self.assertEqual(chords.submediant(x), tonic_dict[x]),
            tonic_dict.keys())

    def test_submediant7(self):
        tonic_dict = {'C': ['A', 'C', 'E', 'G'], 'E': ['C#', 'E', 'G#', 'B'],
                      'B': ['G#', 'B', 'D#', 'F#']}
        map(lambda x: self.assertEqual(chords.submediant7(x), tonic_dict[x]),
            tonic_dict.keys())

    def test_supertonic(self):
        tonic_dict = {'C': ['D', 'F', 'A'], 'E': ['F#', 'A', 'C#'], 'B': ['C#',
                      'E', 'G#']}
        map(lambda x: self.assertEqual(chords.supertonic(x), tonic_dict[x]),
            tonic_dict.keys())

    def test_supertonic7(self):
        tonic_dict = {'C': ['D', 'F', 'A', 'C'], 'E': ['F#', 'A', 'C#', 'E'],
                      'B': ['C#', 'E', 'G#', 'B']}
        map(lambda x: self.assertEqual(chords.supertonic7(x), tonic_dict[x]),
            tonic_dict.keys())

    def test_mediant(self):
        tonic_dict = {'C': ['E', 'G', 'B'], 'E': ['G#', 'B', 'D#'], 'B': ['D#',
                      'F#', 'A#']}
        map(lambda x: self.assertEqual(chords.mediant(x), tonic_dict[x]),
            tonic_dict.keys())

    def test_mediant7(self):
        tonic_dict = {'C': ['E', 'G', 'B', 'D'], 'E': ['G#', 'B', 'D#', 'F#'],
                      'B': ['D#', 'F#', 'A#', 'C#']}
        map(lambda x: self.assertEqual(chords.mediant7(x), tonic_dict[x]),
            tonic_dict.keys())

    def test_determine_triad(self):
        self.chordsTest([
            [['A minor triad', 'C major sixth, second inversion'], ['A', 'C',
             'E']],
            [['C major sixth', 'A minor triad, first inversion'], ['C', 'E', 'A'
             ]],
            [['C major sixth, first inversion',
             'A minor triad, second inversion'], ['E', 'A', 'C']],
            [['C major triad'], ['C', 'E', 'G']],
            [['E diminished triad', 'G minor sixth, second inversion'], ['E',
             'G', 'Bb']],
            [['F augmented triad'], ['F', 'A', 'C#']],
            [['C suspended fourth triad',
             'F suspended second triad, second inversion'], ['C', 'F', 'G']],
            [['F suspended second triad',
             'C suspended fourth triad, first inversion'], ['F', 'G', 'C']],
            [['C suspended second triad',
             'G suspended fourth triad, first inversion'], ['C', 'D', 'G']],
            [['F suspended second triad, first inversion',
             'C suspended fourth triad, second inversion'], ['G', 'C', 'F']],
            ], chords.determine_triad, 'proper naming')

    def test_determine_triad_shorthand(self):
        self.chordsTest([
            [['Am', 'CM6'], ['A', 'C', 'E']],
            [['CM'], ['C', 'E', 'G']],
            [['Edim', 'Gm6'], ['E', 'G', 'Bb']],
            [['Faug'], ['F', 'A', 'C#']],
            [['Csus4', 'Fsus2'], ['C', 'F', 'G']],
            [['Csus2', 'Gsus4'], ['C', 'D', 'G']],
            ], lambda x: chords.determine_triad(x, True), 'proper naming')

    def test_determine_seventh(self):
        self.chordsTest([
            [['C major seventh'], ['C', 'E', 'G', 'B']],
            [['C major seventh, first inversion'], ['E', 'G', 'B', 'C']],
            [['C major seventh, second inversion'], ['G', 'B', 'C', 'E']],
            [['C major seventh, third inversion'], ['B', 'C', 'E', 'G']],
            [['C minor seventh', 'Eb major sixth, third inversion'], ['C', 'Eb'
             , 'G', 'Bb']],
            [['C dominant seventh'], ['C', 'E', 'G', 'Bb']],
            [['C minor/major seventh'], ['C', 'Eb', 'G', 'B']],
            [['C half diminished seventh', 'Eb minor sixth, third inversion'],
             ['C', 'Eb', 'Gb', 'Bb']],
            [['C diminished seventh'], ['C', 'Eb', 'Gb', 'Bbb']],
            [['C minor/major seventh'], ['C', 'Eb', 'G', 'B']],
            [['C augmented major seventh'], ['C', 'E', 'G#', 'B']],
            [['C augmented minor seventh'], ['C', 'E', 'G#', 'Bb']],
            [['C minor sixth', 'A half diminished seventh, first inversion'],
             ['C', 'Eb', 'G', 'A']],
            [['C minor sixth, first inversion',
             'A half diminished seventh, second inversion'], ['Eb', 'G', 'A',
             'C']],
            [['C minor sixth, second inversion',
             'A half diminished seventh, third inversion'], ['G', 'A', 'C', 'Eb'
             ]],
            [['A half diminished seventh', 'C minor sixth, third inversion'],
             ['A', 'C', 'Eb', 'G']],
            ], chords.determine_seventh, 'proper naming')

    def test_determine_seventh_shorthand(self):
        self.chordsTest([[['Am7', 'CM6', 'CM|Am'], ['A', 'C', 'E', 'G']],
                        [['CM7', 'Em|CM'], ['C', 'E', 'G', 'B']], [['CM7'], ['E'
                        , 'G', 'B', 'C']], [['Fm/M7', 'Abaug|Fm'], ['F', 'Ab',
                        'C', 'E']]], lambda x: chords.determine_seventh(x,
                        True), 'proper naming')

    def chordsTest(
        self,
        values,
        what_func,
        what_desc,
        ):
        map(lambda x: map(lambda y: self.assert_(y in what_func(x[1]),
            "The %s '%s' should be in '%s', but is not." % (what_desc, y,
            what_func(x[1]))), x[0]), values)

    def test_from_shorthand(self):
        answers = {  # Triads Augmented Sevenths Sixths 6/9 Slash chords
                     # Suspended chords 9 11 13 Altered chords Special Poly
                     # chords
            'Amin': ['A', 'C', 'E'],
            'Am': ['A', 'C', 'E'],
            'A-': ['A', 'C', 'E'],
            'Amaj': ['A', 'C#', 'E'],
            'AM': ['A', 'C#', 'E'],
            'A': ['A', 'C#', 'E'],
            'Adim': ['A', 'C', 'Eb'],
            'Aaug': ['A', 'C#', 'E#'],
            'A+': ['A', 'C#', 'E#'],
            'A7#5': ['A', 'C#', 'E#', 'G'],
            'Amaj7+5': ['A', 'C#', 'E#', 'G'],
            'Amaj7+': ['A', 'C#', 'E#', 'G#'],
            'Amin7+': ['A', 'C#', 'E#', 'G'],
            'Amin7': ['A', 'C', 'E', 'G'],
            'Am7': ['A', 'C', 'E', 'G'],
            'Ami7': ['A', 'C', 'E', 'G'],
            'A-7': ['A', 'C', 'E', 'G'],
            'Amaj7': ['A', 'C#', 'E', 'G#'],
            'AM7': ['A', 'C#', 'E', 'G#'],
            'Ama7': ['A', 'C#', 'E', 'G#'],
            'A7': ['A', 'C#', 'E', 'G'],
            'Amin7b5': ['A', 'C', 'Eb', 'G'],
            'Am7b5': ['A', 'C', 'Eb', 'G'],
            'Adim7': ['A', 'C', 'Eb', 'Gb'],
            'Am/M7': ['A', 'C', 'E', 'G#'],
            'Am/ma7': ['A', 'C', 'E', 'G#'],
            'AmM7': ['A', 'C', 'E', 'G#'],
            'Am/maj7': ['A', 'C', 'E', 'G#'],
            'Amin6': ['A', 'C', 'E', 'F#'],
            'Am6': ['A', 'C', 'E', 'F#'],
            'Amaj6': ['A', 'C#', 'E', 'F#'],
            'A6': ['A', 'C#', 'E', 'F#'],
            'A6/9': ['A', 'C#', 'E', 'F#', 'B'],
            'A69': ['A', 'C#', 'E', 'F#', 'B'],
            'A/G': ['G', 'A', 'C#', 'E'],
            'Amin/G': ['G', 'A', 'C', 'E'],
            'Am/M7/G': ['G', 'A', 'C', 'E', 'G#'],
            'Asus2': ['A', 'B', 'E'],
            'Asus4': ['A', 'D', 'E'],
            'Asus47': ['A', 'D', 'E', 'G'],
            'A11': ['A', 'E', 'G', 'D'],
            'Asus': ['A', 'D', 'E'],
            'Asus4b9': ['A', 'D', 'E', 'Bb'],
            'Asusb9': ['A', 'D', 'E', 'Bb'],
            'Amaj9': ['A', 'C#', 'E', 'G#', 'B'],
            'A9': ['A', 'C#', 'E', 'G', 'B'],
            'Amin9': ['A', 'C', 'E', 'G', 'B'],
            'Am9': ['A', 'C', 'E', 'G', 'B'],
            'A7#11': ['A', 'C#', 'E', 'G', 'D#'],
            'Am11': ['A', 'C', 'E', 'G', 'D'],
            'Amin11': ['A', 'C', 'E', 'G', 'D'],
            'Amaj13': [
                'A',
                'C#',
                'E',
                'G#',
                'B',
                'F#',
                ],
            'A13': [
                'A',
                'C#',
                'E',
                'G',
                'B',
                'F#',
                ],
            'Am13': [
                'A',
                'C',
                'E',
                'G',
                'B',
                'F#',
                ],
            'A7b9': ['A', 'C#', 'E', 'G', 'Bb'],
            'A7#9': ['A', 'C#', 'E', 'G', 'B#'],
            'A7b5': ['A', 'C#', 'Eb', 'G'],
            'A6/7': ['A', 'C#', 'E', 'F#', 'G'],
            'A67': ['A', 'C#', 'E', 'F#', 'G'],
            'A5': ['A', 'E'],
            'Ahendrix': ['A', 'C#', 'E', 'G', 'C'],
            'N.C.': [],
            'NC': [],
            'Dm|G': ['G', 'B', 'D', 'F', 'A'],
            'Dm7|G': [
                'G',
                'B',
                'D',
                'F',
                'A',
                'C',
                ],
            'Am7|G7': [
                'G',
                'B',
                'D',
                'F',
                'A',
                'C',
                'E',
                'G',
                ],
            }
        map(lambda x: self.assertEqual(answers[x], chords.from_shorthand(x),
            'The shorthand of %s is not %s, expecting %s' % (x,
            chords.from_shorthand(x), answers[x])), answers.keys())

    def test_malformed_from_shorthand(self):
        for x in ['Bollocks', 'Asd', 'Bbasd@#45']:
            self.assertRaises(FormatError, chords.from_shorthand, x)
            self.assertRaises(NoteFormatError, chords.from_shorthand, x[1:])

    def test_determine(self):
        map(lambda x: self.assertEqual(True,
            chords.determine(chords.from_shorthand('C' + x)) != [],
            "'C%s' should return a value" % x), chords.chord_shorthand.keys())
        map(lambda x: self.assertEqual('C' + chords.chord_shorthand_meaning[x],
            chords.determine(chords.from_shorthand('C' + x))[0],
            "The proper naming of '%s' is not '%s',expecting '%s'" % ('C' + x,
            chords.determine(chords.from_shorthand('C' + x)), 'C'
             + chords.chord_shorthand_meaning[x])), [x for x in
            chords.chord_shorthand.keys() if x != '5'])
        self.chordsTest([[['A13'], [
            'A',
            'C#',
            'E',
            'G',
            'B',
            'D',
            'F#',
            ]], [['Am13'], [
            'A',
            'C',
            'E',
            'G',
            'B',
            'D',
            'F#',
            ]], [['AM13'], [
            'A',
            'C#',
            'E',
            'G#',
            'B',
            'D',
            'F#',
            ]]], lambda x: chords.determine(x, True), 'chord name')

    def test_determine_polychord(self):
        self.chordsTest([  # insano test
            [['FM|Dm'], ['D', 'F', 'A', 'C']],
            [['Dm|GM'], ['G', 'B', 'D', 'F', 'A']],
            [['FM|G7', 'FM|GM'], [
                'G',
                'B',
                'D',
                'F',
                'A',
                'C',
                ]],
            [['Am|G7'], [
                'G',
                'B',
                'D',
                'F',
                'A',
                'C',
                'E',
                ]],
            [['Am7|G7'], [
                'G',
                'B',
                'D',
                'F',
                'A',
                'C',
                'E',
                'G',
                ]],
            [['CM9|CM'], [
                'C',
                'E',
                'G',
                'C',
                'E',
                'G',
                'B',
                'D',
                ]],
            [['CM9|CM7'], [
                'C',
                'E',
                'G',
                'B',
                'C',
                'E',
                'G',
                'B',
                'D',
                ]],
            [['A13|G13'], [
                'G',
                'B',
                'D',
                'F',
                'A',
                'C',
                'E',
                'A',
                'C#',
                'E',
                'G',
                'B',
                'D',
                'F#',
                ]],
            ], lambda x: chords.determine_polychords(x, True),
                'polychord naming')


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(test_chords)


