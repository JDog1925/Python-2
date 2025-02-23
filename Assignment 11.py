class Node:
    def __init__(self, value):
        self.value = value  # value of node
        self.left = None  # left child
        self.right = None  # right child

class BinarySearchTree:
    def __init__(self):
        self.root = None # Root of tree

    def insert(self, value):
        # New value into BST
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        #help fuction to recursively insert a value
        if value < node.value:
            #put into left subtree
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert_recursive(node.left,value)
        else:
            #put in right subtree
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert_recursive(node.right, value)

    def search(self, value):
        #search for value in BST
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        #helps fucntion recursively search for a value
        #node is None or value is found
        if node is None:
            return False
        if node.value == value:
            return True
        #value smaller search left subtree
        if value < node.value:
            return self._search_recursive(node.left, value)
        # larger search right subtree
        else:
            return self._search_recursive(node.right, value)

#cases
if __name__ == "__main__":
    bst = BinarySearchTree()
    #values
    bst.insert(55)
    bst.insert(35)
    bst.insert(25)
    bst.insert(45)
    bst.insert(75)
    bst.insert(65)
    bst.insert(85)
#searching for values
print("Search for 45:", bst.search(45))# return True
print("Search for 40:", bst.search(40))# return False
print("Search for 75:", bst.search(75))# return True
print("Search for 100:", bst.search(100))# return False
print("Search for 85:", bst.search(85)) #return True
