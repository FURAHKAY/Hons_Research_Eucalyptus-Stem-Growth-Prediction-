import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def kmeans_clustering(data, k):
    # Step 1: Initialize centroids randomly
    centroids = np.random.choice(len(data), k, replace=False)
    centroids = data[centroids]

    print("Initial Centroids:")
    print(centroids)

    iteration = 0

    while True:
        # Step 2: Assign each data point to the nearest centroid
        labels = np.argmin(np.linalg.norm(data[:, np.newaxis] - centroids, axis=2), axis=1)

        print(f"\nIteration {iteration + 1} - Assignments:")
        print(labels)

        # Step 3: Update centroids based on the mean of assigned data points
        new_centroids = np.array([np.mean(data[labels == j], axis=0) for j in range(k)])

        print("\nUpdated Centroids:")
        print(new_centroids)

        # Step 4: Check for convergence
        if np.array_equal(centroids, new_centroids):
            break

        centroids = new_centroids
        iteration += 1

    return labels, centroids

def visualize_clusters(data, labels, centroids):
    plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', alpha=0.5, edgecolors='k', linewidths=0.5)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=100, label='Centroids')
    plt.title('k-Means Clustering')
    plt.xlabel('Gene 1 Expression Level')
    plt.ylabel('Gene 2 Expression Level')
    plt.legend()
    plt.show()

# Scenario Explanation:
# Suppose we have gene expression data representing the expression levels of two genes (Gene 1 and Gene 2)
# for a set of samples. We want to use k-Means clustering to identify clusters of samples based on their
# gene expression patterns.

# Desired Response:
# The algorithm should output the initial centroids, the assignments of each sample to clusters in each iteration,
# and the final centroids. The visualization will show the identified clusters and the final centroid positions.

# Example data (replace this with your own bioinformatics data)
np.random.seed(42)
gene_data = np.concatenate([np.random.normal(loc=5, scale=1, size=(50, 2)),
                            np.random.normal(loc=10, scale=1, size=(50, 2)),
                            np.random.normal(loc=15, scale=1, size=(50, 2))])

# Number of clusters (k)
num_clusters = 3

# Run k-Means clustering
labels, centroids = kmeans_clustering(gene_data, num_clusters)

# Visualize the final clusters and centroids
visualize_clusters(gene_data, labels, centroids)
