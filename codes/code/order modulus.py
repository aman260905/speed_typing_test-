import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"Elapsed time:{elapsed_time:.6f} seconds")
import math
def order_mod(a: int, n: int) -> int:
    if n <= 1:
        return -1
    if math.gcd(a, n) != 1:
        return -1
    a = a % n
    if a == 0:
        return -1
    k = 1
    current_power = a
    while k <= n:
        if current_power == 1:
            return k
        current_power = (current_power * a) % n
        k += 1
    return -1
a1, n1 = 3, 7
print(f"Order of {a1} mod {n1}: {order_mod(a1, n1)}")
a2, n2 = 2, 8
print(f"Order of {a2} mod {n2}: {order_mod(a2, n2)}")
a3, n3 = 10, 13
print(f"Order of {a3} mod {n3}: {order_mod(a3, n3)}")
a4, n4 = 2, 5
print(f"Order of {a4} mod {n4}: {order_mod(a4, n4)}")
