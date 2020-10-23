import perceptron

x1 = 1
x2 = 0

test = perceptron.Perceptron(x1, x2)
print(test.AND())
print(test.XOR())
print(test.NAND())
print(test.OR())
