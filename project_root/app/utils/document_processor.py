import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from .cleaner import clean_data
from .transformer import transform_data
from .vectorizer import create_word_vectors

nltk.download('punkt')
nltk.download('stopwords')

def process_document(file_path):
    with open(file_path, 'r') as file:
        data = file.read().replace('\n', ' ')

    cleaned_data = clean_data(data)
    transformed_data = transform_data(cleaned_data)
    word_vectors = create_word_vectors(transformed_data)

    return word_vectors

def process_documents(directory_path):
    documents = {}
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt") or filename.endswith(".pdf"):
            file_path = os.path.join(directory_path, filename)
            documents[filename] = process_document(file_path)

    return documents

def remove_stop_words(data):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(data)
    filtered_data = [w for w in word_tokens if not w in stop_words]

    return ' '.join(filtered_data)

def clean_data(data):
    data = data.lower()
    data = re.sub(r'\d+', '', data)
    data = re.sub(r'\W+', ' ', data)
    data = remove_stop_words(data)

    return data
