import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time= end_time-start_time
print(f"Elapsed time: [{elapsed_time:.6f}seconds")
import math
def is_abundant(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 1:
        return False
    total = 1
    limit = int(math.isqrt(n))
    for i in range(2, limit + 1):
        if n % i == 0:
            total += i
            j = n // i
            if j != i and j != n:
                total += j
    return total > n
print(is_abundant(12))
print(is_abundant(30))
print(is_abundant(667))
