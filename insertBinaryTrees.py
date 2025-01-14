class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)

                else:
                    self.left.insert(data)

            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)

                else:
                    self.right.insert(data)

        else:
            self.data = data
            print(data)

    def getValue(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    print('No value found')
                else:
                    return self.left.getValue(data)
            elif data > self.data:
                if self.right is None:
                    print("No value found")
                else:
                    return self.right.getValue(data)
            else:
                return str(self.data) + "is found"

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()


# Use the insert method to add nodes
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)

root.PrintTree()

print(root.getValue(15))