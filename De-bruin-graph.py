import networkx as nx
import matplotlib.pyplot as plt

# Function to generate a De Bruijn graph given k and a list of sequences
def generate_de_bruijn_graph(k, sequences):
    # Create a directed graph
    graph = nx.DiGraph()

    # Iterate through each sequence in the list
    for seq in sequences:
        # Iterate through each k-mer in the sequence
        for i in range(len(seq) - k + 1):
            # Extract the k-mer
            kmer = seq[i:i+k]

            # Add the k-mer as a node if it doesn't exist in the graph
            if not graph.has_node(kmer):
                graph.add_node(kmer)

            # If there is a next position in the sequence, extract the next k-mer
            if i + k < len(seq):
                next_kmer = seq[i+1:i+k+1]

                # Add the next k-mer as a node if it doesn't exist in the graph
                if not graph.has_node(next_kmer):
                    graph.add_node(next_kmer)

                # Add an edge from the current k-mer to the next k-mer if it doesn't exist
                if not graph.has_edge(kmer, next_kmer):
                    graph.add_edge(kmer, next_kmer)

    # Return the generated De Bruijn graph
    return graph

# Function to visualize the De Bruijn graph
def visualize_graph(graph):
    # Define the layout for visualization
    pos = nx.circular_layout(graph)

    # Draw the graph with labels, node attributes, and styling
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=1000, font_size=10)

    # Show the graph visualization
    plt.show()

# Example usage
sequences = ['ATGCG', 'TGCGT', 'GCGTA', 'CGTAC', 'GTACG']
k_value = 3

# Generate the De Bruijn graph
de_bruijn_graph = generate_de_bruijn_graph(k_value, sequences)

# Print the nodes and edges in the De Bruijn graph
print("Nodes in the De Bruijn Graph:")
print(de_bruijn_graph.nodes())

print("\nEdges in the De Bruijn Graph:")
print(de_bruijn_graph.edges())

# Visualize the De Bruijn graph
visualize_graph(de_bruijn_graph)
