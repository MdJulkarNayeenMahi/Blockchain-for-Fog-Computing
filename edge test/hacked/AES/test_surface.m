% data = dlmread("hacked.csv");

test = dlmread('.csv');
x=test(:,1);
y=test(:,2);
z=test(:,3);

surf(x,y,z);
