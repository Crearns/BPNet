# _*_ coding: utf-8 _*_

from BPNet import NeuralNetwork
import numpy as np

nn = NeuralNetwork([2, 2, 1], 'tanh')
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])
nn.fit(x, y)
for i in [[0, 1], [1, 0], [1, 1]]:
    print(i, nn.predict(i))