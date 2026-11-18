class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Binary tree (Assessment 3.5 diagram)
#
#               L
#            /     \
#          Y         C
#         / \       / \
#        H   A     Y   A
#       /     \   /
#      R       E S

r = Node("R")
h = Node("H", left=r)
e = Node("E")
a1 = Node("A", right=e)
y1 = Node("Y", left=h, right=a1)

s = Node("S")
y2 = Node("Y", left=s)
a2 = Node("A")
c = Node("C", left=y2, right=a2)

root = Node("L", left=y1, right=c)


# DFS methods (recursive)
def preorder(node, order):
    # Root -> Left -> Right
    if node:
        order.append(node.value)
        preorder(node.left, order)
        preorder(node.right, order)
    return order


def inorder(node, order):
    # Left -> Root -> Right
    if node:
        inorder(node.left, order)
        order.append(node.value)
        inorder(node.right, order)
    return order


def postorder(node, order):
    # Left -> Right -> Root
    if node:
        postorder(node.left, order)
        postorder(node.right, order)
        order.append(node.value)
    return order


# DFS preorder using a stack (iterative)
def tree_dfs(root):
    order = []
    stack = [root]
    while stack:
        node = stack.pop()
        order.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order


print("Preorder DFS :", " - ".join(preorder(root, [])))
print("Inorder DFS  :", " - ".join(inorder(root, [])))
print("Postorder DFS:", " - ".join(postorder(root, [])))
print("Stack DFS    :", " - ".join(tree_dfs(root)))