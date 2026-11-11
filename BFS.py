from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Binary tree
e = Node("E")
s = Node("S")
a = Node("A", left=e, right=s)
r = Node("R")
root = Node("Y", left=a, right=r)


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


# Graph
graph = {
    "Y": ["A", "R"],
    "A": ["Y", "E"],
    "R": ["Y", "S"],
    "E": ["A", "S"],
    "S": ["R", "E"],
}


def graph_bfs(graph, start):
    order = []
    visited = {start}
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


print("Binary tree BFS:", " - ".join(tree_bfs(root)))
print("Graph BFS:", " - ".join(graph_bfs(graph, "Y")))