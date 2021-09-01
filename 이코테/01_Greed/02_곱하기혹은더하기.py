# Q2 곱하거나 더하거나

s = input()

#print(s)
num_first = None
sum = 0
for i in s:
  if num_first is None:
    num_first = i
  else:
    if '0' or '1' in num_first+i:
      sum = int(i)+int(num_first)
      num_first = i
    else:
      sum = int(i)*int(num_first)
      num_first = i

print(f"만들어지는 가장 큰 수:{sum}")
