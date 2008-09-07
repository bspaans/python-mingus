import sys
sys.path += ["../"]

from mingus.containers.NoteContainer import NoteContainer
from mingus.containers.Note import Note
import unittest

class test_NoteContainers(unittest.TestCase):
	
	def setUp(self):
		self.n1 = NoteContainer()
		self.n2 = NoteContainer("A")
		self.n3 = NoteContainer(["A", "C", "E"])
		self.n4 = NoteContainer(["A", "C", "E", "F", "G"])

	def test_add_note(self):
		self.assertEqual(self.n2 , self.n2.add_note("A"))
		self.assertEqual(NoteContainer("A"), self.n1.add_note("A"))
		self.n1 - "A"
		self.assertEqual(self.n3 + ["F", "G"], self.n4)
		self.n3 - ["F", "G"]
		self.assertEqual(self.n2 + ["C", "E"], self.n3)
		self.n2 - ["C", "E"]

	def test_add_notes(self):
		self.assertEqual(self.n3, self.n1.add_notes(["A", "C", "E"]))
		self.n1.empty()
		self.assertEqual(self.n3, self.n1.add_notes([["A", 4], ["C", 4], ["E", 4]]))
		self.n1.empty()
		self.assertEqual(self.n2, self.n1.add_notes(Note("A")))
		self.n1.empty()
		self.assertEqual(self.n2, self.n1.add_notes([Note("A")]))
		self.n1.empty()
		self.assertEqual(self.n2, self.n1.add_notes("A"))
		self.n1.empty()
		self.assertEqual(self.n3, self.n2 + NoteContainer(["C", "E"]))
		self.n2 = NoteContainer("A")

	def test_remove_note(self):
		n = NoteContainer(["C", "E", "G"])
		n.remove_note("C")
		self.assertEqual(NoteContainer(["E", "G"]), n)
		n.remove_note("E")
		self.assertEqual(NoteContainer(["G"]), n)
		n.remove_note("G")
		self.assertEqual(NoteContainer([]), n)
		

	def test_remove_notes(self):
		pass

	def test_sort(self):
		n1 = NoteContainer(["Eb", "Gb", "C"])
		n2 = NoteContainer(["Eb", "Gb", "Cb"])
		n1.sort()
		n2.sort()

		self.assertEqual(Note("C"), n1[0])
		self.assertEqual(Note("Cb"), n2[0])

	def test_getitem(self):
		self.assertEqual(self.n2[0], Note("A"))
		self.assertEqual(self.n3[0], Note("C"))
		self.assertEqual(self.n4[0], Note("C"))
		self.assertEqual(self.n4[1], Note("E"))
		self.assertEqual(self.n4[2], Note("F"))

def suite():
	return unittest.TestLoader().loadTestsFromTestCase(test_NoteContainers)

