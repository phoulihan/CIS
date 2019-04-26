#!/usr/bin/e
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
    
    def filename(the_path_tmp):
               if  filename.endswith(".txt"): 
                    file_path = the_path_tmp + '/' + filename
                    tmp = self.tokenize_text(file_path)
                    the_body_tmp = [word_i for word_i in tmp.split() if word_i not in the_stopwords]
                    the_body = ' '.join(the_body_tmp)
                    full_list = full_list.append(
                            {'label': word,
                             'body': the_body}, ignore_index=True)
    
    
