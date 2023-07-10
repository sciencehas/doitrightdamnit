from sklearn.metrics.pairwise import cosine_similarity
from .vectorizer import Vectorizer
from .document_processor import DocumentProcessor

class SimilarityAnalyzer:
    def __init__(self):
        self.vectorizer = Vectorizer()
        self.doc_processor = DocumentProcessor()

    def calculate_similarity(self, documents):
        vectors = self.vectorizer.create_vectors(documents)
        similarity_matrix = cosine_similarity(vectors)
        return similarity_matrix

    def analyze_similarity(self, documents):
        similarity_matrix = self.calculate_similarity(documents)
        similar_documents = self.find_similar_documents(similarity_matrix)
        return similar_documents

    def find_similar_documents(self, similarity_matrix, threshold=0.8):
        similar_documents = []
        for i in range(len(similarity_matrix)):
            for j in range(i+1, len(similarity_matrix)):
                if similarity_matrix[i][j] > threshold:
                    similar_documents.append((i, j))
        return similar_documents

    def get_similar_content(self, documents):
        similar_documents = self.analyze_similarity(documents)
        similar_content = []
        for doc1, doc2 in similar_documents:
            similar_sentences = self.doc_processor.get_similar_sentences(documents[doc1], documents[doc2])
            similar_content.append((documents[doc1], documents[doc2], similar_sentences))
        return similar_content
