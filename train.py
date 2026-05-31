#train a perceptron
import numpy as np
import pandas as pd
import ast
import matplotlib.pyplot as plt
import pickle
class Perceptron(object):
    def __init__(self, lg_rate, n_iter):
        self.lg_rate = lg_rate
        self.n_iter = n_iter

    def fit(self, X, y):
        self.w_ = np.zeros(1+ X.shape[1]) # Initilize zero weights matrix
        self.error_ = []

        for _ in range(self.n_iter):
            error = 0
            for xi in range (len(X)):
                update = self.lg_rate * (y[xi] - self.predict(X[xi]))
                self.w_[0] += update
                self.w_[1:] += update * X[xi, :]
                error += update
            self.error_.append(error)
        return  self.w_, self.error_

    def product(self, X):
        return np.dot(self.w_[1:], X) + self.w_[0]

    def predict(self, X):
        if self.product(X) > 0:
            return 1
        else:
            return -1


df = pd.read_csv('training_data.csv')

#generate input and traget arrays from csv
# csv returns strings for lists: so we use 'ast'

ip_vect = []
target = []

for i in range(len(df)):
    target.append(int(df['label'].iloc[i])) # returns data type too > use int()
    vector = ast.literal_eval(df['vector'].iloc[i]) # ast converts string to literals
    ip_vect.append(vector)

X = np.array(ip_vect)
y = target
ppn = Perceptron(lg_rate = .01, n_iter = 10)

ppn.fit(X,y)


# save the model using pickle

with open("ppn.pkl", "wb") as f:
    pickle.dump(ppn,f)
