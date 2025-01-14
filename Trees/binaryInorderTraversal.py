class BinaryInorderSubtree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insert(root, val):
    if root is None:
        root = BinaryInorderSubtree(val)
        return root

    if val < root.data:
        root.leftChild = insert(root.leftChild, val)

    if val > root.data:
        root.rightChild = insert(root.rightChild, val)
    return root


def inorder(root):
    if root is None:
        return

    inorder(root.leftChild)
    print(root.data)
    inorder(root.rightChild)


root = insert(None, 15)
insert(root, 10)
insert(root, 25)
insert(root, 6)
insert(root, 14)
insert(root, 20)
insert(root, 60)
inorder(root)


def inorderTraversal(self, root: BinaryInorderSubtree):
    def inorder(root):
        nonlocal res
        if root:
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

    res = []
    inorder(root)
    return res
