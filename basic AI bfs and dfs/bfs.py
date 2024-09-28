from collections import deque
def bfs(graph, start):
    q = deque([start])
    visited=set()

    while q:
        node=q.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)




graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


bfs(graph, 'A')
