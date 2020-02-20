from node import Node
from graph import Graph

z = Node("z")
y = Node("y")
x = Node("x")
v = Node("v")
t = Node("t")
u = Node("u")
w = Node("w")

nodes = [z,y,x,v,t,u,w]

g = Graph.create_from_nodes(nodes)

g.connect(z,y,12)
g.connect(z,x,8)
g.connect(x,y,6)
g.connect(x,w,6)
g.connect(x,v,3)
g.connect(y,t,7)
g.connect(y,v,8)
g.connect(t,v,4)
g.connect(t,u,2)
g.connect(v,w,4)
g.connect(v,u,3)
g.connect(w,u,3)

paths = g.dijkstra(x)

print( [(weight, [n.data for n in node]) for (weight, node) in paths])