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
        text_split = [re.sub('[^A-Za-z0-9]+', '', word).lower() for word in text_split_pre]
        
        text_split_out = re.sub(' +', ' ', ' '.join(text_split))
      
        return text_split_out
    
    def list_txt_files(self, the_path):
        the_stopwords = set(stopwords.words('english'))
        full_list = pd.DataFrame()
        the_dirs = os.listdir(the_path)
        for word in the_dirs:
            the_path_tmp = the_path + word
            for filename in os.listdir(the_path_tmp):
                if filename.endswith(".txt"): 
                    file_path = the_path_tmp + '/' + filename
                    tmp = self.tokenize_text(file_path)
                    the_body_tmp = [word for word in tmp.split() if word not in the_stopwords]
                    the_body = ' '.join(the_body_tmp)
                    full_list = full_list.append(
                            {'label': word,
                             'body': the_body}, ignore_index=True)
                    continue
                else:
                    continue
    
        return full_list