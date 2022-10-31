import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./data/test3.csv', encoding='utf-8')

list1 = df['title'].astype(str)
list1_1 = []
for i in list1:
    list1_1.append(i.split())

list2 = df['contents'].astype(str)
list2_2 = []
for i in list2:
    list2_2.append(i.split())

df2 = pd.DataFrame({'time': df['time'], 'title': list1_1, 'contents': list2_2})

print(df2)