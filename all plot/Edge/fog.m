clear all;
close all;
clc

A= dlmread("fog.csv");
x= A(:,1);
x2= A(:,2);
y= A(:,3);
y2= A(:,4);
z= A(:,5);
z2= A(:,6);

x1 = x2+15;
y1 = y2 +15;
z1= z2 +15; 


hold on
plot(x, '-o');
plot(x1, '-o');
plot(y, '-*');
plot(y1, '-*');
plot(z, '-+');
plot(z1, '-+');

legend('AES Encryption','AES Decryption', 'DES Encryption', 'DES Decryption','RSA Encryption','RSA Decryption',  'Location', 'NorthWest')
xlabel('Block Number(Unit)'), ylabel('Execution Time (sec)')
title('Edge level  information passing through AES,DES & RSA algorithm')
