# -*- coding: utf-8 -*-

import os, sys
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)

import unittest
from tfidf import TfIdf

class TestFillBrokenWords(unittest.TestCase):

    def test_(self):
        pass


if __name__ == '__main__': unittest.main()
