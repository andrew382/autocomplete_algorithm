"""Contains the AutocompleteProvider class and helper functions.
"""

import string
from functools import reduce
from collections import namedtuple
from autocomplete import candidate as cand

class AutocompleteProvider:
    """Provides autocomplete suggestions for word fragments. Suggestions are
    based off of previously provided passages typed by the user. 
    """

    def __init__(self):
        """Initalizes AutocompleteProvider object.
        """
        self.memory = {}

    def getWords(self, fragment):
        """Returns list of candidates ordered by confidence.

        :param str fragment: The word fragment to be autocompleted.
        """
        fragment = fragment.translate(None, string.punctuation).lower()
        try:
            memory_node = get_bottom_node(fragment, self.memory)
        except KeyError:  # occurs when fragment has never been seen before
            return []
        candidate_list = get_candidates(fragment, memory_node.memory)
        if memory_node.confidence > 0:
            candidate_list.append(cand.Candidate(fragment, 
                                                 memory_node.confidence))
        return sorted(candidate_list, key=lambda x: x.confidence, reverse=True)

    def train(self, passage):
        """Trains the algorithm with the provided passage.

        :param str passage: Contains words that the autocomplete algorithm will
        use to train.
        """
        word_list = preprocess(passage)
        for word in word_list:
            self.memory = memorize(self.memory, word)


class MemoryNode:
    """Used by AutocompleteProvider to store the confidence and next memorizied
    letters of the key (a letter).
    """

    def __init__(self, memory=None, confidence=None):
        """Initalizes MemoryNode object.
        """
        self.memory = memory
        self.confidence = confidence

    def __eq__(self, other):
        """Determines if two instances are equal. Overrides the default 
        implementation.
        """
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False


def get_candidates(fragment, memory):
    candidate_list = []
    for letter, node in memory.iteritems():
        new_fragment = fragment + letter
        if node.confidence > 0:
            candidate_list.append(cand.Candidate(new_fragment, node.confidence))
        if node.memory:
            candidate_list += get_candidates(new_fragment, node.memory)
    return candidate_list


# TODO: consider having function return Candidate({}, 0) if KeyError is thrown.
def get_bottom_node(fragment, memory):
    """Goes down the nested dictionaries in memory in a path given by fragment.
    Returns the MemoryNode at the end of the path. Function throws KeyError if
    fragment is not recognized in the memory. 

    :param str fragment: word fragment that specifies the path.
    :param dict memory: memory dictionary that the word will be added to.
    """
    memory_node = memory[fragment[0]]
    for letter in fragment[1:]:
        memory_node = memory_node.memory[letter]
    return memory_node


def memorize(memory, word):
    """Adds a single word to memory.

    :param dict memory: memory dictionary that the word will be added to.
    :param str word: the word fragment to be added to memory.
    """
    letter = word[0]
    word = word[1:]
    memory_node = memory.get(letter, MemoryNode({}, 0))
    if word:
        memory_node.memory = memorize(memory_node.memory, word)
    else:
        memory_node.confidence += 1
    memory[letter] = memory_node
    return memory


def preprocess(passage):
    """Preprocesses a passage for training in the AutocompleteProvider class. 
    Returns a list of lowercase words without punctuation.

    :param str passage: The passage of words to be preprocessed.
    """
    return passage.translate(None, string.punctuation).lower().split()
