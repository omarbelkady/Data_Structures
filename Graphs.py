from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}  # Format: {vertex: [(neighbor, weight), ...]}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, u, v, weight=None):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append((v, weight))
    
    def delete_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
        for u in self.graph:
            self.graph[u] = [(v, w) for v, w in self.graph[u] if v != vertex]
    
    # DFS Traversal (Returns Visited Nodes in DFS Order)
    def dfs(self, start):
        visited = []
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                for neighbor, _ in self.graph.get(node, []):
                    stack.append(neighbor)
        return visited
    
    # BFS Traversal (Returns Visited Nodes in BFS Order)
    def bfs(self, start):
        visited = []
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                for neighbor, _ in self.graph.get(node, []):
                    queue.append(neighbor)
        return visited
    
    # DFS Search (Check if Target is Reachable)
    def dfs_search(self, start, target):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node == target:
                return True
            if node not in visited:
                visited.add(node)
                for neighbor, _ in self.graph.get(node, []):
                    stack.append(neighbor)
        return False
    
    # BFS Search (Check if Target is Reachable)
    def bfs_search(self, start, target):
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node == target:
                return True
            if node not in visited:
                visited.add(node)
                for neighbor, _ in self.graph.get(node, []):
                    queue.append(neighbor)
        return False

# Example Usage
g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")

print("DFS Traversal:", g.dfs("A"))          
print("BFS Traversal:", g.bfs("A"))          
print("DFS Search (D):", g.dfs_search("A", "D"))
print("BFS Search (E):", g.bfs_search("A", "E"))  