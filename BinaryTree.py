
from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_tree():
    e = Node("E")
    s = Node("S")
    a = Node("A", left=e, right=s)
    r = Node("R")
    y = Node("Y", left=a, right=r)
    return y


def tree_bfs(root):
    order = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        order.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


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


root = build_tree()
print("Binary tree BFS:", " - ".join(tree_bfs(root)))
print("Binary tree DFS:", " - ".join(tree_dfs(root)))