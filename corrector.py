import re
import sys, os
from collections import Counter
#Counter is dict subclass for counting
# Internally represented as a dict with keys as words and values as word occurrences

# fileName = 'dictionary.txt'
fileName = 'dictionary.txt'
filePath = os.path.join(os.path.dirname(__file__), fileName)


testName = 'testfile.txt'
testPath = os.path.join(os.path.dirname(__file__), testName)
print testPath
f = open(testPath, 'w')

class Corrector(object):

	def words(text):
		return re.findall(r'\w+', text.lower())

	WORDS = Counter(words(open(filePath, 'r').read()))

	def __init__(self):
		super(Corrector, self).__init__()
		# self.selfWORDS = Counter(self.words(open(filePath, 'r').read()))
		
	
	def P(self, word):
		'''
		Probability that word appears in English text
		'''
		N = sum(Corrector.WORDS.values())
		# N = sum(WORDS.values())
		# return Corrector.WORDS[word] / N
		return Corrector.WORDS[word]

	def correction(self, word):
		'''
		Most probable spelling correction for word.
		This will be the main function
		'''
		if self.candidates(word):
			return max(self.candidates(word), key = self.P)
		else:
			return ''

	def candidates(self, word):
		'''
		Candidates of spelling corrections to consider. We will check these in the
		dictionary
		The error model is the list of words one distance away from the original word is 
		more probable than words that are two distances away from the original word and less
		probable than the original word. In order of priority
		1. Original word, if it is known
		2. List of known words one edit distance away, if there are any
		3. List of known words two edit distances away, if there are any
		4. Original word, even if it is not known
		'''
		return self.known([word]) or self.known(self.edits1(word)) or self.known(self.edits2(word)) or [word]

	def known(self, words):
		'''
		The subset of words that appear in the dictionary
		Receives the lists of modified words from edits1 and check the words against the 
		dictionary. Returns the words that exist
		'''
		return set([w for w in words if w in Corrector.WORDS])
		# return set(w for w in words if w in WORDS)

	def edits1(self, word):
		'''
		Create the corrections based on edits that are one step away from `word`
		'''
		letters = 'abcdefghijklmnopqrstuvwxyz'
		splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
		deletes = [L + R[1:] for L, R in splits if R]
		transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
		replaces = [L + w + R[1:] for L, R in splits if R for w in letters]
		inserts = [ L + w + R for L, R in splits for w in letters]
		# Build set from list of lists
		f.write(str(replaces))
		return set(deletes + transposes + replaces + inserts)

	def edits2(self, word):
		'''
		Create edits that are 2 steps away from word
		'''
		return {ver2 for ver1 in self.edits1(word) for ver2 in self.edits1(ver1)}

