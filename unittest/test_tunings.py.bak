#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path += ['../']
import mingus.extra.tunings as tunings
from mingus.containers.note import Note
from mingus.core.mt_exceptions import RangeError
import unittest


class test_Tunings(unittest.TestCase):

    def setUp(self):
        self.guitar6 = tunings.get_tuning('guitar', 'Standard', 6, 1)
        self.guitar12 = tunings.get_tuning('guitar', 'Standard', 6, 2)

    def test_get_tuning(self):
        self.assert_(tunings.get_tuning('guitar', 'Standard').instrument
                      == 'Guitar')

    def test_get_tunings(self):
        self.assert_(tunings.get_tunings('Guitar')[0].instrument == 'Guitar')
        self.assert_(tunings.get_tunings('Bass guitar')[0].instrument
                      == 'Bass guitar')
        self.assert_(tunings.get_tunings('Bass guita')[0].instrument
                      == 'Bass guitar')
        self.assert_(tunings.get_tunings('Bass')[0].instrument == 'Bass guitar')
        self.assert_('Bass guitar' in [x.instrument for x in
                     tunings.get_tunings('b')])
        self.assert_('Banjo (bass)' in [x.instrument for x in
                     tunings.get_tunings('b')])

    def test_count_strings(self):
        self.assert_(self.guitar6.count_strings() == 6)
        self.assert_(self.guitar12.count_strings() == 6)

    def test_count_courses(self):
        self.assert_(self.guitar6.count_courses() == 1.0)
        self.assert_(self.guitar12.count_courses() == 2.0)

    def test_find_frets(self):
        self.assert_(self.guitar6.find_frets('E-1') == [
            None,
            None,
            None,
            None,
            None,
            None,
            ])
        self.assert_(self.guitar6.find_frets('E-2') == [
            0,
            None,
            None,
            None,
            None,
            None,
            ])
        self.assert_(self.guitar6.find_frets('A-2') == [
            5,
            0,
            None,
            None,
            None,
            None,
            ])
        self.assert_(self.guitar6.find_frets('D-3') == [
            10,
            5,
            0,
            None,
            None,
            None,
            ])
        self.assert_(self.guitar6.find_frets('G-3') == [
            15,
            10,
            5,
            0,
            None,
            None,
            ])
        self.assert_(self.guitar6.find_frets('B-3') == [
            19,
            14,
            9,
            4,
            0,
            None,
            ])
        self.assert_(self.guitar6.find_frets('E-4') == [
            24,
            19,
            14,
            9,
            5,
            0,
            ])
        self.assert_(self.guitar6.find_frets('E-4', 18) == [
            None,
            None,
            14,
            9,
            5,
            0,
            ])

    def test_find_fingering(self):
        self.assert_([(0, 0), (1, 0)] in self.guitar6.find_fingering(['E-2',
                     'A-2']))
        self.assert_([(5, 0), (4, 12)] in self.guitar6.find_fingering(['E-4',
                     'B-4']))

    def test_get_Note(self):
        self.assert_(self.guitar6.get_Note(0, 0) == Note('E-2'))
        self.assert_(self.guitar6.get_Note(1, 0) == Note('A-2'))
        self.assert_(self.guitar6.get_Note(2, 0) == Note('D-3'))
        self.assert_(self.guitar6.get_Note(3, 0) == Note('G-3'))
        self.assert_(self.guitar6.get_Note(3, 3) == Note('A#-3'))
        self.assertRaises(RangeError, self.guitar6.get_Note, -1, 3)
        self.assertRaises(RangeError, self.guitar6.get_Note, 7, 3)
        self.assertRaises(RangeError, self.guitar6.get_Note, 3, -1)
        self.assertRaises(RangeError, self.guitar6.get_Note, 3, 25)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(test_Tunings)


