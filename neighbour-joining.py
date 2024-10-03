import numpy as np
from Bio import Phylo
import matplotlib.pyplot as plt

def neighbour_joining(D, taxa):
    n = len(D)
    
    # Base case: if there are only two taxa, create a tree with two branches
    if n == 2:
        tree = Phylo.BaseTree.Tree()
        tree.root = Phylo.BaseTree.Clade()
        tree.root.clades.append(Phylo.BaseTree.Clade(name=taxa[0]))
        tree.root.clades.append(Phylo.BaseTree.Clade(name=taxa[1]))
        return tree

    # Function to calculate the total distance of a taxon
    total_dist = lambda i: sum(D[i, :])

    # Calculate the Q matrix using the Neighbour-Joining formula
    Q = np.zeros_like(D, dtype=float)
    for i in range(n):
        for j in range(n):
            if i != j:
                Q[i, j] = (n - 2) * D[i, j] - total_dist(i) - total_dist(j)

    # Find the indices (i, j) with the minimum Q value
    i, j = np.unravel_index(np.argmin(Q), Q.shape)

    # Calculate the values needed for tree construction
    delta_ij = (total_dist(i) - total_dist(j)) / (n - 2)
    limb_length_i = 0.5 * (D[i, j] + delta_ij)
    limb_length_j = 0.5 * (D[i, j] - delta_ij)

    # Create a new taxon with the calculated limb lengths
    new_taxon = f"({taxa[i]}:{limb_length_i},{taxa[j]}:{limb_length_j})"
    
    # Remove the original taxa i and j and add the new taxon
    taxa.pop(max(i, j))
    taxa.pop(min(i, j))
    taxa.append(new_taxon)

    # Update the distance matrix with the new taxon
    D_new = np.zeros((n - 1, n - 1), dtype=float)
    for k in range(n - 1):
        if k != i and k != j:
            D_new[k, -1] = 0.5 * (D[i, k] + D[j, k] - D[i, j])
            D_new[-1, k] = D_new[k, -1]

    for m in range(n - 2):
        for k in range(n - 1):
            if k != i and k != j:
                D_new[k, m] = D[k, m]

    D_new[-1, -1] = 0

    # Recursively call the function with the updated distance matrix and taxa list
    return neighbour_joining(D_new, taxa)

def visualize_tree(tree):
    Phylo.draw(tree, do_show=False)
    plt.show()

# Example distance matrix
distance_matrix = np.array([
    [0, 5, 9, 9],
    [5, 0, 10, 10],
    [9, 10, 0, 8],
    [9, 10, 8, 0]
])

# Example taxa labels
taxa_labels = ['A', 'B', 'C', 'D']

# Run neighbour joining algorithm
nj_tree = neighbour_joining(distance_matrix, taxa_labels)

# Visualize the tree
visualize_tree(nj_tree)
