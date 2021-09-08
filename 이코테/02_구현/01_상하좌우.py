# 110p예제
# -*- coding: utf-8 -*-
n = int(input())

s = input().split() # 이동방향
x,y = 1,1

m_type = ['L','R','U','D']
m_x = [0, 0, -1, 1]
m_y = [-1, 1, 0, 0]
# L 일때 x 좌표그대로 y좌표 -1

for i in s:
    for j in range(4):
        if i == m_type[j]:
            nx = x + m_x[j]
            ny = y + m_y[j]
    if nx < 1 or ny < 1 or nx > n or ny > n: # 지도 공간 n x n 의 범위벗어나는경우 x,y값 non-update 
        continue
    else:
        x,y = nx, ny
print(x,y)
