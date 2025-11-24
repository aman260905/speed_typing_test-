import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"Elapsed time:{elapsed_time:.6f} seconds")
def legendre_symbol(a, p):
    if p <= 2 or p % 2 == 0:
        raise ValueError("p must be an odd prime")
    a = a % p
    if a == 0:
        return 0
    res = pow(a, (p - 1) // 2, p)
    if res == 1:
        return 1
    elif res == p - 1:
        return -1
    else:
        return 0
print(legendre_symbol(5, 11))
print(legendre_symbol(8, 73))
print(legendre_symbol(4, 29))
