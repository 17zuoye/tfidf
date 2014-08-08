# -*- coding: utf-8 -*-

import math
from etl_utils import process_notifier, cpickle_cache, cached_property
from collections import defaultdict

class TfIdf():
    def __init__(self, documents_or_func, cache_dir):
        """
        1. input is [ [item_id, {feature1:count1, feature2: count2, ...}], ... ]
        2. onput is [ [item_id, {feature1:rate1,  feature2: rate2,  ...}], ... ]
        """
        self.documents_or_func = documents_or_func
        self.cache_dir = cache_dir

        self.idf_default_val = sum(self.idf_cache.values()) / float(len(self.idf_cache))
        # Always load idf cache, and it's really small.
        self.idf_cache = IdfResult(lambda : self.idf_default_val, self.idf_cache)

    @cached_property
    def documents(self):
        documents = self.documents_or_func
        if '__call__' in dir(documents):
            documents = documents()
        assert len(documents), u"Documents should not be none."
        return documents

    @cached_property
    def doc_list(self):
        return [d1[1] for d1 in self.documents]

    def tf(self, word1, doc1, uniq_features_count1):
        return float(doc1[word1]) / uniq_features_count1

    @cached_property
    def idf_cache(self):
        def func():
            feature_in_doc_to_count = defaultdict(int)
            for features in self.doc_list:
                for feature1 in features:
                    feature_in_doc_to_count[feature1] += 1

            idf_result = IdfResult()
            all_num = float(len(self.doc_list))

            for feature1, count1 in feature_in_doc_to_count.iteritems():
                idf_result[feature1] = math.log( all_num / count1 )

            return idf_result

        return cpickle_cache(self.cache_dir + '/idf.cPickle', func)


    def tfidf(self, word1, doc1, uniq_features_count1):
        idf_value = self.idf_cache[word1]
        score = self.tf(word1, doc1, uniq_features_count1) * idf_value
        return score

    def tfidf_in_a_doc(self, doc1):
        doc1 = dict(doc1)
        uniq_features_count = sum([doc1[key] for key in doc1])
        return {w1: self.tfidf(w1, doc1, uniq_features_count) for w1 in doc1}

    def generate_tfidf_cache(self):
        def func():
            result = TfIdfResult()
            for item1 in process_notifier(self.documents):
                id1, doc1 = item1
                result[id1] = self.tfidf_in_a_doc(doc1)
            return result
        return cpickle_cache(self.cache_dir + '/tfidf.cPickle', func)

class IdfResult(defaultdict):
    def inspect(self):
        for word1, freq1 in sorted(self.iteritems(), key=lambda i1: -i1[1]):
            print word1, freq1

class TfIdfResult(dict):
    def inspect(self, doc_func=None):
        for item_id1, freq1 in self.iteritems():
            print
            print "="*80
            if doc_func:
                print doc_func(item_id1)
            else:
                print item_id1
            print sorted(freq1.iteritems(), key=lambda i1: -i1[1])
