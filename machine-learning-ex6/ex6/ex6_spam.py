# %%
import numpy as np
import re

# Because I don't want to spend lots of time to rewrite ewerything to python, now I'm using oct2py
from oct2py import  octave

# %%

f = open('emailSample1.txt', 'r')
file_contents = f.read()
f.close()

# %%

print(file_contents)

# %%
# def getVocabList():
    
#     f = open('vocab.txt', 'r')
#     file_content = f.read()
#     f.close()
    
#     vocabList = {}
    
#     file_content_split = file_content.splitlines()
    
#     for line in file_content_split:
    
#         vocabList[line.split()[1]] = int(line.split()[0])
    
#     return vocabList
    
# def porterStemmer(inString):
        
#     if inString[-1] in [ 's',  'e'] :
        
#         inString = inString[:-1]
    
#     return inString
    
# def emailFeatures(word_indices):
    
#     n = 1899
    
#     x = np.zeros(n)
    
#     x[word_indices] = 1
    
#     return x

# %%

word_indices = octave.processEmail( file_contents).flatten()
word_indices

# %%


# %%
from sklearn import svm
# %%

# %%
data = sio.loadmat(file_name='spamTrain.mat')
X=data['X']
y=data['y'].flatten()
# %%

import scipy.io as sio
# %%
C = 0.1
model = svm.SVC(kernel='linear', C = C)
# %%
model.fit(X, y)
# %%
model