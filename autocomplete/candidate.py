"""Contains the Candidate class.
"""

class Candidate:
    """Stores a candidate word and the confidence for autocomplete.
    """

    def __init__(self, word=None, confidence=None):
        """Initalizes Candidate object.

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

    def __eq__(self, other):
        """Determines if two instances are equal. Overrides the default 
        implementation.
        """
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __str__(self):
        return self.word + ' (' + str(self.confidence) + ')'

    def __repr__(self):
        return str(self)
        