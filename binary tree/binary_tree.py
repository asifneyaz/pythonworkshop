"""Define a Node for binary tree. This set/get the value of the node, set/get the value of left/right child
      tree
      ----
       j    <-- root
     /   \
    f      k
  /   \      \
 a     h      z    <-- leaves
 """


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Python program to introduce Binary Tree

# A class that represents an individual node in a
# Binary Tree



# create root
root = Node(1)
''' following is the tree after above statement
		1
	/ \
	None None'''

root.left = Node(2)
root.right = Node(3)

''' 2 and 3 become left and right children of 1
		1
		/ \
		2	 3
	/ \ / \
None None None None'''


root.left.left = Node(4)
'''4 becomes left child of 2
		1
	/	 \
	2		 3
	/ \	 / \
4 None None None
/ \
None None'''



def printInorder(root):
    if root:

        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.data)

        # now recur on right child
        printInorder(root.right)


printInorder(root)

