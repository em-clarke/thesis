from collections import Counter
from random import choice, choices
from string import ascii_lowercase
from cachetools import cached
from cachetools.keys import hashkey

from makeDictionary import COCA

#### Making/Defining Letter Sets ####
alphabet = "abcdefghijklmnopqrstuvwxyz"
frequencies = [8.04, 1.48, 3.34, 3.82, 12.49, 2.40, 1.87, 5.05, 7.57, 0.16, 0.54, 4.07, 2.51, 7.23, 7.64, 2.14, 0.12, 6.28, 6.51, 9.28, 2.73, 1.05, 1.68, 0.23, 1.66, 0.09]

def getWeightedLetters(n: int) -> str:
  s = ''.join(sorted(choices(alphabet, weights=frequencies, k=n)))
  print(s)
  return s

lSet1 = "abcceeefghhiklnnnorrrssssttvyy"
lSet2 = "aacddeeeeffghiiiimnnooostttuvw"
lSet3 = "abcdeeeeefghiikkmooorrrrssttwy"
lSet4 = "acddeeeeefghiimoorrsssttuuvwwz"
lSet5 = "aaacceefffiklllmnnnnnoprrsttty"
lSet6 = "bddeeefgghiiiillmmnnnorrrsttty" 
lSet7 = "aaabeeegiiillmmnooopprrssstttu"
lSet8 = "cdeeeghiiiiiiklmmnnnnoorrtttvw"

#### Given a set of letters, outputs all the possible words that can be made ####
def getPossibleWords(letters: str, dictionary: set) -> set:
  if len(letters) < 4:
    return set()
  return {word for word in dictionary if wordInStr(word, letters)}


def wordInStr(word : str, letters : str) -> bool:
  wSet, lSet = set(word), set(letters)
  wCount, lCount = Counter(word), Counter(letters)
  if wSet - lSet != set(): return False
  for k,v in wCount.items():
    if v > lCount[k]: return False    
  return True

#### remove used words from a letter set ####
def useWord(word: str, letters: str) -> str:
  remainingLetters = ""
  letters_count = Counter(letters)
  word_count = Counter(word)
  difference = letters_count - word_count
  for item in difference.elements():   
    remainingLetters += item   

  return remainingLetters


#### Generates a list of all possible lists of words that can be made from a letter set ####
def wordListGenerator2(letters: str, seedWords: list=[]) -> list:
  allLists = []

  for seed in seedWords:
    letters = useWord(seed, letters)

  return getAllTuples(letters, getPossibleWords(letters, set(COCA.keys())))

@cached(cache={}, key=lambda letters, _: hashkey(letters))
def getAllTuples(letters: str, words: set) -> set:
  # print(letters)
  newWords = getPossibleWords(letters, words)
  if not newWords:
    return [tuple()]

  tuples = set()
  for word in newWords:
    newLetters = useWord(word, letters)
    newTuples = getAllTuples(newLetters, newWords)
    newTuples = set(map(lambda t : (word,) + t, newTuples))
    tuples = tuples.union(newTuples)
  return tuples