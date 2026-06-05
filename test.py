import pickle
import pandas as pd
from train import Perceptron # the class needs to be imported
import ast # to convert strings into lists with df.read_csv()

#load the model
with open("ppn.pkl", "rb") as f:
    ppn = pickle.load(f)

df = pd.read_csv('training_data.csv')
new_df = df

#print(ppn.product(ast.literal_eval(df['vector'].iloc[178])))
#print(df[['sender', 'subject']].iloc[178])
for i in range(len(df)):
    vector = ast.literal_eval(df['vector'].iloc[i])
    if ppn.product(vector) <= 0: # decision is based on the dot product of inputs and weights
        mail_type = 'nosy'
        new_df.loc[i, 'result'] = mail_type
        #print('Email mail_type: ', mail_type , '>  Move to Trash')
    elif ppn.product(vector) <= .05:
        mail_type = 'normal'
        new_df.loc[i, 'result'] = mail_type
        #print('Email mail_type: ', mail_type, '>  Do nothing ')
    else:
        mail_type = 'clean'
        new_df.loc[i, 'result'] = mail_type
        #print('Email mail_type: ', mail_type, '>  Read it ASAP')


new_df.to_csv('train_result.csv')
