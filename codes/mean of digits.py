import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time= end_time-start_time
print(f"Elapsed time: [{elapsed_time:.6f}seconds")
def mean_of_digits(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    s = str(abs(n))
    digits = [int(ch) for ch in s]
    return sum(digits) / len(digits)
print(mean_of_digits(1234))
print(mean_of_digits(1235564))
