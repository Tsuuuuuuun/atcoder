N,M = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(M)]

def dfs(u, visited, graph):
    visited[u] = True
    max_length = 0
    for v, w in graph[u]:
        if not visited[v]:
            max_length = max(max_length, w + dfs(v, visited, graph))
    visited[u] = False
    return max_length

def max_path_length_dfs(N, M, roads):
    graph = {i: [] for i in range(1, N + 1)}

    # Create adjacency list
    for a, b, c in roads:
        graph[a].append((b, c))
        graph[b].append((a, c))

    max_length = 0
    for start in range(1, N + 1):
        visited = [False] * (N + 1)
        max_length = max(max_length, dfs(start, visited, graph))

    return max_length

result = max_path_length_dfs(N, M, roads)
print(result)