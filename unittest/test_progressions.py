import sys
sys.path = ["../"] + sys.path
import unittest
import mingus.core.progressions as progressions

class test_progressions(unittest.TestCase):
	
	def setUp(self):
		pass


	def test_to_chords(self):
		self.assertEqual([["C", "E", "G"], ["G", "B", "D"]], \
				progressions.to_chords(["I", "V"], 'C'))
		self.assertEqual([["C", "E", "G"], ["G", "B", "D", "F"]], \
				progressions.to_chords(["I", "V7"], 'C'))
		self.assertEqual([["C#", "E#", "G#"], ["D#", "F#", "A#"]],\
				progressions.to_chords(["#I", "#ii"]))

	def test_determine(self):
		self.assertEqual(['tonic'], progressions.determine(["C", "E", "G"], 'C'))
		self.assertEqual(['tonic seventh'], progressions.determine(["C", "E", "G", "B"], 'C'))
		self.assertEqual(['tonic dominant seventh'], progressions.determine(["C", "E", "G", "Bb"], 'C'))
		self.assertEqual(['I'], progressions.determine(["C", "E", "G"], 'C', True))
		self.assertEqual(['I'], progressions.determine(["E", "G", "C"], 'C', True))
		self.assertEqual(['I'], progressions.determine(["G", "C", "E"], 'C', True))
		self.assertEqual(['V7'], progressions.determine(["G", "B", "D", "F"], 'C', True))
		self.assertEqual(['Vm7', 'bviiM6'], progressions.determine(["G", "Bb", "D", "F"], 'C', True))
		self.assertEqual([['I'], ['V']], progressions.determine([["C", "E", "G"], ["G", "B", "D"]], "C", True))
		self.assertEqual(['bii', 'bIVM6'], progressions.determine(["Db", "Fb", "Ab"], 'C', True))

def suite():
	return unittest.TestLoader().loadTestsFromTestCase(test_progressions)
	

