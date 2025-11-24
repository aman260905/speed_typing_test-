import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"Elapsed time:{elapsed_time:.6f} seconds")
def prime_pi(n):
    if n < 2:
        return 0
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    p = 2
    while p * p <= n:
        if sieve[p]:
            for i in range(p*p, n+1, p):
                sieve[i] = False
        p += 1
    return sum(sieve)
print(prime_pi(10))
print(prime_pi(100))
print(prime_pi(374))
