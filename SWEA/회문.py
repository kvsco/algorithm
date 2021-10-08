import sys

sys.stdin = open("swea/회문.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m = map(int, input().split()) 
    # size : N x N
    # 회문길이 : M

    arr = [0 for _ in range(n) ]
    for i in range(n):
        arr[i] = list(input())
    #print(arr)

    #row 탐색
    for i in range(n):
        for j in range(n-m+1): # 회문길이는 m이니깐 앞에서부터 n-m+1 만큼 뺴면서 탐색
            palindrome = ''
            for k in range(j,n):
                palindrome += arr[i][k]
            #print(palindrome[:m]) # 앞에서부터 회문길이까지만.
            #print(palindrome[:m][::-1])
            if palindrome[:m] == palindrome[:m][::-1]:
                print(f"#{test_case} {palindrome[:m]}")
                break
    #colum 탐색
    for i in range(n):
        for j in range(n-m+1): #위와 동일
            palindrome = ''
            for k in range(j,n):
                palindrome += arr[k][i]
            if palindrome[:m] == palindrome[:m][::-1]:
                print(f"#{test_case} {palindrome[:m]}")
                break