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

with open('fog.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        x1.append(float(row[1]))
        y.append(float(row[2]))
        y1.append(float(row[3]))
        z.append(float(row[4]))
        z1.append(float(row[5]))


#plt.plot(x,x1,y,y1,z,z1, marker='o')
plt.plot(x, '-o' );
plt.plot(x1, '-o');
plt.plot(y, '-*');
plt.plot(y1, '-*');
plt.plot(z, '-+');
plt.plot(z1, '-+');

plt.title('Cloud level  information passing through AES,DES & RSA algorithm')

plt.xlabel('Block Number(Unit)')
plt.ylabel('Execution Time (sec)')

#plt.legend(['line plot 1','line plot 1'])


plt.legend(['AES Encryption','AES Decryption', 'DES Encryption', 'DES Decryption','RSA Encryption','RSA Decryption'])

plt.show()

