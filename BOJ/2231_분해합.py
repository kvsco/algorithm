n = int(input())

for i in range(0,n):
    a=0
    num_str = str(i) # 분해합구하기위해 문자열로 변환
    
    for j in num_str:
        a += int(j)
    
    if a + i == n:
        print(i)
        break

    if i == n-1: # for문 끝까지 탐색했을시. 없다고판단
        print(0)



    
    