from typing import Set, Union

class Node:
    def __init__(self, identifier: Union[str, int]):
        
        self.identifier = identifier                                                # type: Union[str, int]
        # contains the Node-objects that are targets of this node
        self.neighbour_nodes = set()                                                # type: Set[Node]

    def __str__(self) -> str:
        
        return str(self.identifier) if isinstance(self.identifier, int) else f'\'{self.identifier}\''

    def __eq__(self, obj) -> bool:
        # Checks if two nodes are equal by comparing their identifiers.
        if not isinstance(obj, Node):
            return False
        return self.identifier == obj.identifier

    def __hash__(self) -> int:
        # Generates a hash value for the node based on its identifier.
        return hash(self.identifier)

    def has_edge_to(self, node) -> bool:
        
        return node in self.neighbour_nodes

    def add_edge(self, node):
        
        if self.has_edge_to(node):
            raise ValueError("Edge already exists")
        self.neighbour_nodes.add(node)

    def remove_edge(self, node):
        
        if not self.has_edge_to(node):
            raise ValueError("Edge does not exist")
        self.neighbour_nodes.remove(node)

    def degree(self) -> int:
        # Returns the degree of this node, which is the number of neighboring nodes.
        return len(self.neighbour_nodes)
