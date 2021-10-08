import sys

sys.stdin = open("swea/글자수.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    list_str1 = list(set(str1))
    dic = {}
    for i in list_str1:
        dic[i] = 0
        
        for j in str2:
            if i == j:
                dic[i] += 1
    
    max_num = 0
    for i in list_str1:
        if dic[i] > max_num:
            max_num = dic[i]
    print(f'#{test_case} {max_num}')

    
    
            