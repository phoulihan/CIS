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
        the_dirs = os.listdir(the_path)
        for word in the_dirs:
            the_path_tmp = the_path + word
            print word
            for filename in os.listdir(the_path_tmp):
                if filename.endswith(".txt"): 
                    file_path = the_path_tmp + '/' + filename
                    tmp = self.tokenize_text(file_path)
                    the_body_tmp = [word_i for word_i in tmp.split() if word_i not in the_stopwords]
                    the_body = ' '.join(the_body_tmp)
                    full_list = full_list.append(
                            {'label': word,
                             'body': the_body}, ignore_index=True)
                    continue
                else:
                    continue
    
        return full_list
    
    def the_vec_func(self, files_in):
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn import preprocessing
        
        the_vec = CountVectorizer()
        cnt_vec = pd.DataFrame(the_vec.fit_transform(files_in.body).toarray())
        cnt_vec.columns = the_vec.get_feature_names()
        
        lab_enc = preprocessing.LabelEncoder()
        the_labels = pd.DataFrame(lab_enc.fit_transform(files_in.label))
        
        return cnt_vec, the_labels
    
    def pca_step(self, data_in, num_comp):
        from sklearn.decomposition import PCA
        my_vec_model = PCA(n_components=num_comp)
        my_vec_model.fit(data_in)
        my_vec_pca = my_vec_model.transform(data_in)
        
        print ("Variance Explained: " + str(sum(my_vec_model.explained_variance_ratio_)))
        
        return my_vec_pca
    
    def full_train(self, the_model, my_vec_in, labels_in):
        #optimal_rf = RandomForestClassifier(bootstrap=False,criterion="gini",max_depth=20,n_estimators=50)
        the_model.fit(my_vec_in, labels_in)
        feature_imp = the_model.feature_importances_
        
        return feature_imp