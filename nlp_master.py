# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 21:38:37 2019

@author: pathouli
"""

from nlp_class import nlp_func
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.decomposition import PCA

the_path = 'C:/Users/pathouli/myStuff/academia/torhea/data/'

framework = nlp_func()

the_files =  framework.list_txt_files(the_path)

my_vec_model, label_decoder, my_vec, labels = framework.the_vec_func(the_files)

# my_pca = framework.pca_step(my_vec, 10)

the_model = RandomForestClassifier()
#the_model = MultinomialNB()
# the_model = AdaBoostClassifier()
# the_model = SVC()

#param_grid = {"shrinking": [True, False]}

param_grid = {"max_depth": [1, 5, 20],
              "n_estimators": [10, 50],
              "bootstrap": [True, False],
              "criterion": ["gini", "entropy"]}

gridsearch_model, best, opt_params = framework.grid_search_func(param_grid, the_model, my_vec, labels)

the_model_train, feature_imp = framework.full_train(the_model, gridsearch_model, my_vec, labels) 

#feature_imp_sort.sort_values("features", ascending=False)
#feature_imp_sort.sort_values('0', ascending=False)

the_test = "C:/Users/pathouli/myStuff/academia/torhea/sample_data/sample.txt"
prediction, prediction_proba = framework.predict(the_model_train, my_vec_model, label_decoder, the_test, "file")

for word in feature_imp.index[1:20]:
    prediction, prediction_proba = framework.predict(the_model_train, my_vec_model, label_decoder, [word], None)
    print word + ": " + prediction