from node import Node
from graph import Graph

# from binary_tree import BinaryTree


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

w_graph = Graph.create_from_nodes([a,b,c,d,e,f])

w_graph.connect(a,b,5)
w_graph.connect(a,c,10)
w_graph.connect(a,e,2)
w_graph.connect(b,c,2)
w_graph.connect(b,d,4)
w_graph.connect(c,d,7)
w_graph.connect(c,f,10)
w_graph.connect(d,e,3)

print([(weight, [n.data for n in node]) for (weight, node) in w_graph.dijkstra(a)])



# bt = BinaryTree()