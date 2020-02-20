from node import Node
from graph import Graph

##############################################################
######################### Use ################################
##############################################################

# Make 4 nodes (Locations as Data)
pool = Node("Pool")
hideout = Node("Secret Hideout")

g = Graph.create_from_nodes([pool, hideout])

# Connect nodes in the adjxacency matrix
g.connect(pool, hideout)

# View current adjacency matrix
print("2x2 adjacency matrix")
g.print_adj_mat()


# Add new nodes
library = Node("Library")
beach = Node("Beach")
g.add_node(library)
g.add_node(beach)

# Connect new nodes
g.connect(pool, beach)
g.connect(hideout, library)

print("New 4x4 adjacency matrix:")
g.print_adj_mat()

# Print out connections to a certain node
print([node[0].data for node in g.connections_to(hideout)])



# Use bfs() to breadth-first-search
coalarr = []
for _ in range(20):
    coalarr.append(Node("coal"))

goldarr = []
for _ in range(3):
    goldarr.append(Node("gold"))

g = Graph.create_from_nodes(coalarr + goldarr)

starting_node = coalarr[0]
ending_node = goldarr[0]

g.connect(0,1)
g.connect(0,2)
g.connect(0,3)
g.connect(20, 3)
g.connect(1,4)
g.connect(2,5)
g.connect(5,0)
g.connect(3,6)
g.connect(6,7)
g.connect(5,8)
g.connect(6,9)
g.connect(3,10)
g.connect(9,10)
g.connect(10,11)
g.connect(10,12)
g.connect(12,13)
g.connect(13,14)
g.connect(14,15)
g.connect(15,16)
g.connect(15,18)
g.connect(18,17)
g.connect(18,19)
g.connect(17,21)
g.connect(19,22)

search = lambda node: node.data == "gold"
bfs_res = g.bfs(starting_node, search)
if bfs_res == ending_node:
    print("BFS algorithm works")


print([node[0].data for node in g.connections_to(g.connections_to(starting_node)[2][0])])

print([node for node in g.connections_to(1)])

# Make weighted graph
n1 = Node("Library")
n2 = Node("Gryffindor Common Room")
n3 = Node("Dungeons")
n4 = Node("Hogsmeade")
n5 = Node("Shrieking Shack")
n6 = Node("Hufflepuff Common Room")
n7 = Node("Great Hall")
n8 = Node("Whomping Willow")
weighted = Graph.create_from_nodes([n1, n2, n3, n4, n5, n6, n7, n8])

weighted.connect(n1, n2, 10)
weighted.connect(n1, n4, 20)
weighted.connect(n3, n4, 5)
weighted.connect(n1, n3, 2)
weighted.connect(n3, n5, 7)
weighted.connect(n8, n5, 1)
weighted.connect(n8, n7, 4)
weighted.connect(n6, n7, 1)
weighted.connect(n7, n1, 6)
weighted.connect(n7, n2, 3)
# weighted.connect(n1, n8, 9)


# Test weights
# Get weights and nodes connected to n1
print([(node_weight[0].data, node_weight[1]) for node_weight in weighted.connections_to(n1)])

# Test dijkstra's alg
print()
print("Dijsktra's Test: Distances from 'Whomping Willow'")
print()
# print([(weight, [n.data for n in node]) for (weight, node) in weighted.dijkstra(n8)])
print([(weight, [n.data for n in node]) for (weight, node) in weighted.dijkstra(n1)])
# Next steps notes: Implement a heap for dijksras alg to change from O(n^2) to O(nlgn)
# 
# I also will put a depth-first search in the graph 