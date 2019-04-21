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
        with open(file_path,'r') as txt:
             the_text = txt.readlines()
        text_split_pre = ' '.join(the_text)
        text_split_pre = text_split_pre.split()
        text_split = [re.sub('[^A-Za-z0-9]+', '', word).lower() for word in text_split_pre]
        
        text_split_out = re.sub(' +', ' ', ' '.join(text_split))
      
        return text_split_out
    def get_txt(self,path,filename,stopwords):
        txt_path = os.path.join(path,filename)
        print(txt_path)
        tmp = self.tokenize_text(txt_path)
        the_body_tmp = [word for word in tmp.split() if word not in stopwords]
        the_body = ' '.join(the_body_tmp)
        return the_body
    def list_txt_files(self, the_path):
        the_stopwords = set(stopwords.words('english'))
        full_list = pd.DataFrame()
        the_dirs = os.listdir(the_path)
        for word in the_dirs:
            the_path_tmp = os.path.join(the_path,word)
            for filename in os.listdir(the_path_tmp):
                if filename.endswith(".txt"): 
                    the_body = self.get_txt(the_path_tmp,filename,the_stopwords)
                    full_list = full_list.append(
                            {'label': word,
                             'body': the_body}, ignore_index=True)
                    continue
                else:
                    continue
    
        return full_list
