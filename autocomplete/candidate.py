"""Contains the Candidate class.
"""

class Candidate:
    """Stores a candidate word and the confidence for autocomplete.
    """

    def __init__(self, word=None, confidence=None):
        """Initalizes candidate object.

        :param str word: Autocomplete candidate word.
        :param int confidence: Confidence of candidate word.
        """
        self.word = word
        self.confidence = confidence

    def getWord(self):
        """Returns the candidate word.
        """
        return self.word

    def getConfidence(self):
        """Returns the confidence of the candidate word.
        """
        return self.confidence