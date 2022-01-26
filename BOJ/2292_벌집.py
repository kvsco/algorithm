n = int(input())

bee = 1
count = 1

while n > bee:
    bee += 6*count # 벌집 크기는 6배수로 증가
    count += 1 
    
print( count)  