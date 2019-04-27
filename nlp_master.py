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
from sklearn.decomposition import PCA

the_path = 'C:/Users/pathouli/myStuff/academia/torhea/data/'

framework = nlp_func()

the_files =  framework.list_txt_files(the_path)

my_vec, labels = framework.the_vec_func(the_files)

# test = framework.pca_step(my_vec, 10)

#my_vec_model = PCA(n_components=6)
#my_vec_model.fit(my_vec)
#my_vec_pca = my_vec_model.transform(my_vec)

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

#print ("Variance Explained: " + str(sum(my_vec_model.explained_variance_ratio_)))
print ("Grid Search Model Accuracy: " + str(grid_search.best_score_))

best_params = grid_search.best_params_


optimal_rf = RandomForestClassifier(bootstrap=False,criterion="gini",max_depth=20,n_estimators=50)
test = framework.full_train(optimal_rf, my_vec, labels)

optimal_rf.fit(my_vec, labels)
feature_imp = optimal_rf.feature_importances_
print (dsdsf)

non_zero = np.where(feature_imp != 0)


