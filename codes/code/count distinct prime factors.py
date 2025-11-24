import time
start_time = time.perf_counter() 
for i in range(1000000):
    _ = i * 2
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")
def count_distinct_prime_factors(n):
    count = 0
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            count += 1
            while n % factor == 0:
                n //= factor
        factor += 1
    if n > 1:
        count += 1
    return count
print(count_distinct_prime_factors(6573465))
print(count_distinct_prime_factors(66678))
print(count_distinct_prime_factors(3))
print(count_distinct_prime_factors(345))
