import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import sklearn.datasets
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix

class KMeansOnDigits:

    def __init__(self, n_clusters, random_state):
        self.n_clusters = n_clusters
        self.random_state = random_state

    def load_dataset(self):
        self.digits = sklearn.datasets.load_digits()

    def predict(self):
        model = KMeans(n_clusters=self.n_clusters, random_state=self.random_state)
        self.clusters = model.fit(self.digits.data)

    def get_labels(self):
        res = np.zeros_like(self.clusters)
        for c in range(10): #0-9
            mask = (self.clusters == c)
            xc = np.bincount(self.digits.target[mask]).argmax()
            res[mask] = xc
        self.labels = res

    def calc_accuracy(self):
        xc = np.mean(self.digits.target == self.labels)
        self.accuracy = round(xc, 2)

    def confusion_matrix(self):
        self.mat = confusion_matrix(self.digits.target, self.labels)