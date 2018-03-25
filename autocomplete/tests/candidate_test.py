"""Contains unit tests for the Candidate class.
"""

import unittest
from autocomplete import candidate as cand


class TestCandidateNoInputs(unittest.TestCase):
	"""Tests the Candidate class methods when initialized with neither word nor
	confidence inputs.
	"""

	def setUp(self):
		"""Initializes a Candidate with no inputs.
		"""
		self.candidate = cand.Candidate()

	def test_candidate_getWord(self):
		"""Tests the getWord method.
		"""
		correct_answer = None
		output = self.candidate.getWord()
		self.assertEqual(output, correct_answer)

	def test_candidate_getConfidence(self):
		"""Tests the getConfidence method.
		"""
		correct_answer = None
		output = self.candidate.getConfidence()
		self.assertEqual(output, correct_answer)


class TestCandidateOnlyWord(unittest.TestCase):
	"""Tests the Candidate class methods when initialized with only a word 
	input. 
	"""

	def setUp(self):
		"""Initializes a Candidate with only a word input.
		"""
		input_word = 'aBc!@#123'  # contains upper/lower case, numbers, specials
		self.candidate = cand.Candidate(word=input_word)

	def test_candidate_getWord(self):
		"""Tests the getWord method.
		"""
		correct_answer = 'aBc!@#123'
		output = self.candidate.getWord()
		self.assertEqual(output, correct_answer)

	def test_candidate_getConfidence(self):
		"""Tests the getConfidence method.
		"""
		correct_answer = None
		output = self.candidate.getConfidence()
		self.assertEqual(output, correct_answer)


class TestCandidateOnlyConfidence(unittest.TestCase):
	"""Tests the Candidate class methods when initialized with only a confidence 
	input. 
	"""

	def setUp(self):
		"""Initializes a Candidate with only a confidence input.
		"""
		input_confidence = 10
		self.candidate = cand.Candidate(confidence=input_confidence)

	def test_candidate_getWord(self):
		"""Tests the getWord method.
		"""
		correct_answer = None
		output = self.candidate.getWord()
		self.assertEqual(output, correct_answer)

	def test_candidate_getConfidence(self):
		"""Tests the getConfidence method.
		"""
		correct_answer = 10
		output = self.candidate.getConfidence()
		self.assertEqual(output, correct_answer)


class TestCandidateWordAndConfidence(unittest.TestCase):
	"""Tests the Candidate class methods when initialized with both a word and
	confidence input. 
	"""

	def setUp(self):
		"""Initializes a Candidate with only a word and confidence input.
		"""
		input_word = 'aBc!@#123'
		input_confidence = 10
		self.candidate = cand.Candidate(word=input_word, 
										confidence=input_confidence)

	def test_candidate_getWord(self):
		"""Tests the getWord method.
		"""
		correct_answer = 'aBc!@#123'
		output = self.candidate.getWord()
		self.assertEqual(output, correct_answer)

	def test_candidate_getConfidence(self):
		"""Tests the getConfidence method.
		"""
		correct_answer = 10
		output = self.candidate.getConfidence()
		self.assertEqual(output, correct_answer)


if __name__ == '__main__':
    unittest.main()