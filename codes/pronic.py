import time
start_time=time.perf_counter()
for i in range(1000000):
    _= i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"elapsed time:{elapsed_time:.6f}seconds")
def is_pronic(n):
    if n < 0:
        return False
    import math
    k = int(math.sqrt(n))
    return n == k * (k + 1)
print(is_pronic(67))
print(is_pronic(2))
print(is_pronic(789796878))
print(is_pronic(56))
