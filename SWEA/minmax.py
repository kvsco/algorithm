import sys

sys.stdin = open("swea/minmax.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # print(test_case)
    N = input()
    # print(N)
    numList = list(map(int, input().split()))
    # print(numList)
    mx_num = max(numList)
    mn_num = min(numList)

    print(f'#{test_case} {mx_num-mn_num}')
    # ///////////////////////////////////////////////////////////////////////////////////
