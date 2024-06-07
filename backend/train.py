#need to figure out a way to make this more accurate


import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import ast
import numpy as np
import feather
import joblib

def makeMatrix(file):
    return np.array(ast.literal_eval(file))

def updateDf():
    df = feather.read_dataframe("./archive/data.feather")
    df["mfcc"] = df["mfcc"].apply(makeMatrix)
    feather.write_dataframe(df, "./archive/data2.feather")

def toInt(flt):
    return int(flt)

#first 5 elements
def f5MFCC(row):
    mfcc = row["mfcc"].split(",")[:5]
    mfcc = [float(x) for x in mfcc]
    age = row["age"]
    mfcc_with_age = [age] + mfcc
    return mfcc_with_age

#using length
def lenMFCC(mfcc, max_length=5):
    mfcc = mfcc.split(",")  #mfcc is a comma-separated string
    mfcc = str(len(mfcc))
    mfcc = [int(digit) for digit in mfcc]  #convert strings to integers
    if len(mfcc) < max_length:
        #pad the sequence with zeros if its length is less than max_length
        mfcc = [0] * (max_length - len(mfcc)) + mfcc
    elif len(mfcc) > max_length:
        #truncate the sequence if its length is greater than max_length
        mfcc = mfcc[:max_length]
    return mfcc

#0 for male, 1 for female
def sex2bool(sex):
    return 0 if sex == "male" else 1

def fixLang(lang):
    #maybe eventually remove the whole row but this is a filler
    return "fill" if lang == None else lang

data = feather.read_dataframe("./archive/data.feather")
#data = data.head(60)
data["sex"] = data["sex"].apply(sex2bool)

data["age"] = data["age"].apply(toInt)
#print(data)
data["mfcc_with_sex_age"] = data.apply(f5MFCC, axis=1)
X = data["mfcc_with_sex_age"]

data["native_language"] = data["native_language"].apply(fixLang)
y = data["sex"].values

#print(X, y)
X_train, X_valid, y_train, y_valid = train_test_split(X, y)
model = GaussianNB()

X_train = np.array(X_train.tolist())
y_train = np.array(y_train)
model.fit(X_train, y_train)

#Calculate and print the score of the model
X_valid = np.array(X_valid.tolist())
y_valid = np.array(y_valid)
score = model.score(X_valid, y_valid)
#print("Model Score:", score)
# Save the model to a file
#joblib.dump(model, 'trained_model.pkl')

#prints out predictions for all valid sets
for X_sample, y_sample in zip(X_valid, y_valid):
    X_sample = np.array(X_sample).reshape(1, -1)  # Reshape to ensure it's a 2D array
    prediction = model.predict(X_sample)
    print("Gender is", prediction[0], "Actual gender:", y_sample)
#Save the score to a text file
with open("model_score.txt", "w") as f:
    f.write("Model Score: " + str(score))
