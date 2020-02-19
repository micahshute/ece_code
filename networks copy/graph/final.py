from node import Node
from dvnode import DVNode
from dvgraph import DVGraph


a = DVNode("a")
b = DVNode("b")
c = DVNode("c")

g = DVGraph.create_from_nodes([a,b,c])

print(c.shortest_path_table)

g.connect(a,b,1)
g.connect(b,c,1)


g.stabilize_nodes()
print(a.shortest_path_table)
print(b.shortest_path_table)

# print("Count to infinity test")
# g.remove_conn(b,c)
# g.update_nodes(a)
# print(a.shortest_path_table)
# print(b.shortest_path_table)


print("No count to infinity test")
g.remove_conn(b,c)
g.set_poison(True)
g.update_nodes(b)
print("A Shortest Path Table:")
print(a.shortest_path_table)
print()
print("B Shortest Path Table:")
print(b.shortest_path_table)