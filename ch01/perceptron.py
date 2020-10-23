import pandas as pd
import numpy as np


class Perceptron:
    """
    Logical operation implementation in Perceptron
    """

    def __init__(self, x1, x2):
        """

        Parameters
        ----------
        x1 : float
         input signal
        x2 : float
         input signal
        """
        self.x1 = x1
        self.x2 = x2
        self.x = np.array([x1, x2])

    def AND(self, dx1=0, dx2=0):
        """
        AND arithmetic implementation

        Returns
        -------
        self.logical_operation : bool
            Returns the judgment result for the input signal
        """
        w = np.array([0.5, 0.5])
        b = -0.7
        return self.logical_operation(w, b)

    def OR(self):
        """
        OR arithmetic implementation

        Returns
        -------
        self.logical_operation : bool
            Returns the judgment result for the input signal
        """
        w = np.array([0.5, 0.5])
        b = -0.2
        return self.logical_operation(w, b)

    def NAND(self):
        """
        NOT AND arithmetic implementation

        Returns
        -------
        self.logical_operation : bool
            Returns the judgment result for the input signal
        """
        w = np.array([-0.5, -0.5])
        b = 0.7
        return self.logical_operation(w, b)

    def XOR(self):
        """
        NOT OR arithmetic implementation
        
        Returns
        -------
        self.AND(self.NAND(), self.OR()) : bool
            Returns NOT OR arithmetic implementation
        """
        return self.AND(self.NAND(), self.OR())

    def logical_operation(self, weight, bias):
        """

        Parameters
        ----------
        weight : ndarray
            numpy array
        bias : float
            bias

        Returns
        -------
        bool
        """
        temp = np.sum(self.x * weight) + bias
        if temp <= 0:
            return 0
        else:
            return 1
