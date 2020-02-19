from node import Node
from binary_heap import MinHeap

class DijkstraNodeDecorator:
    
    def __init__(self, node):
        self.node = node
        self.prov_dist = float('inf')
        self.hops = []

    def index(self):
        return self.node.index

    def data(self):
        return self.node.data
    
    def update_data(self, data):
        self.prov_dist = data['prov_dist']
        self.hops = data['hops']
        return self
    


class Graph: 


    def __init__(self, nodes):
        self.adj_list = [ [node, []] for node in nodes ]
        for i in range(len(nodes)):
            nodes[i].index = i


    def connect_dir(self, node1, node2, weight = 1):
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        # Note that the below doesn't protect from adding a connection twice
        self.adj_list[node1][1].append((node2, weight))

    def connect(self, node1, node2, weight = 1):
        self.connect_dir(node1, node2, weight)
        self.connect_dir(node2, node1, weight)

    
    def connections(self, node):
        node = self.get_index_from_node(node)
        return self.adj_list[node][1]
    
    def get_index_from_node(self, node):
        if not isinstance(node, Node) and not isinstance(node, int):
            raise ValueError("node must be an integer or a Node object")
        if isinstance(node, int):
            return node
        else:
            return node.index

    def dijkstra(self, src):
        
        src_index = self.get_index_from_node(src)
        # Map nodes to DijkstraNodeDecorators
        # This will initialize all provisional distances to infinity
        dnodes = [ DijkstraNodeDecorator(node_edges[0]) for node_edges in self.adj_list ]
        # Set the source node provisional distance to 0 and its hops array to its node
        dnodes[src_index].prov_dist = 0
        dnodes[src_index].hops.append(dnodes[src_index].node)
        # Set up all heap customization methods
        is_less_than = lambda a, b: a.prov_dist < b.prov_dist
        get_index = lambda node: node.index()
        update_node = lambda node, data: node.update_data(data)

        #Instantiate heap to work with DijkstraNodeDecorators as the hep nodes
        heap = MinHeap(dnodes, is_less_than, get_index, update_node)

        min_dist_list = []

        while heap.size() > 0:
            # Get node in heap that has not yet been "seen"
            # that has smallest distance to starting node
            min_decorated_node = heap.pop()
            min_dist = min_decorated_node.prov_dist
            hops = min_decorated_node.hops
            min_dist_list.append([min_dist, hops])
            
            # Get all next hops. This is no longer an O(n^2) operation
            connections = self.connections(min_decorated_node.node)
            # For each connection, update its path and total distance from 
            # starting node if the total distance is less than the current distance
            # in dist array
            for (inode, weight) in connections: 
                node = self.adj_list[inode][0]
                heap_location = heap.order_mapping[inode]
                if(heap_location is not None):
                    tot_dist = weight + min_dist
                    if tot_dist < heap.nodes[heap_location].prov_dist:
                        hops_cpy = list(hops)
                        hops_cpy.append(node)
                        data = {'prov_dist': tot_dist, 'hops': hops_cpy}
                        heap.decrease_key(heap_location, data)

        return min_dist_list 




a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

g = Graph([a,b,c,d,e,f])

g.connect(a,b,5)
g.connect(a,c,10)
g.connect(a,e,2)
g.connect(b,c,2)
g.connect(b,d,4)
g.connect(c,d,7)
g.connect(c,f,10)
g.connect(d,e,3)

print([(weight, [n.data for n in node]) for (weight, node) in g.dijkstra(a)])