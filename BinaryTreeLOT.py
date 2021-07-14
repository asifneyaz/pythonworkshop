import queue


def level_order(root, result):
    if root is None:
        return
    q = queue.Queue()
    q.put(root)
    node = None

    while not q.empty():
        node = q.get()
        result.append(node.getData())
        if BinaryTreeNode.get_left() is not None:
            q.put(BinaryTreeNode.get_left())
        if BinaryTreeNode.get_right() is not None:
            q.put(BinaryTreeNode.get_right())


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    #Set Data

    def set_data(self, data):
        return self.data
    #get Data

    def get_data(self):
        return self.data

    #get left child of node
    def get_left(self):
        return self.left

    #get right child

    def get_right(self):
        return self.right


