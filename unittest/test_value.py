import mingus.core.value as value
import unittest

class test_value(unittest.TestCase):

	def setUp(self):
		pass

	def test_add(self):
		self.assertEqual( value.add(4, 4), 2 )
		self.assertEqual( value.add(4, 8), 8 / 3.0)
		self.assertEqual( value.add(8, 4), 8 / 3.0)

	def test_dots(self):
		self.assertEqual( value.dots(4, 0), 4)
		self.assertEqual( value.dots(4, 1), 8 / 3.0)
		self.assertEqual( value.dots(4, 1), value.add(8,4))
		self.assertEqual( value.dots(4, 2), value.add(value.add(8,4), 16))
		self.assertEqual( value.dots(8, 0), 8)
		self.assertEqual( value.dots(8, 1), 16 / 3.0)
		self.assertEqual( value.dots(8, 1), value.add(8,16))
		self.assertEqual( value.dots(8, 2), value.add(value.add(8,16), 32))

def suite():
	return unittest.TestLoader().loadTestsFromTestCase(test_value)
	
