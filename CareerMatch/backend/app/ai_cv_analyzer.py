import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class CVAnalyzer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')

    def rank_applicants(self, job_description, cvs):
        """
        job_description: string (opis posla)
        cvs: list of dicts [{"name":..., "email":..., "text":...}]
        return: list of dicts sa sličnostima
        """
        texts = [job_description] + [cv['text'] for cv in cvs]
        tfidf_matrix = self.vectorizer.fit_transform(texts)
        job_vec = tfidf_matrix[0]
        cv_vecs = tfidf_matrix[1:]
        similarities = cosine_similarity(job_vec, cv_vecs).flatten()
        ranked = []
        for i, cv in enumerate(cvs):
            ranked.append({
                'name': cv['name'],
                'email': cv['email'],
                'similarity': float(similarities[i])
            })
        ranked.sort(key=lambda x: x['similarity'], reverse=True)
        return ranked

# Primer upotrebe
if __name__ == "__main__":
    job_desc = "Python developer with experience in machine learning and NLP."
    cvs = [
        {"name": "Ana", "email": "ana@example.com", "text": "Experienced Python developer, worked on NLP projects."},
        {"name": "Marko", "email": "marko@example.com", "text": "Java developer, interested in AI."},
        {"name": "Jelena", "email": "jelena@example.com", "text": "Python and ML enthusiast, NLP background."}
    ]
    analyzer = CVAnalyzer()
    results = analyzer.rank_applicants(job_desc, cvs)
    for r in results:
        print(r)
