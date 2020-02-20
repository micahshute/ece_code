class BinaryTree:

    def __init__(self, nodes = []):
        self.nodes = nodes

    def root(self):
        self.nodes[0]
    
    def iparent(self, i):
        return (i - 1) // 2
    
    def ileft(self, i):
        return 2*i + 1

    def iright(self, i):
        return 2*i + 2

    def left(self, i):
        return self.node_at_index(self.ileft(i))
    
    def right(self, i):
        return self.node_at_index(self.iright(i))

    def parent(self, i):
        return self.node_at_index(self.iparent(i))

    def node_at_index(self, i):
        return self.nodes[i]

    def size(self):
        return len(self.nodes)
    
# bt = BinaryTree([5,7,18,2,9,13,4])
# print(bt.root())
# print(bt.left(0))
# print(bt.right(0))
# print(bt.parent(5))
# print(bt.parent(4))