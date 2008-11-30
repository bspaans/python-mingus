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
		time.sleep(1)
		fluidsynth.stop_NoteContainer(NoteContainer(["E", "G", Note("C", 6)]))


	def test_playbar(self):
		b = Bar()
		b + Note("C")
		b + Note("E")
		b + Note("G")
		self.assert_(fluidsynth.play_Bar(b))

	def test_playbars(self):
		b = Bar()
		b + Note("C")
		b + Note("E")
		b + Note("G")
		c = Bar()
		c + Note("Eb")
		c + "Gb"
		c + "B"
		c + Note("C", 5)
		self.assert_(fluidsynth.play_Bars([b, c], [1, 2]))

	def test_track(self):
		b = Bar()
		b + Note("C")
		b + Note("E")
		b + Note("A")
		b + "E"

		t = Track()
		t + b
		t + b
		self.assert_(fluidsynth.play_Track(t))

	def test_tracks(self):
		b = Bar()
		b + Note("C")
		b + Note("E")
		b + Note("A")
		b + "E"
		c = Bar()
		c + Note("Eb")
		c + "Gb"
		c + "B"
		c + Note("C", 5)

		t = Track()
		t + b
		t + c

		t2 = Track()
		t2 + b
		t2 + b
		self.assert_(fluidsynth.play_Tracks([t, t2], [0, 1]))


def suite():
	return unittest.TestLoader().loadTestsFromTestCase(test_fluidsynth)
