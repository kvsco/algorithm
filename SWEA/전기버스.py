from os import walk
import sys

sys.stdin = open("swea/전기버스.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    K,N,M = map(int, input().split())
    stop = list(map(int,input().split()))
    #print(K,N,M)
    #print(stop)
    # k : 한번에 갈수있는 최대 거리
    # n : 정류장 길이 마지막종점넘버
    # m : 주유소가있는 정류장 갯수
    
    a = 0 # 현위치
    b = K
    result = 0

    stop_list = [0] * (N+1)

    for i in range(len(stop)):
        stop_list[stop[i]] = 1
    #print(K,N,M)
    #print(stop_list)

    while True:
        tmp = 0
        for i in range(a+1, b+1):
            if stop_list[i] == 1:
                a = i #이동
            else:
                tmp += 1
        if tmp == K:
            result = 0
            break

        result += 1
        b = a + K

        if b >= N:
            break
    print(f"#{test_case} {result}")