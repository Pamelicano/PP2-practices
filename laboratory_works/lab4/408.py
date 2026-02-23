def primes(n):
    for num in range(2, n + 1):
        is_prime = True
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            yield num

n = int(input())
buf = []
for p in primes(n):
    buf.append(str(p))
    if len(buf) == 1000:
        print(" ".join(buf), end=" ")
        buf.clear()
if buf:
    print(" ".join(buf))