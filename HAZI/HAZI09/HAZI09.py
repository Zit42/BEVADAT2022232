import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.datasets import load_digits
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix

class KMeansOnDigits:

    def __init__(self, n_clusters, random_state):
        self.n_clusters = n_clusters
        self.random_state = random_state

    def load_dataset(self):
        self.digits = load_digits()

    def predict(self):
        self.model = KMeans(n_clusters=self.n_clusters, random_state=self.random_state)
        self.clusters = self.model.fit_predict(self.digits.data)

    def get_labels(self):
        res = np.zeros_like(self.clusters)
        for c in range(self.n_clusters):
            mask = (self.clusters == c)
            xc = np.argmax(np.bincount(self.digits.target[mask]))
            res[mask] = xc
        self.labels = res

    def calc_accuracy(self):
        xc = np.mean(self.digits.target == self.labels)
        self.accuracy = round(xc, 2)

    def confusion_matrix(self):
        self.mat = confusion_matrix(self.digits.target, self.labels)