from gensimModel import model

def main():
  masterList = {}
  masterList_temp = {}

  with open("data/words_219k_trimmed1.txt") as file, open("data/ScrabbleWords2019.txt") as file2:
    for line in file:
      (word, freq) = line.split()
      freq = int(freq)
      if freq > 300 and len(word) >= 4 and len(word) <= 10:
        masterList_temp[word] = freq

    for line in file2:
      s_word = line.lower().strip()
      if s_word in masterList_temp:
        masterList[s_word] = masterList_temp[s_word]

  for word in list(masterList.keys()):
    try:
      vect = model.get_vector(word)
    except KeyError:
      del masterList[word]

  with open("data/masterDict.txt", "w") as file:
    for word,freq in masterList.items():
      file.write(f'{word} {freq}\n', )


if __name__ == "__main__":
    main()
