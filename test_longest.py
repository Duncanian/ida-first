import unittest;
from longest import longest

class Test(unittest.TestCase):
    def test_longest_word(self):
        sentence = "This is Andela"
        self.assertEqual('Andela', longest(sentence))

    def test_one_word(self):
        sentence = "This"
        self.assertEqual("This", longest(sentence))