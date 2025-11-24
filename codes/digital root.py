import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time= end_time-start_time
print(f"Elapsed time: [{elapsed_time:.6f}seconds")
def digital_root(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    n = abs(n)
    while n >= 10:
        n = sum(int(ch) for ch in str(n))
    return n
print(digital_root(9875))
print(digital_root(345))
print(digital_root(9))
