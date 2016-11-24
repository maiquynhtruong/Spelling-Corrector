import re
import sys, os
from collections import Counter
#Counter is dict subclass for counting
# Internally represented as a dict with keys as words and values as word occurrences

fileName = 'dictionary.txt'
filePath = os.path.join(os.path.dirname(__file__), fileName)
print filePath

def words(text):
	return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open(filePath, 'r').read()))

def P(word):
	'''
	Probability that word appears in English text
	'''
	N = sum(WORDS.values())
	return WORDS[word] / N
	pass

def correction(word):
	'''
	Most probable spelling correction for word.
	This will be the main function
	'''
	pass

def candidates(word):
	'''
	Candidates of spelling corrections to consider. We will check these in the
	dictionary
	'''
	pass

def known(words):
	'''
	The subset of words that appear in the dictionary
	Receives the lists of modified words from edits1 and check the words against the 
	dictionary. Returns the words that exist
	'''
	return set([w for w in words if w in WORDS])

def edits1(word):
	'''
	Create the corrections based on edits that are one step away from `word`
	'''
	letters = 'abcdefghijklmnopqrstuvwxyz'
	splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
	deletes = [L + R[1:] for L, R in splits if R]
	transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
	replaces = [L + w + R[1:] for L, R in splits if R for w in letters]
	inserts = [ L + w + R for L, R in splits for w in letters]
	return set(deletes + transposes + replaces + inserts) # Build set from list of lists

def edits2(word):
	'''
	Create edits that are 2 steps away from word
	'''
	pass

print len(edits1('somthing'))
#known(edits1('somthing'))

#f.write('To test out corrector.py')
#print sys.argv

