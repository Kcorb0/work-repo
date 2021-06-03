def largest_prime(n):
    prime_factor = 1
    i = 2

    while i <= (n / i):
        if n % i == 0:
            prime_factor = i
            n /= i
        else:
            i += 1

    if prime_factor < n:
        prime_factor = n

    return int(prime_factor)


print(largest_prime(600851475143))