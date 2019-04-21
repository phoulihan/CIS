# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 21:38:37 2019

@author: pathouli
"""

from nlp_class import nlp_func
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

the_path = 'C:/Users/pathouli/myStuff/academia/torhea/data/'

framework = nlp_func()

the_files =  framework.list_txt_files(the_path)

the_vec = CountVectorizer()

cnt_vec = pd.DataFrame(the_vec.fit_transform(the_files.body).toarray())
cnt_vec.columns = the_vec.get_feature_names()



# print (the_vec.get_feature_names())

# test = cnt_vec.toarray()

# print (cnt_vec.toarray())




