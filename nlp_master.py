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
from sklearn.model_selection import GridSearchCV

the_path = 'C:/Users/Tyler/data/'

framework = nlp_func()

the_files =  framework.list_txt_files(the_path)

my_vec, labels = framework.the_vec_func(the_files)



the_model = RandomForestClassifier()
#the_model = MultinomialNB()
# the_model = AdaBoostClassifier()
# the_model = SVC(gamma='auto')


param_grid = {"max_depth": [20, 50],
              "n_estimators": [10, 50],
              "bootstrap": [True, False],
              "criterion": ["gini", "entropy"]}

#param_grid = {"alpha": [0, 1.0],
#              "fit_prior": [True, False]}

grid_search = GridSearchCV(the_model, param_grid=param_grid, cv=5)
grid_search.fit(my_vec, labels)
print (grid_search.best_score_)

#optimal_params = (grid_search.best_params_)

#my_cv = cross_val_score(the_model, my_vec, labels, cv=10)

#opt_model = RandomForestClassifier(grid_search.best_params_)
#opt_model.fit(my_vec, labels)

#print (np.mean(my_cv))






#the_model.fit(my_vec, labels)
#test = the_model.feature_importances_

#lab_enc.inverse_transform(0)
# print (the_vec.get_feature_names())
# test = cnt_vec.toarray()
# print (cnt_vec.toarray())
