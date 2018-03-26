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
        passage = ',has.  ! punc#tion?@ here'
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


class TestMemorize(unittest.TestCase):
    """Tests the memorize function.
    """

    def setUp(self):
        self.abc_memory = {'a': auto.MemoryNode({'b':  # memory of the word abc
                                auto.MemoryNode({'c': 
                                auto.MemoryNode({}, 1)}, 0)}, 0)}

    def test_memorize_empty_memory(self):
        """Tests memorize function with an empty memory dictionary passed.
        """
        word = 'abc'
        output = auto.memorize({}, word)
        self.assertEqual(output, self.abc_memory)

    def test_memorize_non_empty_memory(self):
        """Tests memorize function when memory already exists. 
        """
        word = 'adc' 
        correct_answer = {'a': auto.MemoryNode({
                                'b': auto.MemoryNode({'c': 
                                    auto.MemoryNode({}, 1)}, 0),
                                'd': auto.MemoryNode({'c': 
                                    auto.MemoryNode({}, 1)}, 0)
                                }, 0)}
        output = auto.memorize(self.abc_memory, word)
        self.assertEqual(output, correct_answer)

    def test_memorize_same_word(self):
        """Tests memorize function when a word is passed that is already in the 
        memory.
        """
        word = 'abc'
        correct_answer = {'a': auto.MemoryNode({'b': 
                               auto.MemoryNode({'c': 
                               auto.MemoryNode({}, 2)}, 0)}, 0)}
        output = auto.memorize(self.abc_memory, word)
        self.assertEqual(output, correct_answer)

    def test_memorize_same_prefix(self):
        """Tests memorize function when a word is passed that is a prefix of a 
        word already in the memory.
        """
        word = 'ab'
        correct_answer = {'a': auto.MemoryNode({'b': 
                               auto.MemoryNode({'c': 
                               auto.MemoryNode({}, 1)}, 1)}, 0)}
        output = auto.memorize(self.abc_memory, word)
        self.assertEqual(output, correct_answer)


class TestGetBottomNode(unittest.TestCase):
    """Tests the get_bottom_node function.
    """

    def setUp(self):
        self.abc_memory = {'a': auto.MemoryNode({'b':  # memory of the word abc
                                auto.MemoryNode({'c': 
                                auto.MemoryNode({}, 1)}, 0)}, 0)}

    def test_get_bottom_node_single_char(self):
        """Input fragement is a single character. 
        """
        fragment = 'a'
        correct_answer = auto.MemoryNode({'b':  
                                auto.MemoryNode({'c': 
                                auto.MemoryNode({}, 1)}, 0)}, 0)
        output = auto.get_bottom_node(fragment, self.abc_memory)
        self.assertEqual(output, correct_answer)

    def test_get_bottom_node_bottom(self):
        """Input fragement should return a node at the bottom of memory. 
        """
        fragment = 'abc'
        correct_answer = auto.MemoryNode({}, 1)
        output = auto.get_bottom_node(fragment, self.abc_memory)
        self.assertEqual(output, correct_answer)

    def test_get_bottom_node_branches(self):
        """Input memory has branches and function must choose correct branch. 
        """    
        memory = {'a': auto.MemoryNode({
                    'b': auto.MemoryNode({'c': auto.MemoryNode({}, 1)}, 0), 
                    'd': auto.MemoryNode({'e': auto.MemoryNode({}, 2)}, 0)}, 0)}
        fragment = 'ade'
        correct_answer = auto.MemoryNode({}, 2)
        output = auto.get_bottom_node(fragment, memory)
        self.assertEqual(output, correct_answer)

    def test_get_bottom_node_key_error(self):
        """If the fragment does not lead to a node, the function should throw a
        KeyError.
        """
        fragment = 'def'
        try:
            output = auto.get_bottom_node(fragment, self.abc_memory)
            passes_test = False
        except KeyError: 
            passes_test = True
        self.assertTrue(passes_test)
        

class TestAutocompleteProvider(unittest.TestCase):
    """Tests the methods of the AutocompleteProvider class.
    """

    def test_train_no_memory(self):
        """Tests the train method when there are no previous memories.
        """
        pass

    def test_getWords_example(self):
        """Tests getWords method on the given example.
        """
        passage = 'The third thing that I need to tell you is that this thing \
        does not think thoroughly.'
        alg = auto.AutocompleteProvider()
        alg.train(passage)
        candidates = alg.getWords('thi')
        for c in candidates:
            print c.word
            print c.confidence


if __name__ == '__main__':
    unittest.main()