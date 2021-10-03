#모험가길드
#n명의 모험가, 공포도 x

n = input()
x = list(map(int,input().split()))

x.sort() # 정렬
num_group = 0
count = 1

for i in x:
  if i == count:
    num_group+=1
    count = 1
  else:
    count+=1
print(f"최대그룹: {num_group}")
