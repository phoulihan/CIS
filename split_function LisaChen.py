#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_txt_words_file_paths(self, the_path):
    """
    返回一个列表， 包含the_path 文件路径下 所有(word, .txt文件的路径名)。
    """
    words_file_paths = []
    # 当前目录下的所有文件名
    the_dirs = os.listdir(the_path)
    for word in the_dirs:
        #当前目录文件的路径名
        the_path_tmp = the_path + word
        #获取.txt文件的路径名
        word_file_path  = [(word, the_path_tmp + '/' + filename)
                           for filename in os.listdir(the_path_tmp) 
                             if filename.endswith(".txt")]
        #添加到返回列表中
        words_file_paths.append(word_file_path)
    return words_file_paths

def list_txt_files(self, the_path):
    # 获取英文停用词
    the_stopwords = set(stopwords.words('english'))
    # DataFame对象用来存放结果
    full_list = pd.DataFrame()
    words_file_paths = get_txt_words_file_paths(the_path)
    for (word, file_path) in words_file_paths:
        #调用tokenize_text()获取 text 和 tokenize
        tmp = self.tokenize_text(file_path)
        #分词
        the_body_tmp = [word for word in tmp.split() if word not in the_stopwords]
        the_body = ' '.join(the_body_tmp)
        #添加结果到返回list中
        full_list = full_list.append(
                    {'label': word,
                    'body': the_body}, ignore_index=True)
    return full_list


# In[ ]:




