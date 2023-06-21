"""K nearest neighbours implementation

Returns:
    _type_: _description_
"""


import collections
import unittest
import numpy as np

class KNN:
	def __init__(self, k):
		self.k = k


	def fit(self, X, y):
		self.X_train = X
		self.y_train = y

	def euclidean_distance(self, pt1:np.ndarray, pt2:np.ndarray)->float:
		return np.sqrt(np.sum((pt1-pt2)**2))

	def predict(self, X):
		y_pred = [self._predict(x) for x in X]
		return np.array(y_pred)

	def _predict(self, x):
		distances = [self.euclidean_distance(x, x_train) for x_train in self.X_train]
		k_indices = np.argsort(distances)[:self.k]
		k_nearest_labels = [self.y_train[i] for i in k_indices]
		most_common = collections.Counter(k_nearest_labels).most_common(1)
		return most_common[0][0]

class TestSolution(unittest.TestCase):
	def test1(self):
		X_train = np.array([[1,2],[2,3],[110,100],[-5,-5],[-1,4],[4,-5]])
		y_train = ['a','b', 'c', 'd', 'e', 'f']
		
		knn = KNN(k=3)
		knn.fit(X_train, y_train)
		
		X_test = np.array([[0,0],[-1210, -100],[1200,-100],[-1300, -100],[1200, 101],[1200, 110],[4, -5]])
		pred = knn.predict(X_test)

		self.assertEquals(list(pred), ['a', 'c'])

if __name__ == '__main__':
		
	test = TestSolution()
	unittest.main()
		
