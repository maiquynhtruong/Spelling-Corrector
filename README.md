# Spelling-Corrector
A spelling corrector in Python. Given a dictionary of English word (see [dictionary.txt](/dictionary.txt)) and a word, the corrector will try to correct the word's spelling based on the dictionary file. It will first try different ways of modifying the string (splitting the word, deleting characters, transposing, replacing, or inserting) with other letters in the alphabet. The list of edited words will be check against the dictionary to only retain words that actually exist in the dictionary. 

There are two types of modification, one edit distance and two edit distances. The list of resulting modified words will both be checked against the dictionary. After that, the list of existent words will be considered to choose the word that has the highest probability of being mentioned in the dictionary. That word is the corrected version. If the corrector cannot find any word, the original string is returned.

Unittest class is used to test our corrector. The words being tested are either one or two edit distances away from the correct words, and the correct words actually exist in the dictionary.

The spelling corrector implementation is based the that of [Peter Norvig](http://norvig.com/spell-correct.html) with slight modifications and explanation.

#Example (from unittest)
- somthing -> something
- speling -> seeing
- korrectud -> corrected
- coryright -> copyright
- aventure -> adventure
- additonel -> additional
- peotry -> poetry
- peotryy -> poetry
- word -> word
- quintessential -> quintessential
- moring -> morning
