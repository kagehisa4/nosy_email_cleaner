# This is nosy email cleaner perceptron.

* Create a hard-coded system
* Train a linear classifier perceptron using BoW approach.

## Steps used To Train the perceptron
### This approach is based on tokenizing & vectorizing EMAIL subjects.
1. All emails undergo preprocessing to extract clean sender email ids, subject.
2. Label the emails (you can also label them via GMAIL APP) and import lables using IMAP.
3. Use a vocabulary of notorious & clean words to tokenize email subjects.
4. Vectorize the tokens and train your model on the TEST DATA.
5. TEST DATA - equal number of positive and negative emails. (class-balance to avoid classifier bias.)
6. TEST DATA - my emails ~ 1000 in number all tokenized and vectorized.  
7. Test the model and compare accuracy.
8. You can set a threshold to create three CLASSES- 1. Clean (look urgent mails) 2. Normal (look when free.) 3. Nosy (emails  that need to trashed.)

## INSTALLATION
```bash
git clone https://github.com/kagehisa4/nosy_email_cleaner
cd train.py
```

# This is how I've done preprocessing - problems and remedies-

## Problems in the imported dataset (before preprocessing):

1. ![preprocessing\_1](images/preprocessing\_1.png)

  - emails inside <> - extract the string
  - some subject texts UTF encoded - decode UTF into normal text.
  - flags are present as text - convert to text

2. ![preprocessing_2](images/preprocessing_2.png)

  - some subjects are empty cells - delete the rows

3. ![preprocessing_3](images/preprocessing_3.png)

  - duplicates are present - delete duplicates
