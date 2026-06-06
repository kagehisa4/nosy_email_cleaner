# This is nosy email cleaner perceptron.

## Project Overview
* An Email Cleaner that identifies and filters nosy, low-value emails that clutter users’ inboxes using a Bag-of-Words representation. It is designed for future expansion with larger datasets, advanced NLP techniques and personalized email filtering.
* Trained a Perceptron Classifier to learn word importance from data, enabling more robust filtering than hard-coded keyword rules.

## Dataset
- Training Emails: 20
- Classes: Nosy, Clean
- Balanced Dataset: Yes

## Pipeline Model
```mermaid
flowchart LR
  A[Raw Emails] --> B[Tokenization]
  B --> C[Bag of Words]
  C ---> [Vectorize]
  D --> [Perceptron Classifier]
  E --> [Nosy/Clean prediction]
  F --> [1 click cleanup]
```

## INSTALLATION
```bash
git clone https://github.com/kagehisa4/nosy_email_cleaner
cd train.py
```

## Performance Metrics


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
