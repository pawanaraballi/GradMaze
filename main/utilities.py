import numpy as np

class SimilarityMetrics():

    def cosine_similarity(self,vectA,vectB):
        return np.sum(np.multiply(vectA,vectB))/(np.linalg.norm(vectA)*np.linalg.norm(vectB))


if __name__ == "__main__":

    metrics = SimilarityMetrics()
    vectA = np.array([1,1,0])
    vectB = np.array([1,0,1])
    score = metrics.cosine_similarity(vectA,vectB)
    print(score)