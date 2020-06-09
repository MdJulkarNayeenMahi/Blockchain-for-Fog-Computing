clear all;
close all;
clc

%A= dlmread("hacked.csv");
A= dlmread("proposed_not_hacked02.csv");
x= A(:,1);
x1= A(:,2);
y= A(:,3);
y1= A(:,4);
z= A(:,5);
z1= A(:,6);
%r = sqrt(x.^2 + y.^2) + eps;



xlin = linspace(min(x),max(x),80);
ylin = linspace(min(y),max(y),80);

x1lin = linspace(min(x1),max(x1),80);
y1lin = linspace(min(y1),max(y1),80);

[X,Y] = meshgrid(xlin,ylin);
[X1,Y1] = meshgrid(x1lin,y1lin);
f = scatteredInterpolant(x,y,z);
f1 = scatteredInterpolant(x1,y1,z1);
Z = f(X,Y);
Z1 = f1(X1,Y1);

figure
mesh(X,Y,Z) %interpolated
mesh(X1,Y1,Z1)
axis tight; hold on
plot3(x,y,z,'-*','MarkerSize',15) %nonuniform
plot3(x1,y1,z1,'-o','MarkerSize',15) %nonuniform

legend('Linspace','Encryption','Decryption',   'Location', 'NorthWest')
xlabel('DES algorithm'), ylabel('RSA algorithm'), zlabel('Proposed algorithm')
title('Not Hacked through DES, RSA and Proposed Algorithm (Edge)')