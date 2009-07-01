import sys
sys.path += ["../"]

import mingus.extra.tunings as tunings
import unittest

class test_Suite(unittest.TestCase):
	
	def setUp(self):
		pass


def suite():
	return unittest.TestLoader().loadTestsFromTestCase(test_Suite)
