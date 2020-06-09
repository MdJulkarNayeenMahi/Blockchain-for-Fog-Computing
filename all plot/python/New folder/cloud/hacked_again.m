clear all;
close all;
clc

A= dlmread("hacked.csv");
x= A(:,1);
x1= A(:,2);
y= A(:,3);
y1= A(:,4);
z= A(:,5);
z1= A(:,6);

hold on
plot(x, '-o');
plot(x1, '-o');
plot(y, '-*');
plot(y1, '-*');
plot(z, '-+');
plot(z1, '-+');

legend('AES Encryption','AES Decryption', 'DES Encryption', 'DES Decryption','RSA Encryption','RSA Decryption',  'Location', 'NorthWest')
xlabel('Block Number(Unit)'), ylabel('Execution Time (sec)')
title('Cloud Level AES,DES & RSA Hacked Encryption & Decryption')
