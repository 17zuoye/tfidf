TfIdf
====================================
[![Build Status](https://img.shields.io/travis/17zuoye/tfidf/master.svg?style=flat)](https://travis-ci.org/17zuoye/tfidf)
[![Coverage Status](https://coveralls.io/repos/17zuoye/tfidf/badge.svg)](https://coveralls.io/r/17zuoye/tfidf)
[![Health](https://landscape.io/github/17zuoye/tfidf/master/landscape.svg?style=flat)](https://landscape.io/github/17zuoye/tfidf/master)
[![Download](https://img.shields.io/pypi/dm/tfidf.svg?style=flat)](https://pypi.python.org/pypi/tfidf)
[![License](https://img.shields.io/pypi/l/tfidf.svg?style=flat)](https://pypi.python.org/pypi/tfidf)


Compute tf idf with idf and tfidf cache independently.

Usage
------------------------------------
```python
tfidf1 = TfIdf(documents, QuestionWithFitDegree.cache_dir)
tfidf1.idf_cache # access global Idf
```


License
------------------------------------
MIT. David Chen @ 17zuoye
