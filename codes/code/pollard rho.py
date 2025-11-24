import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"Elapsed time:{elapsed_time:.6f} seconds")
import math
import random
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
def pollard_rho(n: int) -> int:
    if n <= 3:
        return n
    if n % 2 == 0:
        return 2
    x = random.randint(2, n - 1)
    y = x                       
    c = random.randint(1, n - 1)
    g = 1
    def f(val, n_mod, c_offset):
        return (val * val + c_offset) % n_mod
    while g == 1:
        x = f(x, n, c)
        y = f(y, n, c)
        y = f(y, n, c)
        g = gcd(abs(x - y), n)
        if g == n:
            return pollard_rho(n)
    return g
n1 = 91
print(f"A factor of {n1} is: {pollard_rho(n1)}")
n2 = 8051
print(f"A factor of {n2} is: {pollard_rho(n2)}")
n3 = 24991
print(f"A factor of {n3} is: {pollard_rho(n3)}")
