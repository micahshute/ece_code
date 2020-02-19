from node import Node
from dvnode import DVNode
from dvgraph import DVGraph

a = DVNode("a")
b = DVNode("b")
c = DVNode("c")
d = DVNode("d")
e = DVNode("e")

g = DVGraph.create_from_nodes([a,b,c,d,e])

print(c.shortest_path_table)

g.connect(a,b,1)
g.connect(b,c,1)
g.connect(c,d,1)
g.connect(d,e,1)

g.stabilize_nodes()

# shortest_path_table returns {destination_index: (length, next_hop_index)}
print(e.shortest_path_table)
print(c.shortest_path_table)

# Test breaking link between d and e causes count to infinity
# WORKS
# print("Count to infinity test")
# g.remove_conn(d,e)
# g.update_nodes(d)
# print(d.shortest_path_table)

# Test breaking link between d and e does not cause count to infinity when poisoned
print("No count to infinity test")
g.remove_conn(d,e)
g.set_poison(True)
g.update_nodes(d)
print(d.shortest_path_table)


# Test HW Problem CH5 P11
print()
print()
print("------------- TEST HOMEWORK PROBLEM -----------------")
print()
print()
w = DVNode("w")
x = DVNode("x")
y = DVNode("y")
z = DVNode("z")

g = DVGraph.create_from_nodes([w,x,y,z])

g.connect(w, y, 1)
g.connect(w, z, 1)
g.connect(y, x, 4)
g.connect(x, z, 50)
g.connect(y, z, 3)

g.stabilize_nodes()

g.connect(y, x, 60)
g.update_nodes(y)

print()
print()
print("------------- NOW WITH POISON REVERSE -----------------")
print()
print()
g = DVGraph.create_from_nodes([w,x,y,z])

g.connect(w, y, 1)
g.connect(w, z, 1)
g.connect(y, x, 4)
g.connect(x, z, 50)
g.connect(y, z, 3)
g.set_poison(True)
g.stabilize_nodes()

g.connect(y, x, 60)
g.update_nodes(y)

