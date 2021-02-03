import numpy as np


class DeepLearning:

    @staticmethod
    def sigmoid(numpy_array):
        return 1 / (1 + np.exp(-numpy_array))

    @staticmethod
    def identity_function(numpy_array):
        return numpy_array
