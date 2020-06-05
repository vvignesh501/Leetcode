class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current_node = self.head
        current_node.next = new_node
        while current_node is not None:
            print(current_node.data, "->")
            current_node = current_node.next
        print("None")

g = LinkedList()
g.append(1)
g.append(2)
