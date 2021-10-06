import sys

sys.stdin = open("swea/숫자카드.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = input()
    num_list = input()
    
    num_box = [0] * 10
    
    for i in num_list:
        num = int(i)
        num_box[num] += 1

    num_max = max(num_box)

    i = 9
    while True:
        
        if num_box[i] == num_max:
            print(f"#{test_case} {i} {num_max}")
            break
        else:
            i = i-1