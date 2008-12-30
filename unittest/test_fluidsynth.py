import sys
sys.path += ["../"]

from mingus.midi import FluidSynth
from mingus.containers import *
import unittest
import time

class test_FluidSynth(unittest.TestCase):
	
	def setUp(self):
		FluidSynth.init("example.sf2")

	def test_main_volume(self):
		for x in range(0, 128, 20):
			FluidSynth.midi.main_volume(1, x)
			FluidSynth.midi.main_volume(2, x)
			FluidSynth.play_NoteContainer(NoteContainer(["C", "E", "G"]), 100,1)
			time.sleep(0.25)

	def test_control_change(self):
		for x in range(0, 128, 20):
			FluidSynth.midi.control_change(1, 13,x)
			FluidSynth.play_NoteContainer(NoteContainer(["C", "E", "G"]), 100,1)
			time.sleep(0.25)

	def test_playnote(self):
		self.assert_(FluidSynth.play_Note(Note("C")))
		time.sleep(0.25)
		FluidSynth.stop_Note(Note("C"))

	def test_playnotecontainer(self):
		self.assert_(FluidSynth.play_NoteContainer(NoteContainer(["C", "E", "G"])))
		time.sleep(0.25)
		FluidSynth.stop_NoteContainer(NoteContainer(["C", "E", "G"]))


		self.assert_(FluidSynth.play_NoteContainer(NoteContainer(["E", "G", Note("C", 6)])))
		time.sleep(0.25)
		FluidSynth.stop_NoteContainer(NoteContainer(["E", "G", Note("C", 6)]))


	def test_playbar(self):
		b = Bar()
		b + Note("C")
		b + Note("E")
		b + Note("G")
		self.assert_(FluidSynth.play_Bar(b))

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
		self.assert_(FluidSynth.play_Bars([b, c], [1, 2]))

	def test_track(self):
		b = Bar()
		b + Note("C")
		b + Note("E")
		b + Note("A")
		b + "E"

		t = Track()
		t + b
		t + b
		self.assert_(FluidSynth.play_Track(t))

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
		self.assert_(FluidSynth.play_Tracks([t, t2], [0, 1]))

	def test_composition(self):
		m = MidiInstrument("Vibraphone")

		b = Bar()
		b + Note("C")
		b + Note("E")
		b + Note("A")
		b + "E"
		c = Bar()
		c + Note("G")
		c + "C"
		c + "E"
		c + Note("C", 5)

		t = Track()
		t + b
		t + c

		t2 = Track()
		t2 + b
		t2 + b

		t2.instrument = m

		c = Composition()
		c+ t
		c+ t2
		self.assert_(FluidSynth.play_Composition(c))
def suite():
	return unittest.TestLoader().loadTestsFromTestCase(test_FluidSynth)
