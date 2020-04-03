import gensim.models.doc2vec as doc
from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec as d2v, TaggedDocument


# documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(common_texts)]
# model = Doc2Vec(documents, vector_size=5, window=2, min_count=1, workers=4)
# model
class Doc2Vec:

    def __init__(self):
        self.list_of_RW = []

    def fit(self):
        documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(self.list_of_RW)]
        model = d2v(documents, vector_size=10, window=2, min_count=1, workers=4)
        return model.docvecs

    def transform(self, subGraphsList):
        for rwList in subGraphsList:
            tmp = []
            for graph in rwList:
                tmp = tmp + (list(graph.nodes))
            self.list_of_RW.append(tmp)
