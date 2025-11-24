import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"Elapsed time:{elapsed_time:.6f} seconds")
def count_divisors(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    count = 2
    limit = int(n**0.5)
    for i in range(2, limit + 1):
        if n % i == 0:
            if i * i != n:
                count += 2
            else:
                count += 1
    return count
def is_highly_composite(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    divisors_of_n = count_divisors(n)
    for i in range(1, n):
        divisors_of_i = count_divisors(i)
        if divisors_of_i >= divisors_of_n:
            return False
    return True
print(f"Is 12 highly composite? {is_highly_composite(12)}")
print(f"Is 18 highly composite? {is_highly_composite(18)}")
print(f"Is 24 highly composite? {is_highly_composite(24)}")
