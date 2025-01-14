# This is the class of the input root. Do not edit it.
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Insert Node
    def insert(self, data):
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

    # Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


def branchSums(root):
    # Write your code here.
    stack = []
    traverseBinarySums(root, 0, stack)
    return stack


def traverseBinarySums(root, sum_val, stack):
    if root is None:
        return
    print(root.data)
    sum_val += root.data
    if root.left is None and root.right is None:
        stack.append(sum_val)
        return

    traverseBinarySums(root.left, sum_val, stack)
    traverseBinarySums(root.right, sum_val, stack)


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.PrintTree())
print(branchSums(root))
