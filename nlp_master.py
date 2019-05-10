# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 21:38:37 2019

@author: pathouli
"""

from nlp_class import nlp_func

the_path = 'C:/Users/pathouli/myStuff/academia/torhea/data/'

framework = nlp_func()

the_files =  framework.list_txt_files(the_path)
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



