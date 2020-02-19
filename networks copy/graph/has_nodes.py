from node import Node

class HasNodes:

    def __init__(self, nodes):
        self.nodes = nodes
        for i in range(len(nodes)):
            nodes[i].index = i

    def get_index_from_node(self, node):
        if not isinstance(node, Node) and not isinstance(node, int):
            raise ValueError("node must be an integer or a Node object")
        if isinstance(node, int):
            return node
        else:
            return node.index