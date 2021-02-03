import perceptron
import numpy as np
from deep_learning import DeepLearning
import
x1 = 1
x2 = 0

test = perceptron.Perceptron(x1, x2)
print(test.AND())
print(test.XOR())
print(test.NAND())
print(test.OR())

x = np.array([1, 2])
print(x.shape)
w = np.array([[1, 3, 5], [2, 4, 5]])
print(w.shape)
print(np.dot(x, w))

X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.6], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])
array_shapes = (W1.shape, X.shape, B1.shape)
A1 = np.dot(X, W1) + B1

deep_learning = DeepLearning()
Z1 = deep_learning.sigmoid(A1)
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])
A2 = np.dot(Z1, W2) + B2
Z2 = deep_learning.sigmoid(A2)
W3 = np.array([[0.1, 0.4], [0.2, 0.4]])
B3 = np.array([[0.1, 0.2]])

A3 = np.dot(Z2, W3) + B3
Y = deep_learning.identity_function(A3)


def init_network():
    network = {'W1': np.array([[0.1, 0.3, 0.5], [0.3, 0.4]]), 'b1': np.array([0.1, 0.3, 0.2]),
               'W2': np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]]), 'b2': np.array([0.1, 0.2]),
               'W3': np.array([[0.1, 0.3], [0.2, 0.4]]), 'b3': np.array([0.1, 0.2])}
    return network


def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = np.dot(x, W1) + b1
    z1 = DeepLearning().sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = DeepLearning().sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = DeepLearning().identity_function(a3)

    return y
