'''
Some unit tests for the corrector
'''
import unittest

class CorrectTest(unittest.TestCase):
	"""docstring for CorrectTest"""
	def testEquals(self):
		self.assertEqual(correction('speling'), 'spelling')
		self.assertEqual(correction('korrectud'), 'corrected')
		self.assertEqual(correction('bycycle'), 'bicycle')
		self.assertEqual(correction('inconvient'), 'inconvenient')
		self.assertEqual(correction('arrainged'), 'arranged')
		self.assertEqual(correction('peotry'), 'poetry')
		self.assertEqual(correction('peotryy'), 'poetry')
		self.assertEqual(correction('word'), 'word')
		self.assertEqual(correction('quintessential'), 'quintessential')
		self.assertEqual(correction('moring'), 'morning')

if __name__ == '__main__':
	unittest.main()