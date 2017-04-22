# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    lst = [0, 1]
    for i in range (2, n+1):
        lst.append(lst[i-1] + lst[i-2])
    return lst.pop()

n = int(input())
print(calc_fib(n))
