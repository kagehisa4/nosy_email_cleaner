import pandas as pd
import  re
vocab = ['noreply', '%', 'cancel', 'connect','connections' 'cut', 'delivery', 'document', 'fee', 'free',
'invitation', 'impressions', 'launch', 'linkedin' 'noticed', 'ordered','profile', 'recently', 'reminder',
'review', 'save','searches', 'ship', 'today', 'tomorrow', 'update', 'views'] # problem with plurals

token_ = {}
df = pd.read_csv('test_data.csv')


def tokenize_and_vectorize(subject,sender):
    vector = []
    token = []
    subject = re.sub(r'[^a-zA-Z0-9 %]', '', subject)
    sender = re.sub(r'[^a-zA-Z0-9]', '', sender)
    #print('a:  ', subject)
    list = subject.lower().split() # a list
    if 'noreply' in sender.lower():
        list.append('noreply')

    #print(list)
    for word in vocab:
        #print(type(word))
        if word in list:
            token.append(word)
            vector.append(1)
        else:
            vector.append(-1)


    return token, vector, subject

all_tokens = []
all_vectors = []
all_subjects = []
new_df = df

for i in range(len(df)):
    old_subject = df['subject'].iloc[i]
    sender = df['sender'].iloc[i]
    #print('b:',  subject)
    token, vector, new_subject = tokenize_and_vectorize(old_subject, sender)
    all_tokens.append(token)
    all_vectors.append(vector)
    all_subjects.append(new_subject)
    # all_vectors.append(vector)

new_df['modified subject'] = all_subjects
new_df['modified token'] = all_tokens
new_df['modified vector'] = all_vectors

new_df.to_csv('modified_4.csv')

'''for i in range(len(all_tokens)):
    print('subject: ', all_subject[i],
        'tokens:' , all_tokens[i], 'vectors: ', all_vectors[i])

new_df = df

new_df['token_new'] = all_tokens
# new_df['vector'] = all_vectors

new_df.to_csv('new_data.csv')'''
