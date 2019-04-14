# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 20:30:42 2019

@author: pathouli
"""
import re, os

def tokenize_text(file_path):
    #read text from file and TOKENIZE
    the_text_tmp = open(file_path, 'r')
    the_text = the_text_tmp.readlines()
    the_text_tmp.close()
    text_split_pre = ' '.join(the_text)
    text_split_pre = text_split_pre.split()
    text_split = [re.sub('[^A-Za-z0-9]+', '', word).lower() for word in text_split_pre]
    
    text_split_out = ' '.join(text_split)
    
    return text_split_out

def list_txt_files(the_path_var):
    file_names = list()
    for filename in os.listdir(the_path):
        if filename.endswith(".txt"): 
            file_names.append(os.path.join(the_path, filename))
            continue
        else:
            continue

    return file_names

the_path = 'C:/Users/pathouli/myStuff/academia/torhea/data/'

the_files = list_txt_files(the_path)

my_clean_text = [tokenize_text(word) for word in the_files]
