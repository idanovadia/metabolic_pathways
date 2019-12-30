import gensim.models.doc2vec as doc
from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec as d2v, TaggedDocument


# documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(common_texts)]
# model = Doc2Vec(documents, vector_size=5, window=2, min_count=1, workers=4)
# model
class Doc2Vec:

    def __init__(self, list_of_RW):
        self.list_of_RW = list_of_RW

    def Doc2Vec(self):
        documents = [TaggedDocument(doc.nodes, [i]) for i, doc in enumerate(self.list_of_RW)]
        model = d2v(documents, vector_size=4, window=2, min_count=1, workers=4)
        return model.docvecs
