def factorial(result):
    print(result)

    if result > 1:
        return result * factorial(result-1)
    else:
        return 1

n = factorial(996)
print(n)