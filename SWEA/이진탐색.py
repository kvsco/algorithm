import sys

sys.stdin = open("swea/이진탐색.txt", "r")

T = int(input())

def pages(start, end, goal, cnt):
    c = int((start+end)/2)
    
    if c == goal:
        cnt = cnt + 1
        return cnt
    if goal > c:
        cnt = cnt + 1
        return pages(c,end,goal,cnt)

    elif goal < c:
        cnt = cnt+ 1
        return pages(start,c,goal,cnt)

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    r,pa,pb = map(int,input().split())
    start = 1
    cnt = 0
    cnt_a = pages(start, r, pa, cnt) # 1~400 300p
    cnt_b = pages(start, r, pb, cnt) # 1~400 350p
    #print(cnt_a,cnt_b)

    if cnt_a<cnt_b :
        print(f"#{test_case} A")
    elif cnt_a == cnt_b:
        print(f"#{test_case} 0")
    else:
        print(f"#{test_case} B")

    


