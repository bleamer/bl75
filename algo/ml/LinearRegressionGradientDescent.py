
# Gradient Descent with linear regression
import numpy as np
class LinearRegressionGD:
    def __init__(self, learning_rate = 0.1, max_iter=100, tolerance=1e-6):
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.tolerance = tolerance
        self.weights = None
        self.bias = None

    def fit(self, X, y):


        n_samples, n_features = X.shape

        self.weights = np.zeros(n_features)
        self.bias = 0

        for i in range(self.max_iter):
            y_pred = np.dot(X, self.weights) + self.bias

            # Compute gradients
            # basically derivative of d/dx 1/samples * sum(y-y_hat)^2
            dw = - (2 / n_samples) * np.dot(X.T, (y - y_pred))
            db = - (2/ n_samples) *(np.sum(y - y_pred))

            # update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

            if np.linalg.norm(dw, 2) < self.tolerance and abs(db) < self.tolerance:
                break

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias


import unittest

class Tests(unittest.TestCase):
    def test1(self):
        
        #Sample DAta
        X = np.array([[1],[2],[3],[4],[5]])
        y = np.array([3,6,9,12,15])

        model = LinearRegressionGD(learning_rate=0.01, max_iter=5000)
        model.fit(X, y)

        X_test = np.array([[11],[22],[33],[44],[55]])
        y_true = np.array([33, 66, 99, 132, 165])
        y_pred = model.predict(X_test)

        differences = abs(y_true - y_pred)
        self.assertTrue(np.all(differences < 0.5)), "results not matching"

        print(y_pred)


if __name__ == '__main__':
    unittest.main()
