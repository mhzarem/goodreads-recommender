import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sparse

class SpectralGraph:

    def __init__(self, name):
        self.name = name

    def make_graph(self, *matrix):
        if not matrix:
            graph = nx.Graph()
            graph.add_edges_from([(1, 2), (2, 3), (1, 3), (5, 7)])
            return graph

        else:
            graph = nx.from_numpy_matrix(matrix)
            return graph


example = SpectralGraph("test")
g = example.make_graph()
nx.spectral_layout(g)
nx.draw(g, with_labels = True)
c = nx.to_numpy_matrix(g)
print(c)
print("first")
c2 = c.dot(c)
print(c2)
print("c2")
print(c2.dot(c))
plt.show()
plt.axis('off')
a = nx.laplacian_spectrum(g)
b = nx.algebraic_connectivity(g)
c = nx.adjacency_spectrum(g)
# print(a)

