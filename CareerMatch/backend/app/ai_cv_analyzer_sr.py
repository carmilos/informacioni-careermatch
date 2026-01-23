# Primer srpskih stop reči (možeš proširiti listu po potrebi)
srpski_stop_reci = [
    'i', 'u', 'na', 'je', 'da', 'se', 'za', 'od', 'do', 'sa', 'po', 'o', 'koji', 'koja', 'koje',
    'a', 'ali', 'ili', 'pa', 'te', 'su', 'sam', 'si', 'smo', 'ste', 'su', 'biti', 'bio', 'bila',
    'bilo', 'bili', 'bile', 'će', 'ne', 'nije', 'jesam', 'jesi', 'jesmo', 'jeste', 'jesu',
    'moj', 'tvoj', 'svoj', 'njegov', 'njen', 'njihov', 'nas', 'vas', 'njih', 'mi', 'ti', 'vi', 'oni',
    'one', 'ono', 'ja', 'on', 'ona', 'ono', 'ko', 'što', 'što', 'kako', 'gde', 'kad', 'kada', 'zašto',
    'čiji', 'čija', 'čije', 'čiji', 'čime', 'čemu', 'čega', 'čega', 'čega', 'čega', 'čega', 'čega',
]

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class CVAnalyzer:
    def __init__(self, stop_words=None):
        self.vectorizer = TfidfVectorizer(stop_words=stop_words)

    def rank_applicants(self, job_description, cvs):
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

# Primer upotrebe za srpski tekst
def test_srpski():
    job_desc = "Python programer sa iskustvom u mašinskom učenju i NLP-u."
    cvs = [
        {"name": "Ana", "email": "ana@example.com", "text": "Iskusan Python programer, radio na NLP projektima."},
        {"name": "Marko", "email": "marko@example.com", "text": "Java programer, zainteresovan za veštačku inteligenciju."},
        {"name": "Jelena", "email": "jelena@example.com", "text": "Python i ML entuzijasta, NLP iskustvo."}
    ]
    analyzer = CVAnalyzer(stop_words=srpski_stop_reci)
    results = analyzer.rank_applicants(job_desc, cvs)
    for r in results:
        print(r)

if __name__ == "__main__":
    test_srpski()
