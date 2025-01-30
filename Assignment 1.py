class Node:
    def __init__(self, data):
        self.data = data # assigns the given data to the node
        self.next = None # Initialize the next attribute to null

class LinkedList:
    def __init__(self):
        self.head = None # Initialize head as None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node


llist = LinkedList()
llist.append("first")
llist.append("linked")
llist.append("list")
llist.append(":)")

llist.prepend("my")
llist.prepend("is")
llist.prepend("This")

llist.print_list()

