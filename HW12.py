def fib(n):
    fib1 = 1
    fib2 = 1
    print(fib1, fib2, end=' ')
    while n-2 > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n = n-1
        print(fib2, end=' ')
