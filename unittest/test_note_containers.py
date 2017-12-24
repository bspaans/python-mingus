#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path += ['../']
from mingus.containers.note_container import NoteContainer
from mingus.containers.note import Note
import unittest


class test_NoteContainers(unittest.TestCase):

    def setUp(self):
        self.n1 = NoteContainer()
        self.n2 = NoteContainer('A')
        self.n3 = NoteContainer(['A', 'C', 'E'])
        self.n4 = NoteContainer(['A', 'C', 'E', 'F', 'G'])
        self.n5 = NoteContainer([
            'A',
            'C',
            'E',
            'F',
            'G',
            'A',
            ])

    def test_add_note(self):
        self.assertEqual(self.n2, self.n2.add_note('A'))
        self.assertEqual(NoteContainer('A'), self.n1.add_note('A'))
        self.n1 - 'A'
        self.assertEqual(self.n3 + ['F', 'G'], self.n4)
        self.assertEqual(self.n2 + ['C', 'E'], self.n3 - ['F', 'G'])
        self.n2 - ['C', 'E']

    def test_add_notes(self):
        self.assertEqual(self.n3, self.n1.add_notes(['A', 'C', 'E']))
        self.n1.empty()
        self.assertEqual(self.n3, self.n1.add_notes([['A', 4], ['C', 5], ['E',
                         5]]))
        self.n1.empty()
        self.assertEqual(self.n2, self.n1.add_notes(Note('A')))
        self.n1.empty()
        self.assertEqual(self.n2, self.n1.add_notes([Note('A')]))
        self.n1.empty()
        self.assertEqual(self.n2, self.n1.add_notes('A'))
        self.n1.empty()
        self.assertEqual(self.n3, self.n2 + NoteContainer([['C', 5], ['E', 5]]))
        self.n2 = NoteContainer('A')

    def test_remove_note(self):
        n = NoteContainer(['C', 'E', 'G'])
        n.remove_note('C')
        self.assertEqual(NoteContainer(['E', 'G']), n)
        n.remove_note('E')
        self.assertEqual(NoteContainer(['G']), n)
        n.remove_note('G')
        self.assertEqual(NoteContainer([]), n)

    def test_determine(self):
        n = NoteContainer(['C', 'E', 'G'])
        self.assertEqual(['C major triad'], n.determine())
        n.transpose('3')
        self.assertEqual(['E major triad'], n.determine())

    def test_remove_notes(self):
        pass

    def test_sort(self):
        n1 = NoteContainer(['Eb', 'Gb', 'C'])
        n2 = NoteContainer(['Eb', 'Gb', 'Cb'])
        n1.sort()
        n2.sort()
        self.assertEqual(Note('Eb'), n1[0])
        self.assertEqual(Note('Gb'), n2[1])

    def test_getitem(self):
        self.assertEqual(self.n2[0], Note('A'))
        self.assertEqual(self.n3[0], Note('A'))
        self.assertEqual(self.n4[0], Note('A'))
        self.assertEqual(self.n4[1], Note('C', 5))
        self.assertEqual(self.n4[2], Note('E', 5))

    def test_transpose(self):
        n = NoteContainer(['C', 'E', 'G'])
        self.assertEqual(NoteContainer(['E', 'G#', 'B']), n.transpose('3'))
        n = NoteContainer(['C-6', 'E-4', 'G-2'])
        self.assertEqual(NoteContainer(['E-6', 'G#-4', 'B-2']), n.transpose('3'
                         ))

    def test_get_note_names(self):
        self.assertEqual(['A', 'C', 'E'], self.n3.get_note_names())
        self.assertEqual(['A', 'C', 'E', 'F', 'G'], self.n4.get_note_names())
        self.assertEqual(['A', 'C', 'E', 'F', 'G'], self.n5.get_note_names())

    def test_from_chord_shorthand(self):
        self.assertEqual(self.n3, NoteContainer().from_chord_shorthand('Am'))

    def test_from_progression_shorthand(self):
        self.assertEqual(self.n3,
                         NoteContainer().from_progression_shorthand('VI'))

    def test_from_interval_shorthand(self):
        self.assertEqual(NoteContainer(['C-4', 'G-4']),
                         NoteContainer().from_interval_shorthand('C', '5'))
        self.assertEqual(NoteContainer(['F-3', 'C-4']),
                         NoteContainer().from_interval_shorthand('C', '5',
                         False))

    def test_is_consonant(self):
        self.assertTrue(NoteContainer().from_chord('Am').is_consonant())
        self.assertTrue(NoteContainer().from_chord('C').is_consonant())
        self.assertTrue(NoteContainer().from_chord('G').is_consonant())
        self.assertTrue(NoteContainer().from_chord('Dm').is_consonant())
        self.assertTrue(NoteContainer().from_chord('E').is_consonant())
        self.assertTrue(not NoteContainer().from_chord('E7').is_consonant())
        self.assertTrue(not NoteContainer().from_chord('Am7').is_consonant())
        self.assertTrue(not NoteContainer().from_chord('Gdim').is_consonant())

    def test_is_perfect_consonant(self):
        self.assertTrue(NoteContainer(['A', 'E']).is_perfect_consonant())
        self.assertTrue(NoteContainer(['A-4', 'A-6']).is_perfect_consonant())
        self.assertTrue(NoteContainer(['A', 'D']).is_perfect_consonant())
        self.assertTrue(not NoteContainer(['A', 'D']).is_perfect_consonant(False))
        self.assertTrue(not NoteContainer().from_chord('Am'
                     ).is_perfect_consonant())
        self.assertTrue(not NoteContainer().from_chord('C').is_perfect_consonant())
        self.assertTrue(not NoteContainer().from_chord('G').is_perfect_consonant())
        self.assertTrue(not NoteContainer().from_chord('Dm'
                     ).is_perfect_consonant())
        self.assertTrue(not NoteContainer().from_chord('E').is_perfect_consonant())

    def test_is_imperfect_consonant(self):
        self.assertTrue(NoteContainer(['A', 'C']).is_imperfect_consonant())
        self.assertTrue(NoteContainer(['A', 'C#']).is_imperfect_consonant())
        self.assertTrue(NoteContainer(['A', 'F']).is_imperfect_consonant())
        self.assertTrue(NoteContainer(['A', 'F#']).is_imperfect_consonant())
        self.assertTrue(not NoteContainer(['A', 'B']).is_imperfect_consonant())
        self.assertTrue(not NoteContainer(['A', 'E']).is_imperfect_consonant())
        self.assertTrue(not NoteContainer(['A-4', 'A-5']).is_imperfect_consonant())

    def test_is_dissonant(self):
        self.assertTrue(NoteContainer().from_chord('E7').is_dissonant())
        self.assertTrue(NoteContainer().from_chord('Am7').is_dissonant())
        self.assertTrue(NoteContainer().from_chord('Gdim').is_dissonant())
        self.assertTrue(not NoteContainer().from_chord('Am').is_dissonant())
        self.assertTrue(not NoteContainer().from_chord('C').is_dissonant())
        self.assertTrue(not NoteContainer().from_chord('G').is_dissonant())
        self.assertTrue(not NoteContainer().from_chord('Dm').is_dissonant())


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(test_NoteContainers)


