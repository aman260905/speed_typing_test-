import time
start_time = time.perf_counter() 
for i in range(1000000):
    _ = i * 2
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")
def is_prime_power(n):
    if n < 2:
        return False
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    for k in range(1, int(n.bit_length()) + 1):
        p = round(n ** (1 / k))
        if p ** k == n and is_prime(p):
            return True
    return False
print(is_prime_power(8))
print(is_prime_power(27))
print(is_prime_power(49))
print(is_prime_power(12))
print(is_prime_power(2))

