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


# Graph
graph = {
    "Y": ["A", "R"],
    "A": ["Y", "E"],
    "R": ["Y", "S"],
    "E": ["A", "S"],
    "S": ["R", "E"],
}


def graph_dfs(graph, start):
    order = []
    visited = set()

    def dfs(vertex):
        visited.add(vertex)
        order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return order


print("Binary tree DFS:", " - ".join(tree_dfs(root)))
print("Graph DFS:", " - ".join(graph_dfs(graph, "Y")))