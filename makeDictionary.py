from gensimModel import model

COCA = {}
COCA_temp = {}

with open("words_219k_trimmed1.txt") as file, open("ScrabbleWords2019.txt") as file2:
  for line in file:
    (word, freq) = line.split()
    freq = int(freq)
    if freq > 300 and len(word) >= 4 and len(word) <= 10:
      COCA_temp[word] = freq

  for line in file2:
    s_word = line.lower().strip()
    if s_word in COCA_temp:
      COCA[s_word] = COCA_temp[s_word]


def getDictVector(dictionary: set) -> dict:
  vectorDict = dict()
  noVectData = set()
  for word in dictionary:
    try:
      vect = model.get_vector(word)
      vectorDict[word] = vect
    except KeyError:
      noVectData.add(word)
      print(word)
  return vectorDict

def getNoVectorDataWords(dictionary: set) -> set:
  vectorDict = dict()
  noVectData = set()
  for word in dictionary:
    try:
      vect = model.get_vector(word)
      vectorDict[word] = vect
    except KeyError:
      noVectData.add(word)
 #     print(word)
  return noVectData

badWords = getNoVectorDataWords(COCA)
COCAvects = getDictVector(COCA)
for word in badWords:
  del COCA[word]

