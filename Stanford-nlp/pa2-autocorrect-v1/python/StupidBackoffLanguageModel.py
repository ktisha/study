import math
from LaplaceBigramLanguageModel import LaplaceBigramLanguageModel

class StupidBackoffLanguageModel(LaplaceBigramLanguageModel):

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    LaplaceBigramLanguageModel.__init__(self, corpus)

  def probability(self, pair):
    self_count_pair = self.count_pair(pair)
    if self_count_pair > 0:
      return math.log((self_count_pair /self.count(pair[0])))
    else:
      count = 0.4 * self.count_smoothed(pair[1])
      return math.log(count)

  def count_smoothed(self, word):
    if self.words.has_key(word):
      word_count = self.words[word]
      my_len = len(self.words) + self.size
      prob = (word_count + 1.0) / my_len
      return prob
    else:
      return 1.0/self.size
