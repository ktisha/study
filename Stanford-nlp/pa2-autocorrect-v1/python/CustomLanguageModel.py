import math

class CustomLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""

    self.words = {}
    self.pairs = {}
    self.train(corpus)
    self.frequences = {}

    for item in self.words.values():
      if self.frequences.has_key(item):
        self.frequences[item] += 1.
      else:
        self.frequences[item] = 1.

    frequences_values = self.frequences.keys()
    frequences_values.sort()

    self.max = int (frequences_values[len(frequences_values) - 1])

    for i in xrange(1, 10):
      if not self.frequences.has_key(i):
        next = self.find_next(i)
        freq = self.frequences[next]
        self.frequences[i] = (self.frequences[i - 1] + freq) /2

    for i in xrange(10, self.max + 2):
      self.frequences[i] = self.frequences[i-1]/2

  def find_next(self, i):
    while not self.frequences.has_key(i):
      if i >= self.max:
        return self.max
      i += 1
    return i

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
    word = pair[1]
    word_count = self.count(word)
    if word_count > 0:
      freq = self.frequences[word_count + 1]
      return (word_count + 1) * freq/ self.frequences[word_count]
    else:
      return self.frequences[1]/self.size

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
        score += math.log(self.probability((prev_word, word)))
      prev_word = word

    return score
