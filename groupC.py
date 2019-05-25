# -*- coding: utf-8 -*-
"""
Created on Fri May 24 20:38:46 2019

@author: pathouli
"""

import pandas as pd
from sklearn.multiclass import OutputCodeClassifier
from sklearn.svm import LinearSVC

the_path = 'C:/Users/pathouli/myStuff/academia/torhea/projects/groupC/'

allstate_data = pd.read_csv(the_path + 'train.csv', sep=",")
clf = OutputCodeClassifier(LinearSVC(random_state=0), code_size=2, random_state=0)      
   
label_cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
X_cols = allstate_data.columns.difference(label_cols)
X = allstate_data[X_cols][1:10000]
y = allstate_data[label_cols][1:10000] #small sample to test      
          
clf.fit(X, y).predict(X) 
