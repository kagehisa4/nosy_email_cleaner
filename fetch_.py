#import standard email library
import imaplib, email
import pandas as pd

#fetch emails use credentials

EMAIL = input('Enter EMAIL: ')
PASSWORD = input('Enter IMAP PASSWORD: ')
SERVER = 'imap.gmail.com'

# log into email via IMAP connection object

mail = imaplib.IMAP4_SSL(SERVER)
mail.login(EMAIL, PASSWORD)

mail.select('"[Gmail]/All Mail"') # Gmail's internal folder -- "[Gmail]/All Mail"


status, data = mail.search(None, 'ALL')
#status = OK
#data = [b'1 2 3 4 5'] - a single bytes string.

mail_ids = data[0].split()
#returns [b'1', b'2', ....]

#create a LIST to store EMAIL DataFrame

annotated = []

for i in mail_ids:
    status, msg_data = mail.fetch(i,
    '(BODY.PEEK[HEADER.FIELDS (FROM SUBJECT)] FLAGS)'
    ) # '(BODY [HEADER/TEXT//])' can be used separately
    # msg_data is still in binary

    # msg_data - [(), b')']

    for response_ in msg_data:
        if isinstance(response_, tuple):
            msg = email.message_from_bytes(response_[1]) # returns a LIST
            sender = msg['from']
            subject = msg['subject']
            flag_ = response_[0].decode()
            label = 1 if '\\Flagged' in str(flag_) else 0

            # save into annotated

            annotated.append({
            "sender" : sender,
            "subject" : subject,
            "label" : flag_ })

mail.logout()

# save to to_csv

df = pd.DataFrame(annotated)

df.to_csv('annotated_emails.csv', index = False)
