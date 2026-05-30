import pandas as pd
import  re
vocab = {'refund', 'document' , 'due' , 'reminder', 'cancel' ,
 'code', 'password', 'today', 'delivery', 'cut', 'invitation', 'launch',
 'free', 'ordered', 'hir', 'ship', 'update', 'review', 'save', '%'}
 #20 words vocab

vocab = sorted(list(vocab))

token_ = {}
df = pd.read_csv('test_data_raw.csv')


def tokenize_and_vectorize(subject):
    vector = []
    token = []
    subject = subject.lower()
    subject = re.sub(r'[^%a-zA-Z0-9]', '', subject)
    for word in vocab:
        if str(word) in subject:
            token.append(word)
    for word in vocab:
        if word in token:
            vector.append(1)
        else:
            vector.append(-1)

    return token, vector

all_tokens = []
all_vectors = []

for subject in df['subject']:
    token, vector = tokenize_and_vectorize(subject)
    all_tokens.append(token)
    all_vectors.append(vector)

new_df = df

new_df['token'] = all_tokens
new_df['vector'] = all_vectors

new_df.to_csv('test_data.csv')
