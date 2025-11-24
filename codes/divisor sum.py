import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"Elapsed time:{elapsed_time:.6f} seconds")
import math
def divisor_sum(n):
    if n <= 0:
        return 0
    total = 0
    limit = int(math.isqrt(n))
    for i in range(1, limit+1):
        if n % i == 0:
            total += i
            j = n // i
            if j != i:
                total += j
    return total
print(divisor_sum(12))
print(divisor_sum(90))
print(divisor_sum(1442))
