from node import Node

class DVNode(Node):

    def __init__(self, data, indexloc = None):
        super(DVNode, self).__init__(data, indexloc)

        # key: dest_node, value: (dist, next_hop)
        self.shortest_path_table = {}
        self.graph = None
        self.unupdated_info = []
        self.poison = False
        
    def receive_info(self, node_info):
        self.unupdated_info.append(node_info)
        print(f"{self.data} receives {self.graph.nodes[node_info[0]].data} to {self.graph.nodes[node_info[1]].data}: Dist: {node_info[2]}")


    def reset_node_table(self):
        for node in self.graph.nodes:
            if node == self:
                self.shortest_path_table[self.index] = (0, None)
            else:
                self.shortest_path_table[node.index] = (float("inf"), None)

    def update(self):
        # info should be [sender_index, destination_index, dist]
        self.reset_node_table()
        for data in self.unupdated_info:
            c_sender = self.graph.get_weight(self, data[0])
            if c_sender > 0 and c_sender + data[2] < self.shortest_path_table[data[1]][0]:
                self.shortest_path_table[data[1]] = (c_sender + data[2], data[0])
                # print(f"Update SPT: {self.data} to {self.graph.nodes[data[1]].data}: {c_sender + data[2]}")     
        print(f"Updated SPT for {self.data}: {self.shortest_path_table}")
        self.unupdated_info = []


    def route_possibilities(self, dest):
        conns = self.graph.connections_from(self)
        return [weight + node.shortest_path_table[dest] for (weight, node) in conns]

    def queue_updates_for_shortest_path_for_dest(self, dest):
        conns = self.graph.connections_from(self)
        for (node, _) in conns:
            if self.poison and node.shortest_path_table[dest][1] == self.index:
                self.unupdated_info.append([node.index, dest, float("inf")])
            else:
                self.unupdated_info.append([node.index, dest, node.shortest_path_table[dest][0]])
        # print(self.unupdated_info)

    def queue_updates_for_shortest_path(self):
        for node in range(len(self.graph.nodes)):
            self.queue_updates_for_shortest_path_for_dest(node)

    # def update(self):
    #     conns = self.graph.connections_to(self)
    #     for (node, weight) in conns:
    #         self.shortest_path_table


    # def get_path(self, node, requester):
    #     if self.shortest_path_table[node.index][1] == requester.index:
    #         return (float("inf"), None)
    #     return self.shortest_path_table[node.index][0]