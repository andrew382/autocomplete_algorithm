"""Contains the AutocompleteProvider class and helper functions.
"""

import string
from autocomplete import candidate as cand

class AutocompleteProvider:
    """Provides autocomplete suggestions for word fragments. Suggestions are
    based off of previously provided passages typed by the user. 
    """

    def __init__(self):
        """Initalizes AutocompleteProvider object.
        """
        pass

    def getWords(self, fragment):
        """Returns list of candidates ordered by confidence.

        :param str fragment: The word fragment to be autocompleted.
        """
        pass

    def train(self, passage):
        """Trains the algorithm with the provided passage.

        :param str passage: Contains words that the autocomplete algorithm will
        use to train.
        """
        pass


def preprocess(passage):
    """Preprocesses a passage for training in the AutocompleteProvider class. 
    Returns a list of lowercase words without punctuation.

    :param str passage: The passage of words to be preprocessed.
    """
    return passage.translate(None, string.punctuation).lower().split()