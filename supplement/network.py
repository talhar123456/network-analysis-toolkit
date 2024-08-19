from node import Node
from typing import Dict, List, Union

class Network:
    def __init__(self, undirected=True, allow_self_edges=False):
        # Initializes the network with certain properties - whether it's undirected and if it allows self-edges.
        
        
        self.nodes = dict()                                                     # type: Dict[Union[int, str], Node]
        self.undirected = undirected                                            # type: bool
        self.allow_self_edges = allow_self_edges                                # type: bool

    def size(self) -> int:
        """
        Returns the number of nodes in the network.

        """
        return len(self.nodes)

    def add_node(self, node: Node):
        
        if node.identifier in self.nodes:
            raise ValueError("Node with the same identifier already exists")
        self.nodes[node.identifier] = node

    def get_node(self, node: Union[int, str, Node]) -> Node:
        # Retrieves a node from the network based on its identifier.
        if isinstance(node, Node):
            if node.identifier not in self.nodes:
                raise KeyError("Node does not exist in the network")
            return self.nodes[node.identifier]
        
        elif node in self.nodes:
            return self.nodes[node]
        else:
            raise KeyError("Node does not exist in the network")

    def edge_exists(self, node_1: Union[str, int, Node], node_2: Union[str, int, Node]) -> bool:
        # Checks if an edge exists between two nodes in the network.
        
        node_1 = self.get_node(node_1)
        node_2 = self.get_node(node_2)
        return node_2 in node_1.neighbour_nodes or (self.undirected and node_1 in node_2.neighbour_nodes)

    def add_edge(self, node_1: Union[str, int, Node], node_2: Union[str, int, Node]):
        
        node_1 = self.get_node(node_1)
        node_2 = self.get_node(node_2)
        if self.edge_exists(node_1, node_2):
            raise ValueError("Edge already exists")
        node_1.add_edge(node_2)
        if self.undirected:
            node_2.add_edge(node_1)

    def remove_edge(self, node_1: Union[str, int, Node], node_2: Union[str, int, Node]):
        
        node_1 = self.get_node(node_1)
        node_2 = self.get_node(node_2)
        if not self.edge_exists(node_1, node_2):
            raise ValueError("Edge does not exist")
        node_1.remove_edge(node_2)
        if self.undirected:
            node_2.remove_edge(node_1)

    def degree_histogram(self) -> List[int]:
        # Computes the histogram of node degrees in the network, i.e., how many nodes have each degree.
        max_degree = self.max_degree()
        histogram = [0] * (max_degree + 1)

        for node in self.nodes.values():
            degree = node.degree()
            histogram[degree] += 1

        return histogram
    
    def normalized_degree_distribution(self) -> List[float]:
        # Computes the normalized degree distribution, which is the probability distribution of the degrees of nodes in the network.
        
        histogram = self.degree_histogram()
        total_nodes = sum(histogram)
        normalized_distribution = [count / total_nodes for count in histogram]

        return normalized_distribution

    def max_degree(self) -> int:
        """
        Computes the highest node degree in the network.

        """
        max_degree = 0
        for node in self.nodes.values():
            degree = node.degree()
            if degree > max_degree:
                max_degree = degree
        return max_degree
