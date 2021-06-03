def fib(n):
    result = []
    a, b = 0, 1
    even = []

    while a < n:
        result.append(a)
        a, b = b, a + b
        print(f"{a}")
        if a % 2 == 0:
            even.append(a)
    print(a)
    return sum(even)


print(fib(400000000))
