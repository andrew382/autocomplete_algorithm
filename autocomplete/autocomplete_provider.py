"""Contains the AutocompleteProvider class.
"""


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