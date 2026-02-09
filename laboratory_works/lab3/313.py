def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

a = list(map(int, input().split()))
primes = list(filter(lambda x: is_prime(x), a))
if primes:
    print(*primes)
else:
    print("No primes")