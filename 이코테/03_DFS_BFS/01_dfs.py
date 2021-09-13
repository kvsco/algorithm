# -*- coding: utf-8 -*-
def dfs(graph, v, visited):
    #현재노드 방문처리
    visited[v] = True
    print(v)

    #현재노드와 연결된 다른노드 재귀호출
    for i in graph[v]:
        print('현재i')
        print(i)
        if not visited[i]: # False이면 방문 X, True 이면 방문한 노드임.
            dfs(graph, i, visited)

#인접리스트 graph
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9
#print(visited)
#노드 1번부터 시작
dfs(graph, 1, visited)