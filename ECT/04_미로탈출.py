from collections import deque

n, m = map(int, input().split(' '))

graph = []
# ๋งต ์ ์
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)


def bfx(x, y):
