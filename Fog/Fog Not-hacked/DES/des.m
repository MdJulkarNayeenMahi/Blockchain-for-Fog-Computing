clear all;
close all;
clc

A= dlmread("Not_hacked.csv");
x= A(:,1);
y= A(:,2);

hold on
plot(x,'-o');
plot(y,'-*');
legend('Encryption','Decryption','Location','NorthWest')
xlabel('Block Number'), ylabel('Encryption & Decryption Execution Time')
title('Cloud Not Hacked Blocks Through DES Encryption and Decryption')


