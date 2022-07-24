# Import libraries
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Data preparation
df_neg = pd.read_csv(r'negative_examples_posology.csv')
first_column = df_neg.columns[0]
df_neg=df_neg.drop(first_column, axis=1)
df_neg = df_neg.rename(columns=({'0':'text'}))
df_neg["label"] = 0

df_pos = pd.read_csv (r'positive_examples_posology.csv')
first_column = df_pos.columns[0]
df_pos=df_pos.drop(first_column, axis=1)
df_pos = df_pos.rename(columns=({'0':'text'}))
df_pos["label"] = 1

df = pd.merge(df_neg, df_pos,how='outer')

# Data preprocessing
#1. Vectorizing data
vectorizer = CountVectorizer(ngram_range=(1, 2), min_df=20)
x = vectorizer.fit_transform(df['text'].values.astype('U'))
y = df['label']

#2. Data split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Training the ML model
model = LogisticRegression(max_iter=1000, random_state=0)
model.fit(x_train, y_train)

# Testing the ML Model
y_pred = model.predict(x_test)
print(classification_report(y_test, y_pred))

#Saving model
pickle.dump(model, open('model_lr.pkl', 'wb'))
pickle.dump(vectorizer, open("vectorizer.pickle", "wb"))