# 113p예제
# -*- coding: utf-8 -*-
# a~h , 1~8 나이트의 위치

knight = input()
#최대범위
max_range = 8 # 8x8 체스판

x_type = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8 }
x = x_type[knight[0]]
y = int(knight[1])
print(f"knight의 좌표:{x,y}")

count = 0
# 이동가능 방향 :  좌 - 위아래        우 - 위아래        위 - 좌우       아래 - 좌우
movetype = [ (-2,-1), (-2, 1), (2,-1), (2,1), (1,2), (-1,2), (1,-2), (-1,-2) ]

for i in movetype:
    print(f'현재step:{i}')
    ax = i[0]
    ay = i[1]
    nx = x + ax
    ny = y + ay
    print(nx,ny)

    if nx < 1 or ny < 1 or nx > max_range or ny > max_range:
        continue
    else:
        count += 1

print(f'이동가능한 경로의 수: {count}')