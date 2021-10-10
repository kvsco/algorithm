t = int(input()) # test case 

for i in range(t):
   n, s = input().split(" ")
   n = int(n)
   sentence = ''
   for sp in s:
       sentence += sp*n
   print(sentence)


    