import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import ast
import numpy as np
import feather

def makeMatrix(file):
    return np.array(ast.literal_eval(file))

def updateDf():
    df = feather.read_dataframe("./archive/data.feather")
    df["mfcc"] = df["mfcc"].apply(makeMatrix)
    feather.write_dataframe(df, "./archive/data2.feather")

def toInt(flt):
    return int(flt)

#try random stuff here
def cutMFCC(mfcc, max_length=5):
    mfcc = mfcc.split(",")  # Assuming mfcc is a comma-separated string
    mfcc = str(len(mfcc))
    mfcc = [int(digit) for digit in mfcc]  # Convert strings to integers
    if len(mfcc) < max_length:
        # Pad the sequence with zeros if its length is less than max_length
        mfcc = [0] * (max_length - len(mfcc)) + mfcc
    elif len(mfcc) > max_length:
        # Truncate the sequence if its length is greater than max_length
        mfcc = mfcc[:max_length]
    return mfcc

data = feather.read_dataframe("./archive/data.feather")
#data = data.head(6000)
data["mfcc"] = data["mfcc"].apply(cutMFCC)
X = data["mfcc"]

data["age"] = data["age"].apply(toInt)
y = data["age"].values
X_train, X_valid, y_train, y_valid = train_test_split(X, y)
model = GaussianNB()

X_train = np.array(X_train.tolist())
y_train = np.array(y_train)
model.fit(X_train, y_train)

#Calculate and print the score of the model
X_valid = np.array(X_valid.tolist())
y_valid = np.array(y_valid)
score = model.score(X_valid, y_valid)
print("Model Score:", score)

#prints out predictions for all valid sets
# for X_sample, y_sample in zip(X_valid, y_valid):
#     X_sample = np.array(X_sample).reshape(1, -1)  # Reshape to ensure it's a 2D array
#     prediction = model.predict(X_sample)
#     print("Age is", prediction[0], "Actual age:", y_sample)
#Save the score to a text file
# with open("model_score.txt", "w") as f:
#     f.write("Model Score: " + str(score))
