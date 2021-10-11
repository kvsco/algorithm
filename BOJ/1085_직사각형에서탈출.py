x,y,w,h = map(int, input().split())

len_list = [x-0, y-0, w-x, h-y]

print(min(len_list))
