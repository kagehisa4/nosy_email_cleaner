import pandas as pd
from  email.header import decode_header

# parts of subject are in UTF- let's decode it properly

def decode_utf(text):
    decoded_parts = decode_header(text)
    decoded_subject = ''
    for part, encoding in decoded_parts:
        if isinstance(part, bytes):
            decoded_subject += part.decode(
                encoding if encoding else 'utf-8',
                errors = 'ignore'
            )
        else:
            decoded_subject += part
    return decoded_subject

#let's read csv
df = pd.read_csv('annotated_emails.csv')

new_df = df

#extract emails <>
new_df['sender'] = new_df['sender'].str.extract(r'<(.*?)>')

#if a cell is missing it's value, better remove it.
new_df = new_df.dropna(subset=['subject'])

#decode utf from subjects
new_df['subject'] = new_df['subject'].apply(decode_utf)

#fetch alphanumeric characters's + % - remove all unnecessary

new_df['subject'] = new_df['subject'].str.replace(r'[^a-zA-Z0-9 %]', '', regex=True)

#remove flags strings to numbers

new_df['label'] = new_df['label'].apply(
    lambda x: 1 if 'Flagged' in  str(x)
    else 0
)

new_df.to_csv('training_data.csv')
