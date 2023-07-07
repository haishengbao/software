'''
并行分词
'''
import os
import pickle
import logging

import sys
sys.path.append("..")

from python_structured import *
from sqlang_structured import *

#FastText库 gensim 3.4.0
from gensim.models import FastText

import numpy as np

#词频统计库
import collections
#词云展示库
import wordcloud
#图像处理库 Pillow 5.1.0
from PIL import Image

多进程
from multiprocessing import Pool as ThreadPool

#python解析
def multipro_python_query(data_list):
result = [python_query_parse(line) for line in data_list]
return result

def multipro_python_code(data_list):
result = [python_code_parse(line) for line in data_list]
return result

def multipro_python_context(data_list):
result = []
for line in data_list:
if line == '-10000':
result.append(['-10000'])
else:
result.append(python_context_parse(line))
return result

#sql解析
def multipro_sqlang_query(data_list):
result = [sqlang_query_parse(line) for line in data_list]
return result

def multipro_sqlang_code(data_list):
result = [sqlang_code_parse(line) for line in data_list]
return result

def multipro_sqlang_context(data_list):
result = []
for line in data_list:
if line == '-10000':
result.append(['-10000'])
else:
result.append(sqlang_context_parse(line))
return result

def parse_data(data_list, split_num, parse_function):
data = [i[1][0][0] for i in data_list]
split_list = [data[i:i + split_num] for i in range(0, len(data), split_num)]
pool = ThreadPool(10)
result_list = pool.map(parse_function, split_list)
pool.close()
pool.join()
result = []
for p in result_list:
result += p
print('条数：%d' % len(result))
return result

def parse_python(python_list, split_num):
acont1_cut = parse_data(python_list, split_num, multipro_python_context)

acont2_cut = parse_data(python_list, split_num, multipro_python_context)

query_cut = parse_data(python_list, split_num, multipro_python_query)

code_cut = parse_data(python_list, split_num, multipro_python_code)

qids = [i[0] for i in python_list]
print(qids[0])
print(len(qids))

return acont1_cut, acont2_cut, query_cut, code_cut, qids
def parse_sqlang(sqlang_list, split_num):
acont1_cut = parse_data(sqlang_list, split_num, multipro_sqlang_context)

acont2_cut = parse_data(sqlang_list, split_num, multipro_sqlang_context)

query_cut = parse_data(sqlang_list, split_num, multipro_sqlang_query)

code_cut = parse_data(sqlang_list, split_num, multipro_sqlang_code)

qids = [i[0] for i in sqlang_list]

return acont1_cut, acont2_cut, query_cut, code_cut, qids
def main(lang_type, split_num, source_path, save_path):
total_data = []
with open(source_path, "rb") as f:
corpus_lis = pickle.load(f) # pickle
if lang_type == 'python':
parse_acont1, parse_acont2, parse_query, parse_code, qids = parse_python(corpus_lis, split_num)
for i in range(len(qids)):
total_data.append([qids[i], [parse_acont1[i], parse_acont2[i]], [parse_code[i]], parse_query[i]])
if lang_type == 'sql':
parse_acont1, parse_acont2, parse_query, parse_code, qids = parse_sqlang(corpus_lis, split_num)
for i in range(len(qids)):
total_data.append([qids[i], [parse_acont1[i], parse_acont2[i]], [parse_code[i]], parse_query[i]])
with open(save_path, "w") as f:
f.write(str(total_data))

python_type = 'python'
sqlang_type = 'sql'

split_num = 1000

if name == 'main':
staqc_python_path = '../hnn_process/ulabel_data/python_staqc_qid2index_blocks_unlabeled.txt'
staqc_python_save = '../hnn_process/ulabel_data/staqc/python_staqc_unlabled_data.txt'

staqc_sql_path = '../hnn_process/ulabel_data/sql_staqc_qid2index_blocks_unlabeled.txt'
staqc_sql_save = '../hnn_process/ulabel_data/staqc/sql_staqc_unlabled_data.txt'

main(sqlang_type, split_num, staqc_sql_path, staqc_sql_save)
main(python_type, split_num, staqc_python_path, staqc_python_save)
