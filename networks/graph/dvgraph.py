from graph import Graph

class DVGraph(Graph):

    @classmethod
    def create_from_nodes(self, nodes, poison = False):
        return DVGraph(len(nodes), len(nodes), nodes)

    def __init__(self, row, col, nodes = None, poison = False):
        super(DVGraph, self).__init__(row, col, nodes)
        for node in self.nodes:
            node.graph = self
            node.poison = poison
            for node2 in self.nodes:
                if node == node2:
                    node.shortest_path_table[node.index] = (0, None)
                else:
                    node.shortest_path_table[node2.index] = (float("inf"), None)

    
    def set_poison(self, p):
        for node in self.nodes:
            node.poison = p

    def stabilize_nodes(self):
        self.update_nodes(0)


    def update_nodes(self,src):
        src = self.get_index_from_node(src)
        should_break = False
        iteration = 0
        conns = [node for (node, weight) in self.connections_from(src)]
        conns.insert(0, self.nodes[src])
        while not should_break:
            print("--------------")
            print(f"t{iteration}")
            old_dicts = []
            new_dicts = []
            next_conns = set()
            for node in conns:
                old_dicts.append(dict(node.shortest_path_table))
                print(f"Update {node.data}")
                node.queue_updates_for_shortest_path()
            for node in conns:
                node.update()
                new_dicts.append(dict(node.shortest_path_table))
            for i in range(len(old_dicts)):
                
                if old_dicts[i] != new_dicts[i]:
                    # print("***********")
                    # print(old_dicts[i])
                    # print(new_dicts[i])
                    # print("***********")
                    to_add_conns = self.connections_from(conns[i])
                    for (node, _ ) in to_add_conns:
                        next_conns.add(node)
            if len(next_conns) == 0:
                should_break = True
            iteration += 1
            conns = list(next_conns)

        
        
    # def update_nodes(self, starting_node, destination_node):
    #     starting_node, destination_node = self.get_index_from_node(starting_node), self.get_index_from_node(destination_node)
    #     connections = self.connections_from(starting_node)
    #     start_stop_conns = [[starting_node, destination_node, connections]]
    #     should_break = False
    #     while not should_break:
    #         next_ssconns = []
    #         for (start, dest, conns) in start_stop_conns:
    #             for (node, _) in conns:
    #                 prev_data = dict(node.shortest_path_table)
    #                 node.receive_info([start, dest, self.nodes[start].shortest_path_table[dest][0]])
    #                 node.update()
    #                 next_data = dict(node.shortest_path_table)
    #                 next_conns = []
    #                 if next_data != prev_data:
    #                     cconns = self.connections_from(node)
    #                     for c in cconns:
    #                         if c.index != dest:
    #                             next_conns.append(c)
    #                     next_ssconns.append([node.index, dest, next_conns])
    #         if len(next_ssconns) == 0:
    #             should_break = True
    #         start_stop_conns = next_ssconns