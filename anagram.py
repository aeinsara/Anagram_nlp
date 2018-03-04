import xlrd
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

from itertools import permutations

import time
start_time = time.time()

wordInput = input("Enter a persian word: ")
perms = [''.join(p) for p in permutations(wordInput)]

df = pd.read_excel('D:\PersianWords.xlsx', sheetname='Sheet1')

print("Column headings:")

listW = df['Total farsi Word']

for word in perms:
    i = 0
    for i in df.index:
        if word == listW[i]:
           print(word)

print("--- %s seconds ---" % (time.time() - start_time))