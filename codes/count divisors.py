import time
start_time = time.perf_counter() 
for i in range(1000000):
    _ = i * 2
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")
def count_divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
        i += 1
    return count
print(count_divisors(6))
print(count_divisors(10))
print(count_divisors(36))
