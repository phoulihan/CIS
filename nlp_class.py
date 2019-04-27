# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 20:30:42 2019

@author: pathouli
"""
import re, os
import pandas as pd
from nltk.corpus import stopwords

class nlp_func():
    
    def tokenize_text(self, file_path):
        #read text from file and TOKENIZE
        the_text_tmp = open(file_path, 'r')
        the_text = the_text_tmp.readlines()
        the_text_tmp.close()
        text_split_pre = ' '.join(the_text)
        text_split_pre = text_split_pre.split()
        text_split = [re.sub('[^A-Za-z]+', '', word).lower() for word in text_split_pre]
        
        text_split_out = re.sub(' +', ' ', ' '.join(text_split))
      
        return text_split_out
    
    def list_txt_files(self, the_path):
        the_stopwords = set(stopwords.words('english'))
        full_list = pd.DataFrame()
        tmp2 = self.function2(the_path)
        the_body_tmp = [word_i for word_i in tmp2.split() if word_i not in the_stopwords]
        the_body = ' '.join(the_body_tmp)
        the_dirs = os.listdir(the_path)
        for word in the_dirs:
            full_list = full_list.append({'label': word,'body': the_body}, ignore_index=True)
    
        return full_list
    
    def function2(self, the_path):
        the_dirs = os.listdir(the_path)
        for word in the_dirs:
            the_path_tmp = the_path + word
            for filename in os.listdir(the_path_tmp):
                if filename.endswith(".txt"): 
                    file_path = the_path_tmp + '/' + filename
                    tmp = self.tokenize_text(file_path)
                    continue
                else:
                    continue
        
        return tmp
    
    def the_vec_func(self, files_in):
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn import preprocessing
        
        the_vec = CountVectorizer()
        cnt_vec = pd.DataFrame(the_vec.fit_transform(files_in.body).toarray())
        cnt_vec.columns = the_vec.get_feature_names()
        
        lab_enc = preprocessing.LabelEncoder()
        the_labels = pd.DataFrame(lab_enc.fit_transform(files_in.label))
        
        return cnt_vec, the_labels