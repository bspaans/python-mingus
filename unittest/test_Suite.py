import sys
sys.path += ["../"]

from mingus.containers.Suite import Suite
import unittest

class test_Suite(unittest.TestCase):
	
	def setUp(self):
		pass


def suite():
	return unittest.TestLoader().loadTestsFromTestCase(test_Suite)
