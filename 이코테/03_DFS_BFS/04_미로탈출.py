from collections import deque

n, m = map(int, input().split(' '))

graph = []
# 맵 제작
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)


def bfx(x, y):
