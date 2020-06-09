clear all;
close all;
clc

A= dlmread("respnse_time.csv");
x= A(:,1);
y= A(:,2);

hold on
plot(x, '-o');
plot(y, '-*');


legend('Fog Response Time','Cloud Response Time', 'Location', 'NorthWest')
xlabel('Block Number(unit)'), ylabel(' Time (sec)')
title('Fog and Cloud Response Time of Proposed Algorithm')
