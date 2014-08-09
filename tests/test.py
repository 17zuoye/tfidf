# -*- coding: utf-8 -*-

import os, sys
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)
os.system("rm -f *.cPickle")

import unittest
from tfidf import TfIdf

class TestTfIdf(unittest.TestCase):

    def setUp(self):
        self.data = [
            [1, {"hello": 1, "world": 1, "I": 1, "You": 1}],
            [2, {"ruby": 1, "python": 1, "I": 1, "choose": 1}],
            [3, {"food": 1, "drink": 1, "I": 1, "You": 1}],
            [4, {"mac": 1, "win": 1, "linux": 1, }],
        ]

    def test_tfidf(self):
        t = TfIdf(self.data, root_dir)
        self.assertTrue(t.idf_cache['I'] < t.idf_cache['hello'])
        self.assertTrue(t.idf_cache['I'] < t.idf_cache['You'])
        self.assertTrue(t.idf_cache['I'] < t.idf_cache['not exist feature'], "test default idf_default_val")

        tfidf_cache = t.generate_tfidf_cache()
        self.assertTrue(tfidf_cache[1]['I'] < tfidf_cache[1]['You'])
        self.assertTrue(tfidf_cache[1]['You'] < tfidf_cache[1]['hello'])
        self.assertTrue(tfidf_cache[1]['hello'] == tfidf_cache[1]['world'])



if __name__ == '__main__': unittest.main()
