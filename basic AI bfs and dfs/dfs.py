def dfs(graph, start, visited=None):
    if visited == None:
        visited = set()
    if start not in visited:
        visited.add(start)
        print(start)
    neighbors = graph[start]
    for neighbor in neighbors:
        dfs(graph, neighbor, visited=visited)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph, 'A')
