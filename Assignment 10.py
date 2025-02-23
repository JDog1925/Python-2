class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_rec(self.root, data)

    def insert_rec(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_rec(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                 self.insert_rec(node.right, data)

    def in_order(self):
        return self.in_order_rec(self.root)

    def in_order_rec(self, node):
        if node is None:
            return []
        return self.in_order_rec(node.left) + [node.data] + self.in_order_rec(node.right)

    def pre_order(self):
        return self.pre_order_rec(self.root) 

    def pre_order_rec(self, node):
        if node is None:
            return[]
        return [node.data] + self.pre_order_rec(node.left) + self.pre_order_rec(node.right)

    def post_order(self):
        return self.post_order_rec(self.root)

    def post_order_rec(self, node):
        if node is None:
            return []
        return self.post_order_rec(node.left) + self.post_order_rec(node.right) + [node.data]

if __name__ == "__main__":
    binarytree = BinaryTree()
    binarytree.insert(50)
    binarytree.insert(30)
    binarytree.insert(20)
    binarytree.insert(40)
    binarytree.insert(70)
    binarytree.insert(60)
    binarytree.insert(80)

    print("In Order: ", binarytree.in_order())
    print("In Pre Order: ", binarytree.pre_order())
    print("In Post Order: ", binarytree.post_order())
