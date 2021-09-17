# 113p예제
# -*- coding: utf-8 -*-
# 00 : 00 : 00 ~ N : 59 : 59 안에 3이 포함되는경우 모두 카운팅
n = int(input())

count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            time = str(i)+':'+str(j)+":"+str(k)
            print(f'시간 time : {time}')
            if '3' in time:
                count += 1
print(count) 