import sys

sys.stdin = open("swea/색칠하기.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input()) # 갯수

    m = [['']*10 for _ in range(10)]
    for i in range(N):
        x1,y1,x2,y2,color = map(int, input().split())

        for i in range(x1,x2+1,1):
            for j in range(y1,y2+1,1):
                if color == 1:
                    m[i][j] += 'R'
                else:
                    m[i][j] += 'B'
    cnt = 0
    #맵 사이즈 10x10
    for i in range(10):
        for j in range(10):    
            if 'R' in m[i][j] and 'B' in m[i][j]:
                cnt += 1
    print(f"#{test_case} {cnt}")
    


    

