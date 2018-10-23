import numpy as np
import pandas as pd

class Lineary_regression:

    def save_to_txt(self, path=r'C:\Users\seb\Desktop\m2.csv'):
        data = self.open_csv_file(path)
        with open(r'C:\Users\seb\Desktop\mm2.txt', 'a') as file:
            for i in range(data.shape[0]):
                for val in data.values[i]:
                    to_write = str(val) + ','
                    file.write(to_write)
                else:
                    file.write('\n')
        return 'Done'


    def open_csv_file(self, path=r'C:\Users\seb\Desktop\m2.csv'):
        file = pd.read_csv(path, delimiter=';')
        # print(type(file))
        file = file.fillna(file.mean(axis=0))
        # print(file)
        return file

    def create_X_and_Y(self, matrix):
        matrix = np.array(matrix)
        X = matrix[:,1:]
        ones = np.ones(X.shape[0])
        X_with_ones = np.insert(X, 0, ones, axis=1)
        Y = matrix[:,0]
        theta = np.zeros(X_with_ones.shape[1])
        return X_with_ones, Y, theta

    def cost_function(self, x, y, theta):
        m = y.shape[0]
        hx = x @ theta # similar like x * theta in octave
        # print(t.shape)
        # print(y.shape)
        J = sum((hx - y) ** 2) / (2 * m)
        return J

    def mean_normalization(self, x):
        x = x[:, 1:]
        self.mu = x.mean(0)
        self.sigma = x.std(0, ddof=1)
        x_norm = np.zeros(x.shape[0]).reshape(x.shape[0],1)
        for j in range(len(self.mu)):
            x_norm = np.column_stack((x_norm, (x[:,j] - self.mu[j]) / self.sigma[j]))
        x_norm = np.insert(x_norm,1, np.ones(x_norm.shape[0]).reshape(x_norm.shape[0]), axis=1)
        return x_norm[:,1:], self.mu, self.sigma

    def predict_value_normalization(self, x, mu, sigma):
        pred_norm = np.array([])
        x = x[1:]
        for i in range(x.shape[0]):
            val = (x[i] - mu[i]) / sigma[i]
            pred_norm = np.insert(pred_norm, i, val, 0)
        pred_norm = np.insert(pred_norm,0,1,0)
        return pred_norm

    def gradient_descend(self, x, y, theta, alpha, iterations):
        m = x.shape[0]
        tmp_theta = np.zeros(x.shape[1])
        tmp_J = self.cost_function(x,y,theta)
        for i in range(iterations):
            for j in range(len(tmp_theta)):
                tmp_theta[j] = theta[j] - alpha * sum((x @ theta - y) * x[:,j] / m)
            else:
                theta = tmp_theta
                J = self.cost_function(x,y,theta)
                if J > tmp_J:
                    return 'somthing goes wrong'
                else:
                    tmp_J = J
                # print(J)
        return theta, J

path = r'C:\Users\seb\Desktop\m2.csv'
start = Lineary_regression()
matrix = start.open_csv_file(path)
print(matrix)
x, y, theta = start.create_X_and_Y(matrix)
# print(start.cost_function(x, y, theta))
x_norm, mu, sigma = start.mean_normalization(x)
theta_g, J = start.gradient_descend(x_norm, y, theta, .01, 6000)
p = np.array([1, 144, 4, 2, 300])
p_norm = start.predict_value_normalization(p, mu, sigma)
print('Prediction is')
print(p_norm @ theta_g)
