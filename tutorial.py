# Author: Patrick Houlihan
# CIS Class exmaples

# -*- coding: utf-8 -*-
import pandas as pd
import re
import os

# dictionary is {key: value, key: value}
the_dict = {'a': 1.56, 'b': 2.5}

#fetch keys
the_keys = the_dict.keys()

#fetch values
the_values = the_dict.values()

the_dict_test = dict()

the_dict_test['a'] = 1

#list index starts at 0
the_array = [1,4,5,6,7]

print the_array[3]

the_array_init = list()
the_array_init.append(1)
the_array_init.append(5)
the_array_init.append(5)

print (the_array_init)

print len(the_array_init)

the_test_set = set()
the_test_set.add(1)
the_test_set.add(5)
the_test_set.add(5)

print (the_test_set)

print (type(0)) #this is an integer
print (type(0.0)) #this is a float
print (type("hello")) #this is a string
print (type(the_test_set))
print (type(the_array_init))

my_int = "0"
print (type(my_int))
my_int = int(my_int)
print (type(my_int))

my_float = "3.124"
print (type(my_float))
my_float = float(my_float)
print (type(my_float))
my_float = int(my_float)
print (type(my_float))
print (my_float)

my_new_float = 3.124
my_new_float = round(my_new_float, 2)
print (my_new_float)

var_a = "1.3"
var_b = 1.5

the_sum = float(var_a) + var_b
print (the_sum)

var_c = "hello"
var_d = " cis class"
the_cat = var_c + var_d
print (the_cat)

the_list_conv = the_cat.split(' ')
print (the_list_conv)

the_join = ','.join(the_list_conv)
print (the_join)
the_join = ' '.join(the_list_conv)
print (the_join)

loop_test_list = ['a', 'b', 'c', 'd']

temp = list()
for word in loop_test_list:
    if word == 'a':
        temp.append(word + '_a')
print temp

loop_test_list_loop = [word + '_a' for word in loop_test_list if word == 'a']


my_int = list(range(100))

even_num = [word for word in my_int if word % 2 == 0]
print (even_num)

odd_num = [word for word in my_int if word % 2 == 1]
print (odd_num)

############PANDAS DEMO############
import pandas as pd

#read in a csv file
the_data = pd.read_csv('C:/Users/pathouli/myStuff/academia/torhea/data/stock.csv')

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