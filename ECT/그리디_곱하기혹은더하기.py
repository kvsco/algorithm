# Q2 곱하거나 더하거나

s = input()

num_list = []
#for idx,i in enumerate(s):
for i in s:
  num_list.append(int(i))

# 0,1 일때 더하기 ==>> **1이하일때**
result = 0

for i in num_list:
  if i <=1 or result <=1:
    result += i
  else:
    result *= i   
  
print(f"만들수있는가장큰수:{result}")
