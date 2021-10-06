import sys

sys.stdin = open("swea/구간합.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    num_list = list(map(int, input().split()))

    sum_list = [0] * (N-K+1)
    for i in range(len(sum_list)):
        sum_Num = 0

        for j in range(0,K):
            #print(f"i: {i} j: {j} sum: {i+j}")
            sum_Num +=num_list[i+j]
        sum_list[i] = sum_Num
    print(f"#{test_case} {max(sum_list) - min(sum_list)}" )