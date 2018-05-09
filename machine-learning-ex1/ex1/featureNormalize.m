function [X_norm, mu, sigma] = featureNormalize(X)
%FEATURENORMALIZE Normalizes the features in X 
%   FEATURENORMALIZE(X) returns a normalized version of X where
%   the mean value of each feature is 0 and the standard deviation
%   is 1. This is often a good preprocessing step to do when
%   working with learning algorithms.

% You need to set these values correctly
data = load('ex1data2.txt');
x = data(:,1:2);
y = data(:,3);
m = length(y);

X_norm = x;
mu = []; sigma = [];
for i = 1: size(x)(2)
  mu = [mu; (sum(x(:,i))/m)];
  sigma = [sigma; max(x(:,i)) - min(x(:,i))];
end
display(mu);display(sigma)

% ====================== YOUR CODE HERE ======================
% Instructions: First, for each feature dimension, compute the mean
%               of the feature and subtract it from the dataset,
%               storing the mean value in mu. Next, compute the 
%               standard deviation of each feature and divide
%               each feature by it's standard deviation, storing
%               the standard deviation in sigma. 
%
%               Note that X is a matrix where each column is a 
%               feature and each row is an example. You need 
%               to perform the normalization separately for 
%               each feature. 
%
% Hint: You might find the 'mean' and 'std' functions useful.
%  
t = (x(1) - mu(1)) / sigma(1)
tmp = []
for i = 1: size(x)(2)
  tmp = [tmp (x(:,i) - mu(i)) / sigma(i)]
end
  
X_norm = tmp

display(X_norm(1,1))







% ============================================================

end
