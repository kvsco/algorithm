import sys

sys.stdin = open("swea/부분집합의합.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    x = len(A)
    N,K = map(int,input().split())

    cnt = 0
    for i in range(1<<x):
        #매 부분집합마다 초기화
        mylist = []
        sum = 0
        for j in range(x):
            if i & (1<<j):
                mylist.append(A[j])
                sum += A[j]
        if len(mylist) == N and sum == K :
            cnt += 1
    print(f'#{test_case} {cnt}')