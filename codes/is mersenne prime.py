import time
start_time = time.perf_counter() 
for i in range(1000000):
    _ = i * 2
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")
def is_mersenne_prime(p):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if not is_prime(p):
        return False
    mersenne = 2 ** p - 1
    return is_prime(mersenne)
print(is_mersenne_prime(2))
print(is_mersenne_prime(3))
print(is_mersenne_prime(5))
print(is_mersenne_prime(11))
print(is_mersenne_prime(4))
