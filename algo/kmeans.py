import numpy as np

def kmeans(data, K):
    # Initialize random cluster centroids
    centroids = initialize_centroids(data, K)
    
    # Initialize cluster assignments and track convergence
    old_centroids = None
    labels = np.zeros(data.shape[0])
    
    # Iterate until convergence
    while not np.array_equal(old_centroids, centroids):
        old_centroids = centroids
        
        # Assign data points to clusters
        labels = assign_clusters(data, centroids)
        
        # Update cluster centroids
        centroids = update_centroids(data, labels, K)
    
    return centroids, labels

def initialize_centroids(data, K):
    indices = np.random.choice(data.shape[0], K, replace=False)
    centroids = data[indices]
    return centroids

def assign_clusters(data, centroids):
    distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)
    labels = np.argmin(distances, axis=1)
    return labels

def update_centroids(data, labels, K):
    centroids = np.zeros((K, data.shape[1]))
    for k in range(K):
        cluster_points = data[labels == k]
        centroids[k] = np.mean(cluster_points, axis=0)
    return centroids


import numpy as np
import unittest

class KMeansTestCase(unittest.TestCase):
    def test_kmeans(self):
        # Test case 1
        data1 = np.array([[1, 2], [2, 1], [10, 12], [12, 10]])
        K1 = 2
        centroids1, labels1 = kmeans(data1, K1)
        self.assertEqual(centroids1.shape[0], K1)
        self.assertEqual(labels1.shape[0], data1.shape[0])

        # Test case 2
        data2 = np.array([[1, 2], [2, 1], [3, 4], [4, 3], [10, 12], [12, 10], [13, 11]])
        K2 = 3
        centroids2, labels2 = kmeans(data2, K2)
        self.assertEqual(centroids2.shape[0], K2)
        self.assertEqual(labels2.shape[0], data2.shape[0])

        # Test case 3
        data3 = np.array([[1, 2], [2, 1]])
        K3 = 1
        centroids3, labels3 = kmeans(data3, K3)
        self.assertEqual(centroids3.shape[0], K3)
        self.assertEqual(labels3.shape[0], data3.shape[0])

if __name__ == '__main__':
    unittest.main()
