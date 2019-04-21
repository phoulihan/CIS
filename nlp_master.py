# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 21:38:37 2019

@author: pathouli
"""

from nlp_class import nlp_func
from sklearn.ensemble import RandomForestClassifier

the_path = 'C:/Users/pathouli/myStuff/academia/torhea/data/'

framework = nlp_func()

the_files =  framework.list_txt_files(the_path)

my_vec, labels = framework.the_vec_func(the_files)

the_model = RandomForestClassifier()
the_model.fit(my_vec, labels)

#lab_enc.inverse_transform(0)
# print (the_vec.get_feature_names())
# test = cnt_vec.toarray()
# print (cnt_vec.toarray())




