import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"Elapsed time:{elapsed_time:.6f} seconds")
import math
def mobius(n):
    if n == 0:
        return 0
    n = abs(n)
    cnt = 0
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            cnt += 1
            x //= p
            if x % p == 0:
                return 0
        p += 1
    if x > 1:
        cnt += 1
    return 1 if cnt % 2 == 0 else -1
print(mobius(30))
print(mobius(67))
print(mobius(4))
