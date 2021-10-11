n = input()
n = n.upper()

alpha = list(set(n))
num_count = []

for i in alpha:
    num_count.append(n.count(i))

#print(alpha)
#print(num_count)

if num_count.count(max(num_count)) > 1:
    print('?')
else:
    print(alpha[num_count.index(max(num_count))])