"""Contains unit tests for the AutocompleteProvider class.
"""

import unittest
from autocomplete import candidate as cand
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
        

class TestGetCandidates(unittest.TestCase):
    """Tests the get_candidates function.
    """

    def test_get_candidates_none(self):
        """No good candidates in memory.
        """
        memory = {'a': auto.MemoryNode({'b':
                       auto.MemoryNode({'c': 
                       auto.MemoryNode({}, 0)}, 0)}, 0)}
        fragment = 'a'
        correct_answer = []
        output = auto.get_candidates(fragment, memory)
        self.assertEqual(output, correct_answer)

    def test_get_candidates_one_good_bottom(self):
        """One good candidate at bottom level of memmory.
        """
        memory = {'a': auto.MemoryNode({'b':
                       auto.MemoryNode({'c': 
                       auto.MemoryNode({}, 2)}, 0)}, 0)}
        fragment = 'prefix'
        correct_answer = [cand.Candidate('prefixabc', 2)]
        output = auto.get_candidates(fragment, memory)
        self.assertEqual(output, correct_answer)

    def test_get_candidates_two_good_diff_lvl(self):
        """Two good candidates at different levels of memmory.
        """
        memory = {'a': auto.MemoryNode({'b':
                       auto.MemoryNode({'c': 
                       auto.MemoryNode({}, 1)}, 0)}, 2)}
        fragment = 'prefix'
        correct_answer = [cand.Candidate('prefixa', 2), 
                          cand.Candidate('prefixabc', 1)]
        output = auto.get_candidates(fragment, memory)
        self.assertEqual(output, correct_answer)

    def test_get_candidates_diff_branches(self):
        """Two good candidates down different branches of memmory.
        """
        memory = {'a': auto.MemoryNode({'b': auto.MemoryNode({'c': 
                                             auto.MemoryNode({}, 1)}, 0),
                                        'd': auto.MemoryNode({'e': 
                                             auto.MemoryNode({}, 3)}, 0)}, 0)}
        fragment = 'prefix'
        correct_answer = [cand.Candidate('prefixabc', 1), 
                          cand.Candidate('prefixade', 3)]
        output = auto.get_candidates(fragment, memory)
        self.assertEqual(output, correct_answer)


class TestAutocompleteProviderTrain(unittest.TestCase):
    """Tests train method of the AutocompleteProvider class.
    """

    def test_train_no_memory(self):
        """Tests the train method when there are no previous memories.
        """
        passage = 'Abc d-ef'  # contains uppercase and special characters
        correct_answer = {'a': auto.MemoryNode({'b':
                               auto.MemoryNode({'c': 
                               auto.MemoryNode({}, 1)}, 0)}, 0),
                          'd': auto.MemoryNode({'e':
                               auto.MemoryNode({'f': 
                               auto.MemoryNode({}, 1)}, 0)}, 0)}
        algorithm = auto.AutocompleteProvider()
        algorithm.train(passage)
        self.assertEqual(algorithm.memory, correct_answer)

    def test_train_has_memory(self):
        """Test the train method when there are previous memories.
        """
        passage = 'ab abc abd'
        memory = {'a': auto.MemoryNode({'b': 
                       auto.MemoryNode({'c': 
                       auto.MemoryNode({}, 1)}, 0)}, 0)}
        correct_answer = {'a': auto.MemoryNode({'b': 
                               auto.MemoryNode({'c': auto.MemoryNode({}, 2),
                                                'd': auto.MemoryNode({}, 1)}, 
                                                1)}, 0)}
        algorithm = auto.AutocompleteProvider()
        algorithm.memory = memory
        algorithm.train(passage)
        self.assertEqual(algorithm.memory, correct_answer)


class TestAutocompleteProviderGetWords(unittest.TestCase):
    """Tests getWords method of the AutocompleteProvider class.
    """

    def test_getWords_no_candidates(self):
        """No good candidates in memory for passed fragment.
        """
        memory = {'a': auto.MemoryNode({'b':
                       auto.MemoryNode({'c': 
                       auto.MemoryNode({}, 1)}, 0)}, 0)}
        fragment = 'ad'
        correct_answer = []
        alg = auto.AutocompleteProvider()
        alg.memory = memory
        output = alg.getWords(fragment)
        self.assertEqual(output, correct_answer)

    def test_getWords_different_branches(self):
        """Two good candidates in different branches. 
        """
        memory = {'a': auto.MemoryNode({
                        'b': auto.MemoryNode({'c': auto.MemoryNode({}, 1)}, 0),
                        'd': auto.MemoryNode({'e':
                                auto.MemoryNode({'f': auto.MemoryNode({}, 2)}, 
                        0)}, 0)}, 0),}
        fragment = 'a'
        correct_answer = [cand.Candidate('adef', 2), cand.Candidate('abc', 1)]
        alg = auto.AutocompleteProvider()
        alg.memory = memory
        output = alg.getWords(fragment)
        self.assertEqual(output, correct_answer)

    def test_getWords_not_all_good_candidates(self):
        """Given the fragment and memory, getWords should not return every 
        candidate with a postive confidence in memory.
        """
        memory = {'a': auto.MemoryNode({'b':
                       auto.MemoryNode({'c': 
                       auto.MemoryNode({}, 1)}, 0)}, 1)}
        fragment = 'aB'  # contains uppercase
        correct_answer = [cand.Candidate('abc', 1)]
        alg = auto.AutocompleteProvider()
        alg.memory = memory
        output = alg.getWords(fragment)
        self.assertEqual(output, correct_answer)


class TestAutocompleteProviderIntegrationTests(unittest.TestCase):
    """Tests AutocompleteProvider methods when used together.
    """

    def test_getWords_example(self):
        """Tests AutocompleteProvider on the given example.
        """
        passage = 'The third thing that I need to tell you is that this thing \
        does not think thoroughly.'
        alg = auto.AutocompleteProvider()
        alg.train(passage)
        fragment1 = 'thi'
        correct_answer1 = [cand.Candidate('thing', 2),
                           cand.Candidate('this', 1),
                           cand.Candidate('third', 1),
                           cand.Candidate('think', 1)]
        fragment2 = 'nee'     
        correct_answer2 = [cand.Candidate('need', 1)]
        fragment3 = 'th'
        correct_answer3 = [cand.Candidate('thing', 2),
                           cand.Candidate('that', 2),
                           cand.Candidate('this', 1),
                           cand.Candidate('third', 1),
                           cand.Candidate('think', 1),
                           cand.Candidate('the', 1),
                           cand.Candidate('thoroughly', 1)]    
        output1 = alg.getWords(fragment1)
        output2 = alg.getWords(fragment2)
        output3 = alg.getWords(fragment3)
        self.assertEqual(output1, correct_answer1)
        self.assertEqual(output2, correct_answer2)
        self.assertEqual(output3, correct_answer3)

    def test_getWords_train_twice(self):
        """Tests AutocompleteProvider when trained twice.
        """
        passage1 = 'This is the fIrst passage.'
        passage2 = 'here is the second passage that works. The thing pass!!!'
        alg = auto.AutocompleteProvider()
        alg.train(passage1)
        alg.train(passage2)
        fragment1 = 'i'
        correct_answer1 = [cand.Candidate('is', 2)]
        fragment2 = 'th'
        correct_answer2 = [cand.Candidate('the', 3),
                           cand.Candidate('this', 1),
                           cand.Candidate('thing', 1),
                           cand.Candidate('that', 1)]
        fragment3 = 'FIRST'
        correct_answer3 = [cand.Candidate('first', 1)]   
        fragment4 = 'pass'                       
        correct_answer4 = [cand.Candidate('passage', 2),
                           cand.Candidate('pass', 1)]    
        output1 = alg.getWords(fragment1)
        output2 = alg.getWords(fragment2)
        output3 = alg.getWords(fragment3)
        output4 = alg.getWords(fragment4)
        self.assertEqual(output1, correct_answer1)
        self.assertEqual(output2, correct_answer2)
        self.assertEqual(output3, correct_answer3)
        self.assertEqual(output4, correct_answer4)


if __name__ == '__main__':
    unittest.main()