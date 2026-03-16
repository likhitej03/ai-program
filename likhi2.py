class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        # Add edge u -> v
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)

    def dfs_recursive(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(f"Visited (recursive): {start}")
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)
        return visited

    def dfs_iterative(self, start):
        visited = set()
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(f"Visited (iterative): {vertex}")
                visited.add(vertex)
                # Add neighbors to stack
                stack.extend(reversed(self.graph[vertex]))
        return visited

    def detect_cycle_util(self, v, visited, rec_stack):
        visited.add(v)
        rec_stack.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                if self.detect_cycle_util(neighbor, visited, rec_stack):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(v)
        return False

    def detect_cycle(self):
        visited = set()
        rec_stack = set()
        for node in self.graph:
            if node not in visited:
                if self.detect_cycle_util(node, visited, rec_stack):
                    return True
        return False

    def connected_components(self):
        visited = set()
        components = []
        for node in self.graph:
            if node not in visited:
                comp = []
                self._dfs_component(node, visited, comp)
                components.append(comp)
        return components

    def _dfs_component(self, node, visited, comp):
        visited.add(node)
        comp.append(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self._dfs_component(neighbor, visited, comp)



g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')
g.add_edge('E', 'F')
g.add_edge('F', 'C') 

print("Recursive DFS starting from A:")
g.dfs_recursive('A')

print("\nIterative DFS starting from A:")
g.dfs_iterative('A')

print("\nCycle detection:")
print("Cycle found!" if g.detect_cycle() else "No cycle detected.")

print("\nConnected components:")
print(g.connected_components())
