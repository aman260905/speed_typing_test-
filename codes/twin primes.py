import time
start_time = time.perf_counter() 
for i in range(1000000):
    _ = i * 2
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")
def twin_primes(limit):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    twins = []
    prev_prime = None
    for num in range(2, limit + 1):
        if is_prime(num):
            if prev_prime is not None and num - prev_prime == 2:
                twins.append((prev_prime, num))
            prev_prime = num
    return twins
print(twin_primes(20))

