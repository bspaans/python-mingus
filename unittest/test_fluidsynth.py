import sys
sys.path += ["../"]

from mingus.extra import fluidsynth
from mingus.containers import *
import unittest
import time

class test_fluidsynth(unittest.TestCase):
	
	def setUp(self):
		fluidsynth.init_fluidsynth()

	def test_playnote(self):
		self.assert_(fluidsynth.play_Note(Note("C")))
		time.sleep(1)
		fluidsynth.stop_Note(Note("C"))

	def test_playnotecontainer(self):
		self.assert_(fluidsynth.play_NoteContainer(NoteContainer(["C", "E", "G"])))
		time.sleep(1)
		fluidsynth.stop_NoteContainer(NoteContainer(["C", "E", "G"]))
		self.assert_(fluidsynth.play_NoteContainer(NoteContainer(["E", "G", Note("C", 6)])))

def suite():
	return unittest.TestLoader().loadTestsFromTestCase(test_fluidsynth)
