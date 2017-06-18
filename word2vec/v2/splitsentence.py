import re
import codecs
import jieba

FILENAME = '1_cleaned'
FILE_TO_WRITE = '1_cleaned_splitted'

ftow = codecs.open(FILE_TO_WRITE, 'w', encoding = 'utf-8') 
with codecs.open(FILENAME, 'r') as f:
    for line in f:
        print(line)
        splitted_line_list = jieba.lcut(line)
        stow = " ".join(splitted_line_list)
        print(stow)
        ftow.write(stow)
