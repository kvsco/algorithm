n, m = map(int, input().split(' '))
graph = []

# 맵제작 0,1
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    # 맵 벗어나는경우 false
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상하좌우 각각 재귀 dfs 실행. 방문한곳 1로 채우기.
        # 해당 재귀함수 속에서 또 다른 인접dfs상하좌우 모두 탐색하여 전부다 1로 채우고 리턴 T
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


result = 0  # 나올수있는 아이스크림 갯수
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)
