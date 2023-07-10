```python
from sentence_transformers import SentenceTransformer

class Transformer:
    def __init__(self):
        self.model = SentenceTransformer('stsb-mpnet-base-v2')

    def transform(self, sentences):
        return self.model.encode(sentences)
```