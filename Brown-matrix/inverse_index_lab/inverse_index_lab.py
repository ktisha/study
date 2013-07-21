from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0, len(review_options)-1)]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    """
    :type strlist: list of str

    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    my_map = {}
    index = 0

    for string in strlist:
        for word in string.split(" "):
            if word in my_map:
                my_map[word].add(index)
            else:
                my_map[word] = {index,}
        index += 1
    return my_map

f = open("stories_small.txt")
index = makeInverseIndex(f.readlines())

## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    result = set()
    for word in query:
        if word in inverseIndex:
            result = result.union(inverseIndex[word])
    return result

print(orSearch(index, ["four", "prep"]))

## Task 6
def andSearch(inverseIndex, query):
    """
    :type inverseIndex: dict

    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    result = set()
    for entry in inverseIndex.items():
        result = result.union(entry[1])

    for word in query:
        if word in inverseIndex:
            result = result.intersection(inverseIndex[word])
    return result
