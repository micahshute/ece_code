from gnode import GNode
from graph import Graph

a = GNode("A")
b = GNode("B")
c = GNode("C")
d = GNode("D")
e = GNode("E")
f = GNode("F")

graph = Graph.create_from_nodes([a,b,c,d,e,f])

# graph.connect(a,b)
# graph.connect(a,c)
# graph.connect(a,e)
# graph.connect(b,c)
# graph.connect(b,d)
# graph.connect(c,d)
# graph.connect(c,f)
# graph.connect(d,e)

graph.connect(a,b,5)
graph.connect(a,c,10)
graph.connect(a,e,2)
graph.connect(b,c,2)
graph.connect(b,d,4)
graph.connect(c,d,7)
graph.connect(c,f,10)
graph.connect(d,e,3)

graph.print_adj_mat()