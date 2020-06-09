import matplotlib.pyplot as plt
import csv

x=[]
x1=[]
y=[]
y1=[]
z=[]
z1=[]
a = []
fig = plt.figure(figsize=(6, 8))
with open('Data passing through DES, RSA and Proposed Algorithm (Fog).csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        x1.append(float(row[1]))
        y.append(float(row[2]))
        y1.append(float(row[3]))
        z.append(float(row[4]))
        z1.append(float(row[5]))
        a.append(float(row[6]))

plt.plot([],[],color='#60b1fd', label='DES Encryption', linewidth=5)
plt.plot([],[],color='#fd9760', label='DES Decryption', linewidth=5)
plt.plot([],[],color='#c7f950', label='RSA Encryption', linewidth=5)
plt.plot([],[],color='#f7f961', label='RSA Decryption', linewidth=5)
plt.plot([],[],color='#f378af', label='Proposed Encryption', linewidth=5)
plt.plot([],[],color='#f1e493', label='Proposed Decryption', linewidth=5)

plt.stackplot(x, x1,y,y1,z,z1,a, colors=['#60b1fd','#fd9760','#c7f950','#f7f961','#f378af','#f1e493'])

plt.xlabel('Block Number (Unit)')
plt.ylabel('Execution Time (sec)')

txt="Data passing through DES, RSA and Proposed Algorithm (Fog)"
# center text
fig.text(.5, .02, txt, ha='center')
plt.legend()
plt.show()
