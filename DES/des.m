clear all;
close all;
clc

A= dlmread("fog_blocks.csv");
x= A(:,1);
y= A(:,2);

hold on
plot(x,'-o');
plot(y,'-*');

legend('Encryption','Decryption','Location','NorthWest')
xlabel('Block Number'), ylabel('Encryption & Decryption Execution Time')
title(' Fog DES Encryption and Decryption ')

