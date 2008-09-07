import sys
sys.path += ["../"]

from mingus.containers.Bar import Bar
from mingus.containers.Note import Note
from mingus.containers.NoteContainer import NoteContainer
from mingus.containers.mt_exceptions import MeterFormatError
import unittest

class test_Bar(unittest.TestCase):
	
	def setUp(self):
		self.b = Bar('C', (4, 4))
		self.c = Bar('E', (2, 2))
		self.meterless = Bar('C', (0, 0))

	def test_place_notes_invalid_durations(self):
		for x in filter(lambda x: x % 2 == 1, range(2, 100)):
			self.assertRaises(MeterFormatError, self.b.place_notes, Note("C"), x)

	def test_place_notes_valid_durations(self):
		for x in map(lambda x: 2 ** x, range(1,16)):
			self.assertEqual(True, self.meterless.place_notes(Note("C"), x),\
			"The beat duration %d should result in a valid beat" % x)
		self.meterless.empty()
	
	def test_place_notes_types(self):
		self.assertEqual(True, self.meterless + NoteContainer(["A", "C"]))
		self.assertEqual(True, self.meterless + "A")
		self.assertEqual(True, self.meterless + Note("A"))
		self.assertEqual(True, self.meterless + ["A", "B"])
		self.assertEqual(True, self.meterless + [Note("A"), Note("B")])


	def test_get_range(self):
		self.b + NoteContainer(["C", "E"])
		self.assertEqual((Note("C"), Note("E")), self.b.get_range())

	def test_set_item(self):
		b = Bar()
		b + ["A", "C", "E"]
		c = Bar()
		c + ["A", "C", "E"]

		self.assertEqual(b, c)
		c[0] = NoteContainer(["A", "C", "E"])
		self.assertEqual(b, c)
		c[0] = ["A", "C", "E"]
		self.assertEqual(b, c)
		c[0] = Note("A")
		c[0] = c[0][2] + NoteContainer(["C", "E"])
		self.assertEqual(b, c)
		c[0] = Note("A")
		c[0] = c[0][2] + "C"
		c[0] = c[0][2] + "E"
		self.assertEqual(b, c)

	def test_key(self):
		self.assertEqual(self.b.key, Note("C"))
		self.assertEqual(self.c.key, Note("E"))


	def test_transpose(self):
		b = Bar()
		c= Bar()
		b + ["C", "E", "G"]
		c + ["E", "G#", "B"]
		b + ["F", "A", "C"]
		c + ["A", "C#", "E"]
		b.transpose("3", True)
		self.assertEqual(b, c)
		b.transpose("3", False)
		b.transpose("3")
		self.assertEqual(b, c)

def suite():
	return unittest.TestLoader().loadTestsFromTestCase(test_Bar)

