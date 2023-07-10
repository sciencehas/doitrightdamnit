```python
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

class Cleaner:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def clean_text(self, text):
        # Remove non-alphabetic characters
        text = re.sub(r'[^a-zA-Z]', ' ', text)

        # Tokenize the words
        word_tokens = word_tokenize(text)

        # Filter out the stop words
        filtered_text = [word for word in word_tokens if word not in self.stop_words]

        return ' '.join(filtered_text)
```