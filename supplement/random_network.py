from node import Node
from network import Network
import random

class RandomNetwork(Network):
    def __init__(self, n_nodes=0, n_edges=0):
        # initilaizer
        if n_nodes < 0 or n_edges < 0:
            raise ValueError("Number of nodes and edges cannot be negative")

        if n_edges > n_nodes * (n_nodes - 1) / 2:
            raise ValueError("Number of edges is larger than possible for the given number of nodes")

        super().__init__(undirected=True, allow_self_edges=False)

        # Create nodes
        for i in range(n_nodes):
            self.add_node(Node(i))

        # Create edges
        edges_added = 0
        while edges_added < n_edges:
            node_1 = random.choice(list(self.nodes.values()))
            node_2 = random.choice(list(self.nodes.values()))
            if node_1 != node_2 and not self.edge_exists(node_1, node_2):
                self.add_edge(node_1, node_2)
                edges_added += 1
