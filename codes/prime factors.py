import time
start_time=time.perf_counter()
for i in range(1000000):
    _= i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"elapsed time:{elapsed_time:.6f}seconds")
def prime_factors(n):
    if n <= 1:
        return []
    factors = []
    d = 2
    while n % d == 0:
        factors.append(d)
        n //= d
    d = 3
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 2
    if n > 1:
        factors.append(n)
    return factors
print(prime_factors(32))
print(prime_factors(3))
print(prime_factors(6783453))
print(prime_factors(88))
