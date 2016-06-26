from django.test import TestCase
from utilities import SimilarityMetrics

import numpy as np


class CosineSimilarityTestCase(TestCase):

    def test_cossim(self):
        """ Test Cosine Similarity Function """
        metrics = SimilarityMetrics()
        test1 = metrics.cosine_similarity(np.asarray([1,1]),np.asarray([-1,1]))
        np.testing.assert_almost_equal(test1,0.0)

        test2 = metrics.cosine_similarity(np.asarray([1,-1]),np.asarray([-1,1]))
        np.testing.assert_almost_equal(test2,-1.0)

        test3 = metrics.cosine_similarity(np.asarray([1,1]),np.asarray([1,1]))
        np.testing.assert_almost_equal(test3,1.0)

