import librosa
import pandas as pd

def pathExists(missing):
    return missing == "FALSE"

def filenameFixer(file):
    ret = './archive/recordings/recordings/' + file + '.mp3'
    return ret

def getMfcc(file):
    signal, sample_rate = librosa.load(file, sr = None)
    mfccs = librosa.feature.mfcc(y=signal, sr = sample_rate, n_mfcc=13)
    return mfccs

df = pd.read_csv('./archive/speakers_all.csv')
df['pathExists'] = df['file_missing?'].apply(pathExists)
df['filename'] = df['filename'].apply(filenameFixer)
df = df[df['pathExists']]
df['mfcc'] = df['filename'].apply(getMfcc)
df.to_csv('data.csv')


