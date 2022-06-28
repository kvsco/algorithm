# -*- coding: utf-8 -*- 
import sys
sys.setrecursionlimit(10**6)

def factorial(result):
    print(result)

    if result > 1:
        return result * factorial(result-1)
    else:
        return 1

n = factorial(100000)
print(n)

# 최대 깊이 n = 995 ,  996부터 RecursionError: maximum recursion depth exceeded while calling a Python object