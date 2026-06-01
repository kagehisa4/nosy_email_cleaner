import pickle
import pandas as pd
from train import Perceptron # the class needs to be imported
import ast # to convert strings into lists with df.read_csv()

#load the model
with open("ppn.pkl", "rb") as f:
    ppn = pickle.load(f)

df = pd.read_csv('test_data.csv')

vector = ast.literal_eval(df['vector'].iloc[71]) # this gives a list
print(str(df[['sender', 'subject', 'token']].iloc[71]))

if ppn.product(vector) <= 0: # decision is based on the dot product of inputs and weights
    type = 'nosy'
    print('Email type: ', type , '>  Move to Trash')
elif ppn.product(vector) <= .05:
    type = 'normal'
    print('Email type: ', type, '>  Do nothing ')
else:
    type = 'clean'
    print('Email type: ', type, '>  Read it ASAP')
