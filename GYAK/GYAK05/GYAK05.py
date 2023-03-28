import numpy as np
from scipy.stats import mode
from typing import Tuple
from sklearn.metrics import confusion_matrix
import seaborn as sns

class KNNClassifier:
    
    def __init__(self, k:int,test_split_ratio:float):
        self.k= k
        self.test_split_ratio = test_split_ratio

    
        