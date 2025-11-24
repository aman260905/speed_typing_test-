import time
start_time=time.perf_counter()
for i in range(1000000):
    _= i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"elapsed time:{elapsed_time:.6f}seconds")
import math
def is_deficient(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    sum_proper_divisors = 1
    limit = int(math.sqrt(n))
    for i in range(2, limit + 1):
        if n % i == 0:
            sum_proper_divisors += i
            complementary_divisor = n // i
            if i * i != n:
                sum_proper_divisors += complementary_divisor
    return sum_proper_divisors < n
print(is_deficient(65))
print(is_deficient(23))
print(is_deficient(9))
print(is_deficient(75))
