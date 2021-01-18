class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class binarytree(object):
    def __init__(self,root):
        self.root= Node(root)

tree = binarytree(4)
tree.root.left = Node(4)
tree.root.right = Node(5)

#   4
#  / \
# 4   5
#