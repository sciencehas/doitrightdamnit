```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

class Vectorizer:

    def __init__(self):
        self.count_vectorizer = CountVectorizer()
        self.tfidf_vectorizer = TfidfVectorizer()

    def create_bag_of_words(self, corpus):
        return self.count_vectorizer.fit_transform(corpus)

    def create_tfidf(self, corpus):
        return self.tfidf_vectorizer.fit_transform(corpus)

    def get_feature_names(self):
        return self.count_vectorizer.get_feature_names()

    def get_idf(self):
        return self.tfidf_vectorizer.idf_

    def transform(self, corpus):
        return self.count_vectorizer.transform(corpus)

    def inverse_transform(self, bag):
        return self.count_vectorizer.inverse_transform(bag)
```