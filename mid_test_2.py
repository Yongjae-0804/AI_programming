import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('./data/test2.csv')

df2 = pd.DataFrame({'DownLink[kbyte/min]': df['DownLink']*0.06, 'UpLink[kbyte/min]': df['UpLink']*0.06}) # (byte/sec)*0.06 = (kbyte/min)
df2 = df2.astype(int)
dflist = (df2['DownLink[kbyte/min]'] >= 15000)

data_HL =[]
for i in dflist:
    if i:
        data_HL.append('High')
    else:
        data_HL.append('Low')

df2['status'] = data_HL

df3 = (df2[df2['status'] == 'High'])
df4 = df2[df2['status']=='Low']

x1 = df3['DownLink[kbyte/min]']
y1 = df3['UpLink[kbyte/min]']
x2 = df4['DownLink[kbyte/min]']
y2 = df4['UpLink[kbyte/min]']

plt.figure(figsize= (30,10))
plt.title('Data Analysis')

plt.xlabel("uplink")
plt.ylabel("downlink")
plt.scatter(y1, x1,color='r', label = 'high')
plt.scatter(df4['UpLink[kbyte/min]'], df4['DownLink[kbyte/min]'],color='blue',  label= 'low')

plt.legend()

plt.show()