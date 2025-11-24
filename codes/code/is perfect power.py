import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"Elapsed time:{elapsed_time:.6f} seconds")
import math
def is_perfect_power(n: int) -> bool:
    if n <= 3:
        return n == 1 
    max_b = math.floor(math.log2(n))
    for b in range(2, max_b + 1):
        try:
            a = round(n ** (1 / b))
        except OverflowError:
            continue
        if a > 1 and a**b == n:
            return True
    return False
n1 = 8
print(f"Is {n1} a perfect power? -> {is_perfect_power(n1)}")
n2 = 125
print(f"Is {n2} a perfect power? -> {is_perfect_power(n2)}")
n3 = 10
print(f"Is {n3} a perfect power? -> {is_perfect_power(n3)}")
n4 = 16
print(f"Is {n4} a perfect power? -> {is_perfect_power(n4)}")
n5 = 1
print(f"Is {n5} a perfect power? -> {is_perfect_power(n5)}")
