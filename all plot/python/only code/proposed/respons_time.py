import matplotlib.pyplot as plt

import numpy as np
from numpy.random import normal,rand
import csv

x=[]
y=[]


with open('respnse_time.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
        


#plt.plot(x,x1,y,y1,z,z1, marker='o')
plt.plot(x, '-o' );
plt.plot(y, '-*');


plt.title('Fog and Cloud Response Time of Proposed Algorithm')

plt.xlabel('Block Number(unit)')
plt.ylabel('Execution Time (sec)')

#plt.legend(['line plot 1','line plot 1'])


plt.legend(['Fog Response Time','Cloud Response Time'])

plt.show()

