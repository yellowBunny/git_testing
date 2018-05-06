
data = load('ex1data1.txt');
X = data(:,1);
X = [ones(length(X),1), X];
y = data(:,2);
m = length(y);
theta = [0;1];
alpha = 0.01;
iterations = 100;
%theta = my_gradient(X, y, theta, alpha, m)
figure;
hold on;
plot(X(:, 2), y, 'rx', 'MarkerSize',5)
xlabel('x')
ylabel('h(x)')
gen = 0
for i = 1: iterations
  theta = my_gradient(X, y, theta, alpha, m);
  J = computeCost(X, y, theta);
  %h_x = X * theta;
  %plot(X(:,2), h_x, '-')
  gen += 1;
  
end
h_x = X * theta;
plot(X(:,2), h_x, '-')
text(25,25,'%s',gen)
hold off