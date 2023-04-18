#%load_ext autoreload
#%autoreload 2

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split


class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        self.epochs= epochs
        self.lr= lr

    def fit(self, X: np.array, y: np.array):
    # Building the model
        self.m = 0
        self.c = 0

        n = float(len(X))  # Number of elements in X

        # Performing Gradient Descent
        losses = []
        for i in range(self.epochs):
            y_pred = self.m*X + self.c  # The current predicted value of Y

            residuals = y_pred - y
            loss = np.sum(residuals ** 2)
            losses.append(loss)
            D_m = (-2/n) * sum(X * residuals)  # Derivative wrt m
            D_c = (-2/n) * sum(residuals)  # Derivative wrt c
            self.m = self.m + self.lr * D_m  # Update m
            self.c = self.c + self.lr * D_c  # Update c
        return losses

    def predict(self, X):
        pred = []
        for X_element in X:
            y_pred = self.m*X_element + self.c
            pred.append(y_pred)

        return self.m*X + self.c




