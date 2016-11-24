'''
Some unit tests for the corrector
'''
import unittest

class CorrectTest(unittest.TestCase):
	"""Test cases for Corrector"""
	def setUp(self):
		self.corrector = Corrector()
		
	def test_equals(self):
		self.assertEqual(self.corrector.correction('speling'), 'spelling')					# insert
		self.assertEqual(self.corrector.correction('korrectud'), 'corrected')				# replace 2
		self.assertEqual(self.corrector.correction('bycycle'), 'bicycle')					# replace
		self.assertEqual(self.corrector.correction('inconvient'), 'inconvenient')			# insert 2
		self.assertEqual(self.corrector.correction('arrainged'), 'arranged')				# delete
		self.assertEqual(self.corrector.correction('peotry'), 'poetry')					# transpose
		self.assertEqual(self.corrector.correction('peotryy'), 'poetry')					# transpose + delete
		self.assertEqual(self.corrector.correction('word'), 'word')						# known
		self.assertEqual(self.corrector.correction('quintessential'), 'quintessential')	# unknown
		self.assertEqual(self.corrector.correction('moring'), 'morning')					# insert
		self.assertEqual(len(WORDS.values()), 32198)
		self.assertEqual(WORDS['the'], 79809)

if __name__ == '__main__':
	unittest.main()