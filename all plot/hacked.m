clear all;
close all;
clc

A= dlmread("hacked.csv");
x= A(:,1);
y= A(:,2);
z= A(:,3);

hold on
plot(x, '-o');
plot(y, '-*');
plot(z, '-+');

legend('AES Encryption', 'DES Encryption','RSA Encryption', 'Location', 'NorthWest')
xlabel('Block Number(Unit)'), ylabel('Execution Time (sec)')
title(' Edge AES,DES & RSA Hacked Encryption')
