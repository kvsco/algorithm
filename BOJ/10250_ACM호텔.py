t = int(input())

for i in range(t):
    H,W,N = map(int, input().split())
    
    floor = N%H
    
    ho = (N//H)+1

    if floor == 0 :
        floor = H #꼭대기층.
        ho -= 1 # 넘어가서 +1호 되서
    print(floor*100 + ho)
    