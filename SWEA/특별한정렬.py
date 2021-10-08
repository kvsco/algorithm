import sys

sys.stdin = open("swea/특별한정렬.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    num_list = list(map(int, input().split()))
    result = []

    for i in range(n):
        if i%2 ==0 :
            bol = False
        else:
            bol = True
        num_list = sorted(num_list, reverse=bol)
        #print(num_list)
        result.append(num_list.pop())
    a = ''
    for i in range(10):
        a += f'{result[i]} '
    print(f"#{test_case} {a}")