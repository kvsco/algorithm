'''
import sys

sys.stdin = open("swea/ㅇㅇㅇ.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    pass
'''

#비트연산자로 부분집합
arr = [1,2,3]
n = len(arr)

for i in range(1 << n): # n=3 : 1000(2) = 8
    for j in range(n): # 한자리씩, 원소 0,1,2개 확인 
        if i & (1<<j): # i 인덱스와 순차 0,1,2 교집합이있을경우
            print(arr[j], end=' ')
    print()


print(5 & 4) # 0101 & 0100 => 둘다1인거 => 0100 = 4
print(3 & 4) # 0011 & 0100 => 둘다1인거 => 0000 = 0

print(3 & (1<<0) ) # 0011 & 0001 = 1
print(3 & (1<<1) ) # 0011 & 0010 = 2
print(3 & (1<<2) ) # 0011 & 0100 = 0
'''
j = 0 (0000) , 1 (0001) , 2 (0010)
i = 0 = 0000  x
  = 1 = 0001  1
  = 2 = 0010  2
  = 3 = 0011  1,2
  = 4 = 0100  3
  = 5 = 0101  1,3
  = 6 = 0110  2,3
  = 7 = 0111  1,2,3
'''