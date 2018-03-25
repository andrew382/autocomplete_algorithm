"""Contains unit tests for the AutocompleteProvider class.
"""

import unittest
from autocomplete import autocomplete_provider as auto

class TestPreprocess(unittest.TestCase):
    """Test the preprocess function.
    """

    def test_preprocess_numbers(self):
        """Passage contains numbers, but no puncuation or uppercase letters.
        """
        passage = '0has num9ers here, 4'
        correct_answer = ['0has', 'num9ers', 'here', '4']
        output = auto.preprocess(passage)

    def test_preprocess_punctuation(self):
        """Passage contains punctuation.
        """
        passage = ',has. ! punc#tion?@ here'
        correct_answer = ['has', 'punction', 'here']
        output = auto.preprocess(passage)

    def test_preprocess_capitals(self):
        """Passage contains capital letters.
        """
        passage = 'String hAs capitalS'
        correct_answer = ['string', 'has', 'capitals']
        output = auto.preprocess(passage)

    def test_preprocess_punctuation_capitals_numbers(self):
        """Passage contains puntuation, capital letters, and numbers.
        """
        passage = 'Str#ing h1As, 12capitalS!!!, 0123'
        correct_answer = ['string', 'h1as', '12capitals', '0123']
        output = auto.preprocess(passage)


if __name__ == '__main__':
    unittest.main()