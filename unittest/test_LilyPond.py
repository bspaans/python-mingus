import sys
sys.path += ["../"]

import unittest
import mingus.extra.LilyPond as LilyPond

from mingus.containers.Note import Note
from mingus.containers.NoteContainer import NoteContainer
from mingus.containers.Bar import Bar
from mingus.containers.Track import Track
from mingus.containers.Composition import Composition

class test_LilyPond(unittest.TestCase):
	
	def setUp(self):
		self.commonbar = Bar()
		self.ebar = Bar('E', (4,4))
		self.fbar = Bar('F', (6,8))

		for y in [self.commonbar, self.ebar, self.fbar]:
			map(lambda x: y + x, ["C", "E", "G", "B"])

		self.track1 = Track()
		self.track1 + self.commonbar
		self.track2 = Track()
		self.track2 + self.commonbar	
		self.track2 + self.ebar

		self.composition1 = Composition()
		self.composition1.add_track(self.track1)
		self.composition2 = Composition()
		self.composition2.add_track(self.track1)
		self.composition2.add_track(self.track2)

	def test_from_Note(self):
		self.assertEqual(LilyPond.from_Note(Note('C')), "c'")
		self.assertEqual(LilyPond.from_Note(Note('C#')),"cis'")
		self.assertEqual(LilyPond.from_Note(Note('C##')),"cisis'")
		self.assertEqual(LilyPond.from_Note(Note('Cb')),"ces'")
		self.assertEqual(LilyPond.from_Note(Note('Cbb')),"ceses'")
		self.assertEqual(LilyPond.from_Note(Note('C', 5)),"c''")
		self.assertEqual(LilyPond.from_Note(Note('C', 6)), "c'''")
		self.assertEqual(LilyPond.from_Note(Note('C', 7)), "c''''")
		self.assertEqual(LilyPond.from_Note(Note('C', 3)), "c,")
		self.assertEqual(LilyPond.from_Note(Note('C', 2)), "c,,")
		self.assertEqual(LilyPond.from_Note(Note('C', 1)), "c,,,")
		self.assertEqual(LilyPond.from_Note(Note('C', 0)), "c,,,,")


	def test_from_NoteContainer(self):
		self.assertEqual(LilyPond.from_NoteContainer(NoteContainer("C")), "c'")
		self.assertEqual(LilyPond.from_NoteContainer(NoteContainer("C"), 4), "c'4")
		self.assertEqual(LilyPond.from_NoteContainer(NoteContainer(["C", "E"])), "<c' e'>")
		self.assertEqual(LilyPond.from_NoteContainer(NoteContainer(["C", "E"]), 4), "<c' e'>4")

	def test_from_Bar(self):
		self.assertEqual(LilyPond.from_Bar(self.commonbar),\
			"{ \\time 4/4 \\key c \\major c'4 e'4 g'4 b'4 }")
		self.assertEqual(LilyPond.from_Bar(self.ebar),\
			"{ \\time 4/4 \\key e \\major c'4 e'4 g'4 b'4 }")
		self.assertEqual(LilyPond.from_Bar(self.fbar),\
			"{ \\time 6/8 \\key f \\major c'8 e'8 g'8 b'8 }")

	def test_from_Track(self):
		self.assertEqual(LilyPond.from_Track(self.track1),\
			"{ { c'4 e'4 g'4 b'4 } }")
		self.assertEqual(LilyPond.from_Track(self.track2),\
			"{ { c'4 e'4 g'4 b'4 } { \\key e \\major c'4 e'4 g'4 b'4 } }")

	def test_from_Composition(self):
		self.assertEqual(LilyPond.from_Composition(self.composition1),\
			"\\header { title = \"Untitled\" composer = \"\" opus = \"\" } { { c'4 e'4 g'4 b'4 } }")
		self.assertEqual(LilyPond.from_Composition(self.composition2),\
			"\\header { title = \"Untitled\" composer = \"\" opus = \"\" } { { c'4 e'4 g'4 b'4 } } { { c'4 e'4 g'4 b'4 } { \\key e \\major c'4 e'4 g'4 b'4 } }")

	def test_from_Suite(self):
		LilyPond.from_Suite(None)

def suite():
	return unittest.TestLoader().loadTestsFromTestCase(test_LilyPond)

