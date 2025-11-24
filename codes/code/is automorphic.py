import time
start_time=time.perf_counter()
for i in range(1000000):
    _= i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"elapsed time:{elapsed_time:.6f}seconds")
def is_automorphic(n):
    if n < 0:
        return False
    num_digits = len(str(n))
    modulus = 10 ** num_digits
    n_squared = n * n
    return n_squared % modulus == n
print(is_automorphic(12))
print(is_automorphic(3))
print(is_automorphic(56897567))
print(is_automorphic(9))
