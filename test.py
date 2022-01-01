from tensordrug.data.graph import Graph
from tensordrug.data.molecule import Molecule
from tensordrug.core.core import Registry as R

# Create graph that uses networkx
edge_list = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]
graph = Graph(edge_list, num_nodes=6)
subgraph = graph.subgraph([2, 3, 4])
graph.visualize()

# Create molecule from smiles definition

mol = Molecule.from_smiles("C1=CC=CC=C1")
print(mol.node_feature)
print(mol.atom_type)
print(mol.to_scaffold())
