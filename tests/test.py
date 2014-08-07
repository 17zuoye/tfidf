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
        self.assertTrue(t.idf_cache['I'] < t.idf_cache['Your'])

        self.assertTrue(t.result[1]['I'] < t.result[1]['You'])
        self.assertTrue(t.result[1]['You'] < t.result[1]['hello'])
        self.assertTrue(t.result[1]['hello'] == t.result[1]['world'])



if __name__ == '__main__': unittest.main()
