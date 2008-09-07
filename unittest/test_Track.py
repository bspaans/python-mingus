import sys
sys.path += ["../"]

from mingus.containers.Track import Track
from mingus.containers.Bar import Bar
from mingus.containers.Instrument import Instrument, Piano, Guitar
import unittest

class test_Track(unittest.TestCase):
	
	def setUp(self):
		self.i = Track(Instrument())
		self.p = Track(Piano())
		self.g = Track(Guitar())
		self.tr = Track()
	
	def test_add(self):
		pass

def suite():
	return unittest.TestLoader().loadTestsFromTestCase(test_Track)

