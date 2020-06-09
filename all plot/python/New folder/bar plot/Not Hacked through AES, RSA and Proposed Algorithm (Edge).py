import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import csv
fig = plt.figure(figsize=(8,5))
x=[]
x1=[]
y=[]
y1=[]
z=[]
z1=[]

with open('Not Hacked through AES, RSA and Proposed Algorithm (Edge).csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        x1.append(float(row[1]))
        y.append(float(row[2]))
        y1.append(float(row[3]))
        z.append(float(row[4]))
        z1.append(float(row[5]))

df_3d = pd.DataFrame([x, x1, y,y1, z, z1]).transpose()
#df_4d = pd.DataFrame([dades04, dades05, dades06]).transpose()
colors = ['#9d43fc','#43ebfc','#fcf919','#001bff','#ff0000','#00ff1b']



ax = fig.add_subplot(111, projection='3d')
z=list(df_3d)

for n, i in enumerate(df_3d):
   
    xs = np.arange(len(df_3d[i]))
    ys = [i for i in df_3d[i]]
    
    arr = np.multiply(xs, ys)
    
    zs = z[n] 
    

    cs = colors[n]
    print(arr)
    
    ax.bar(xs,ys, zs, zdir='y',color=cs, alpha=0.8)
    



xticks= [0,1,2,3,4,5,6,7,8,9,10]

yticks = [0,1,2,3,4,5]


ax.set_xticks(xticks)
ax.set_yticks(yticks)




ax.set_xlabel('\n Block Number (Unit) \n AES Algorithm ')
ax.set_ylabel('RSA Algorithm')
ax.set_zlabel('\nExecution Time (Sec) \n Proposed Algorithm')

plt.legend(['AES Encryption','AES Decryption','RSA Encryption','RSA Decryption','Proposed Encryption', 'Proposed Decryption'],bbox_to_anchor=(0., .93, 1., .102), loc=3,
       ncol=2, mode="expand", borderaxespad=0.)


txt="Not Hacked through AES, RSA and Proposed Algorithm (Edge)"
# center text
fig.text(.5, .05, txt, ha='center')

plt.show()
