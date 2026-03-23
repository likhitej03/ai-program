def dfs_limited(graph, start, target, limit):
    if start == target:
        return True
    if limit <= 0:
        return False
    for neighbor in graph.get(start, []):
        if dfs_limited(graph, neighbor, target, limit - 1):
            return True
    return False

def iddfs(graph, start, target, max_depth):
    for depth in range(max_depth + 1):
        if dfs_limited(graph, start, target, depth):
            return True
    return False

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(iddfs(graph, 'A', 'F', 3))  # Output: True