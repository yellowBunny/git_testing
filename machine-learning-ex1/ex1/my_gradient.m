function theta = my_gradiend(X, y, theta, alpha, m)
  
tmp_theta = theta;

for i = 1: length(theta)
  tmp_theta(i) = theta(i) - alpha * (1/m * sum((((X * theta) - y) .* X(:,i))));
end

theta = tmp_theta;




  
