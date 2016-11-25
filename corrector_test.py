'''
Some unit tests for the corrector
'''
import unittest
from corrector import Corrector

class CorrectTest(unittest.TestCase):
	"""Test cases for Corrector"""
	def setUp(self):
		self.corrector = Corrector()

	def test_equals(self):
		self.assertEqual(self.corrector.correction('somthing'), 'something')					# insert
		self.assertEqual(self.corrector.correction('speling'), 'seeing')				# insert
		self.assertEqual(self.corrector.correction('korrectud'), 'corrected')				# replace 2
		self.assertEqual(self.corrector.correction('coryright'), 'copyright')					# replace
		self.assertEqual(self.corrector.correction('aventure'), 'adventure')			# insert 2
		self.assertEqual(self.corrector.correction('additonel'), 'additional')				# delete
		self.assertEqual(self.corrector.correction('peotry'), 'poetry')					# transpose
		self.assertEqual(self.corrector.correction('peotryy'), 'poetry')					# transpose + delete
		self.assertEqual(self.corrector.correction('word'), 'word')						# known
		self.assertEqual(self.corrector.correction('quintessential'), 'quintessential')	# unknown
		self.assertEqual(self.corrector.correction('moring'), 'morning')					# insert

if __name__ == '__main__':
	unittest.main()