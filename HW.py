# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 15:54:25 2019

@author: Ziyang Wang
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
    
    def body_txt(self,the_path):
        the_stopwords = set(stopwords.words('english'))
        the_dirs = os.listdir(the_path)
        body_txt = []
        for word in the_dirs:
            the_path_tmp = the_path + word
            for filename in os.listdir(the_path_tmp):
                if filename.endswith(".txt"): 
                    file_path = the_path_tmp + '/' + filename
                    tmp = self.tokenize_text(file_path)
                    body_txt_tmp = [word_i for word_i in tmp.split() if word_i not in the_stopwords]
                    body_txt.append (' '.join(body_txt_tmp))
                
        return body_txt
    
    def list_txt_files(self, the_path):
        full_list = pd.DataFrame()
        the_dirs = os.listdir(the_path)
        m=0
        for word in the_dirs:
            the_path_tmp = the_path + word
            for filename in os.listdir(the_path_tmp):
                if filename.endswith(".txt"):
                    the_body=self.body_txt(the_path)
                    full_list = full_list.append(
                            {'label': word,
                             'body': the_body[m]}, ignore_index=True)
                    m = m+1
                    continue
                else:
                    continue
    
        return full_list
