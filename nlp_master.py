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

the_path = 'E:/CIS_research/data/'

user_text=input("please enter the text")

framework = nlp_func()

the_files =  framework.list_txt_files(the_path)

my_vec_model, label_decoder, my_vec, labels = framework.the_vec_func(the_files)


# my_pca = framework.pca_step(my_vec, 10)


the_model = RandomForestClassifier()

#the_model = MultinomialNB()
# the_model = AdaBoostClassifier()
# the_model = SVC(gamma='auto')

param_grid = {"max_depth": [1, 5, 20],
              "n_estimators": [10, 50],
              "bootstrap": [True, False],
              "criterion": ["gini", "entropy"]}

gridsearch_model, best, opt_params = framework.grid_search_func(param_grid, the_model, my_vec, labels)

optimal_rf = RandomForestClassifier()
framework.full_train(optimal_rf, gridsearch_model, my_vec, labels) 

prediction, prediction_proba = framework.predict(optimal_rf, my_vec_model, label_decoder, user_text)

# 