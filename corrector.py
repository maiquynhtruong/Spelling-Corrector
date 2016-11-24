import re

def P(word):
	'''
	Probability that word appears in English text
	'''
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

def known(word):
	'''
	The subset of words that appear in the dictionary
	'''
	pass

def edits1(word):
	'''
	Create the corrections based on edits that are one step away from `word`
	'''
	letters = 'abcdefghijklmnopqrstuvwxyz'
	splits = [(word[:i], word[i:]) for i in range(length(word) + 1)]
	deletes = [L + R[1:] for L, R in splits if R]
	transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 2]
	replaces = [L + w + R[1:] for L, R in splits if R for w in letters]
	inserts = [ L + w + R for L, R in splits for w in letter]


def edits2(word):
	'''
	Create edits that are 2 steps away from word
	'''
	pass
