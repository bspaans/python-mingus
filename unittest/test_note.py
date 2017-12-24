#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path += ['../']
from mingus.containers.note import Note
import unittest
from mingus.containers.mt_exceptions import NoteFormatError


class test_Note(unittest.TestCase):

    def setUp(self):
        self.c = Note('C', 5)
        self.c1 = Note('C')
        self.c2 = Note('C', 3)
        self.b4 = Note('B', 4)
        self.b5 = Note('B', 5)

    def test_cmp(self):
        self.assertTrue(self.c1 <= self.b5)
        self.assertTrue(self.c < self.b5)
        self.assertTrue(self.c1 < self.b5)
        self.assertTrue(self.c2 < self.b5)
        self.assertTrue(self.c > self.b4, '%s %s' % (self.c, self.b4))
        self.assertTrue(self.c1 < self.b4)
        self.assertTrue(self.c2 < self.b4)
        self.assertTrue(self.b4 < self.b5)
        self.assertTrue(Note('C') > Note('Cb'))
        self.assertTrue(self.c > None)

    def test_eq(self):
        self.assertTrue(self.c != self.c1)
        self.assertTrue(self.c == self.c)
        self.assertTrue(Note('C') == Note('C'))
        self.assertTrue(self.c != None)

    def test_to_int(self):
        self.assertEqual(48, Note('C', 4))
        self.assertEqual(47, Note('Cb', 4))
        self.assertEqual(36, int(self.c2))
        self.assertEqual(71, int(self.b5))
        self.assertEqual(59, int(self.b4))

    def test_set_note(self):
        n = Note()
        self.assertTrue(n.set_note('C', 5, {}))
        n.empty()
        self.assertTrue(n.set_note('C-5'))
        self.assertTrue(n.set_note('C', 5))
        self.assertTrue(n.set_note('C#-12', 5))
        self.assertRaises(NoteFormatError, n.set_note, 'H')
        self.assertRaises(NoteFormatError, n.set_note, 'C 23')
        self.assertRaises(NoteFormatError, n.set_note, 'C# 123')

    def test_to_hertz(self):
        self.assertEqual(Note('A', 0).to_hertz(), 27.5)
        self.assertEqual(Note('A', 1).to_hertz(), 55)
        self.assertEqual(Note('A', 2).to_hertz(), 110)
        self.assertEqual(Note('A', 3).to_hertz(), 220)
        self.assertEqual(Note('A', 4).to_hertz(), 440)
        self.assertEqual(Note('A', 5).to_hertz(), 880)
        self.assertEqual(Note('A', 6).to_hertz(), 1760)

    def test_from_hertz(self):
        a = Note()
        self.assertEqual(a.from_hertz(55.5), Note('A', 1))
        self.assertEqual(a.from_hertz(110), Note('A', 2))
        a.from_hertz(220)
        self.assertEqual(a, Note('A', 3))
        a.from_hertz(440)
        self.assertEqual(a, Note('A', 4))
        a.from_hertz(880)
        self.assertEqual(a, Note('A', 5))
        a.from_hertz(1760)
        self.assertEqual(a, Note('A', 6))

    def test_transpose(self):
        a = Note('C')
        a.transpose('3')
        self.assertEqual(Note('E'), a)
        a.transpose('b2')
        self.assertEqual(Note('F'), a)
        a.transpose('5')
        self.assertEqual(Note('C', 5), a)
        a.transpose('5', False)
        self.assertEqual(Note('F'), a)
        a = Note('G-5')
        a.transpose('5')
        self.assertEqual(Note('D-6'), a)
        a.transpose('5', False)
        self.assertEqual(Note('G-5'), a)
        a.transpose('5', False)
        self.assertEqual(Note('C-5'), a)

    def test_from_int(self):
        self.assertEqual(Note('C', 0), Note().from_int(0))
        self.assertEqual(Note('C', 1), Note().from_int(12))

    def test_measure(self):
        self.assertTrue(Note('C').measure(Note('D')) == 2)
        self.assertTrue(Note('D').measure(Note('C')) == -2)

    def test_to_shorthand(self):
        self.assertTrue(Note('C-0').to_shorthand() == 'C,,')
        self.assertTrue(Note('C-2').to_shorthand() == 'C')
        self.assertTrue(Note('C-3').to_shorthand() == 'c')
        self.assertTrue(Note('C-4').to_shorthand() == "c'")
        self.assertTrue(Note('C-9').to_shorthand() == "c''''''")

    def test_from_shorthand(self):
        self.assertTrue(Note().from_shorthand('C,,') == Note('C-0'))
        self.assertTrue(Note().from_shorthand('C') == Note('C-2'))
        self.assertTrue(Note().from_shorthand('c') == Note('C-3'))
        self.assertTrue(Note().from_shorthand("c'") == Note('C-4'))
        self.assertTrue(Note().from_shorthand("c''''''") == Note('C-9'))


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(test_Note)


