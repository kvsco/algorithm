# Breadth 넓이 우선 탐색 DFS 보다 BFS가 연산속도 조금 더 빠름.
from collections import deque


def bfs(graph, start, visited):
    # queue
    q = deque([start])
    visited[start] = True  # 현재 노드 방문체크

    while q:
        print(q)
        v = q.popleft()
        print(v, end=' ')

        for i in graph[v]:  #
            if not visited[i]:  # 방문안했다면.
                q.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

# print(graph[1])
bfs(graph, 1, visited)
