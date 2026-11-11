class Graph:
    def __init__(self):
        # Using an adjacency list to represent the graph nodes and edges
        self.graph = {}

    def add_edge(self, u, v):
        # Adds an undirected edge between node u and node v
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        print("Graph Adjacency List:")
        for node, neighbors in self.graph.items():
            print(f"{node} -> {', '.join(neighbors)}")


# Example usage based on Assessment 3.3 (using letters from last name "Y A R E S"):
if __name__ == "__main__":
    g = Graph()
    # Adding edges based on your graph diagram structure
    g.add_edge('Y', 'A')
    g.add_edge('Y', 'R')
    g.add_edge('A', 'E')
    g.add_edge('A', 'S')

    g.display()