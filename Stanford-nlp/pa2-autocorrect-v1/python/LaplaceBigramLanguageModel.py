import math

class LaplaceBigramLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""

    self.words = {}
    self.pairs = {}
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """
    self.size = 0.0
    prev_word = ""
    for sentence in corpus.corpus: # iterate over sentences in the corpus
      for datum in sentence.data: # iterate over datums in the sentence
        word = datum.word # get the word
        if self.words.has_key(word):
          self.words[word] += 1.0
        else:
          self.words[word] = 1.0
        self.size += 1.0

        if prev_word:
          pair = (prev_word, word)
          if self.pairs.has_key(pair):
            self.pairs[pair] += 1.0
          else:
            self.pairs[pair] = 1.0

        prev_word = word

      prev_word = ""

  def probability(self, pair):
    return math.log( ((self.count_pair(pair) + 1.0)/(self.count(pair[0]) + self.size)))

  def count(self, word):
    if self.words.has_key(word):
      return self.words[word]
    return 0

  def count_pair(self, pair):
    if self.pairs.has_key(pair):
      return self.pairs[pair]
    return 0

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the
        sentence using your language model. Use whatever data you computed in train() here.
    """
    score = 0.0
    prev_word = ""
    for word in sentence:
      if prev_word:
        score += self.probability((prev_word, word))
      prev_word = word

    return score
