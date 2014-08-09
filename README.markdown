TfIdf
====================================
Compute tf idf with idf and tfidf cache independently.

Usage
------------------------------------
```python
tfidf1 = TfIdf(documents, QuestionWithFitDegree.cache_dir)
tfidf1.idf_cache # access global Idf
tfidf_cache = tfidf1.generate_tfidf_cache()
```


License
------------------------------------
MIT. David Chen @ 17zuoye
