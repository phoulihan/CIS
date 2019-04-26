# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 01:06:41 2019

@author: lenovo
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
        #the_stopwords = set(stopwords.words('english'))
        #代表一堆停止词的单词列表
        full_list = pd.DataFrame()
        #每个column就是一个Series的数据格式
        the_dirs = os.listdir(the_path)
        #返回指定的文件夹包含的文件或文件夹的名字的列表 
        for word in the_dirs:
            the_path_tmp = the_path + word
            for filename in os.listdir(the_path_tmp):
                filename(self, the_path_tmp)
                full_list = full_list.append(
                            {'label': word,
                             'body': the_body}, ignore_index=True)
                        #Series.append(to_append, ignore_index=False, verify_integrity=False
                        #to_append : Series or list/tuple of Series；ignore_index : boolean, default False；
                        #If True, do not use the index labels
                    continue
                else:
                    continue
    
        return full_list
    
def filename(self, the_path_tmp):
    #for filename in os.listdir(the_path_tmp):
    the_stopwords = set(stopwords.words('english'))
    
    full_list = pd.DataFrame()
    
                if filename.endswith(".txt"): 
                    file_path = the_path_tmp + '/' + filename
                    tmp = self.tokenize_text(file_path)
                    #分词
                    the_body_tmp = [word for word in tmp.split() if word not in the_stopwords]
                    the_body = ' '.join(the_body_tmp)
                    
            return filename(self, the_path_tmp)