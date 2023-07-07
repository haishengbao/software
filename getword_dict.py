以下是您提供的代码的修改版本：

```python
#构建初步词典的具体步骤1
def get_vocab(corpus):
    word_vocab = set()
    for data in corpus:
        for i in range(0,len(data[1][0])):
            word_vocab.add(data[1][0][i])
        for i in range(0,len(data[1][1])):
            word_vocab.add(data[1][1][i])
        for i in range(0,len(data[2][0])):
            word_vocab.add(data[2][0][i])
        for i in range(0,len(data[3])):
            word_vocab.add(data[3][i])
    return word_vocab

import pickle

def load_pickle(filename):
    return pickle.load(open(filename, 'rb'), encoding='iso-8859-1')

#构建初步词典
def vocab_processing(filepath, save_path):
    with open(filepath, 'r') as f:
        total_data = eval(f.read())
        f.close()

    word_vocab = get_vocab(total_data)
    
    with open(save_path, "w") as f:
        f.write(str(word_vocab))

def final_vocab_processing(existing_vocab_path, new_data_path, save_path):
    existing_vocab = set()
    with open(existing_vocab_path, 'r') as f:
        existing_vocab = set(eval(f.read()))
        f.close()
    
    new_data = eval(open(new_data_path, 'r').read())

    new_vocab = get_vocab(new_data)
    word_set = new_vocab - existing_vocab
    
    print("Existing Vocabulary Size:", len(existing_vocab))
    print("New Words Found:", len(word_set))
    
    with open(save_path, "w") as f:
        f.write(str(word_set))

if __name__ == "__main__":
    #====================获取staqc的词语集合===============
    python_hnn = '/home/gpu/RenQ/stqac/data_processing/hnn_process/data/python_hnn_data_teacher.txt'
    python_staqc = '/home/gpu/RenQ/stqac/data_processing/hnn_process/data/staqc/python_staqc_data.txt'
    python_word_dict = '/home/gpu/RenQ/stqac/data_processing/hnn_process/data/word_dict/python_word_vocab_dict.txt'

    sql_hnn = '/home/gpu/RenQ/stqac/data_processing/hnn_process/data/sql_hnn_data_teacher.txt'
    sql_staqc = '/home/gpu/RenQ/stqac/data_processing/hnn_process/data/staqc/sql_staqc_data.txt'
    sql_word_dict = 'D:/学习/aDrive/data_processing/hnn_process/data/word_dict/sql_word_vocab_dict.txt'

    # vocab_processing(python_staqc, python_word_dict)
    # vocab_processing(sql_staqc, sql_word_dict)

    #====================获取最后大语料的词语集合的词语集合===============
    new_sql_staqc = '../hnn_process/ulabel_data/staqc/sql_staqc_unlabled_data.txt'
    final_vocab_processing(sql_word_dict, new_sql_staqc, save_path)
    #vocab_processing(new_sql_staqc, final_word_dict_sql)

    new_python_staqc = '../hnn_process/ulabel_data/staqc/python_staqc_unlabled_data.txt'
    #final_vocab_processing(python_word_dict, new_python_large, large_word_dict_python)
    #vocab_processing(new_python_staqc, final_word_dict_python)
```

请确保按照您的需求设置正确的文件路径。希望对您有所帮助！如果有任何其他问题，请随时提问。
