import pandas as pd
from scipy.stats import mode
from typing import Tuple
from sklearn.metrics import confusion_matrix
import seaborn as sns

class KNNClassifier:

    def __init__(self, k:int,test_split_ratio:float):
        self.k= k
        self.test_split_ratio = test_split_ratio

    @property
    def k_neighbors(self):
        return self.k

    @staticmethod
    def load_csv(path: str)->Tuple[pd.DataFrame, pd.Series]:
        dataset= pd.read_csv(path)
        dataset = dataset.sample(frac=1, random_state=42)
        x,y=dataset.iloc[:,:-1], dataset.iloc[:,-1]
        return x,y
    
    def train_test_split(self, features:pd.DataFrame,
                        labels:pd.Series):
        test_size= int(len(features)*self.test_split_ratio)
        train_size=len(features)-test_size
        assert len(features)==test_size+train_size, "Size mismatch!"

        self.x_train, self.y_train= features.iloc[:train_size,:],labels.iloc[:train_size]
        self.x_test, self.y_test= features.iloc[train_size:,:],labels.iloc[train_size:]

    def euclidean(self, element_of_x : pd.Series)->pd.Series :
        return ((self.x_train-element_of_x)**2).sum(axis=1).pow(0.5)

    def predict(self, x_test: pd.DataFrame):
        labels_pred=[]
        for i, row in x_test.iterrows():
            distances= self.euclidean(row)
            distances= pd.DataFrame(sorted(zip(distances, self.y_train)))
            label_pred = distances.iloc[:self.k,1].mode()
            labels_pred.append(label_pred)
        
        self.y_preds = pd.DataFrame(labels_pred).iloc[:,0]

    def accuracy(self) -> float:
        true_positive = (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) * 100
    
    def confusion_matrix(self):
        conf_matrix = confusion_matrix(self.y_test, self.y_preds)
        #sns.heatmap(conf_matrix, annot=True)
        return conf_matrix
    
    def plot_confusion_matrix(self):
        return self.confusion_matrix()
    #lapon plot_confusion_matrix, tesztnél confusion_matrix

    def best_k(self)->Tuple[int, float]:
        xc=-1.0
        res=-1
        a = self.k
        for i in range (1, 21):
            self.k=i
            self.predict(self.x_test)
            acc= self.accuracy()
            if (acc>xc):
                res=self.k
                xc= acc
                
        self.k=a 
        return res, round(xc,2)

