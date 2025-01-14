def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    list1, list2 = [], []
    res1 = dfs(arrayOne, list1)
    res2 = dfs(arrayTwo, list2)

    if res1 == res2:
        return True
    return False


def dfs(tree, arr):
    if tree is None:
        return

    dfs(tree.left, arr)
    arr.append(tree.value)
    dfs(tree.right, arr)
    return arr


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):

        # Write your code here.
        # Do not edit the return statement of this method.
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self


root1 = BST(10)
root1.insert(15)
root1.insert(8)
root1.insert(12)
root1.insert(94)
root1.insert(81)
root1.insert(5)
root1.insert(2)
root1.insert(11)

root2 = BST(10)
root2.insert(8)
root2.insert(5)
root2.insert(15)
root2.insert(2)
root2.insert(12)
root2.insert(11)
root2.insert(94)
root2.insert(81)

out = sameBsts(root1, root2)
print(out)


