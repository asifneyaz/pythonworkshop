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
        if BinaryTreeNode.getLeft() is not None:
            q.put(BinaryTreeNode.getLeft())
        if BinaryTreeNode.getRight() is not None:
            q.put(BinaryTreeNode.getRight())


class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    #Set Data
    def setData(self,data):
        return self.data
    #get Data
    def getData(self):
        return self.data
    def getData(self):
        return self.data
    #get left child of node
    def getLeft(self):
        return self.left
    #get right child
    def getRight(self):
        return self.right


