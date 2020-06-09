import matplotlib.pyplot as plt

import numpy as np
from numpy.random import normal,rand
import csv

x=[]
x1=[]
y=[]
y1=[]
z=[]
z1=[]

with open('Not Hacked through DES, RSA and Proposed Algorithm (Edge).csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        x1.append(float(row[1]))
        y.append(float(row[2]))
        y1.append(float(row[3]))
        z.append(float(row[4]))
        z1.append(float(row[5]))


fig, ax = plt.subplots(figsize=(7, 5))
fig.subplots_adjust(bottom=0.2, left=0.2)
#plt.plot(x,x1,y,y1,z,z1, marker='o')
ax.plot(x, '-o' );
ax.plot(x1, '-o');
ax.plot(y, '-*');
ax.plot(y1, '-*');
ax.plot(z, '-+');
ax.plot(z1, '-+');


ax.set_xlabel('Block Number (Unit) \n\n Not Hacked through DES, RSA and Proposed Algorithm (Edge)')
ax.set_ylabel('Execution Time (sec)')
#plt.zlabel('Proposed Algorithm')
#plt.title(.5, .05,'Not Hacked through DES, RSA and Proposed Algorithm (Edge)')

#txt="Data passing through AES, RSA and Proposed Algorithm (Fog)"
#fig = plt.figure()
#fig.text(.5, .05, txt, ha='center')

plt.legend(['DES Encryption','DES Decryption','RSA Encryption','RSA Decryption','Proposed Encryption', 'Proposed Decryption'])

plt.show()
