

data = load('ex1data1.txt');
X = data(:, 1); y = data(:, 2);
m = length(y); % number of training examples
X = [ones(m, 1), data(:,1)]; % Add a column of ones to x
theta = zeros(2, 1); % initialize fitting parameters



J = 0
theta

J = sum(( X * theta -y) .** 2) / 2/m
theta = theta - (alpha/m*sum(( (( X * theta -y) .** 2) .*X))).'
