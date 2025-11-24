import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"Elapsed time:{elapsed_time:.6f} seconds")
import math
def is_prime(n: int) -> bool:
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True
def is_carmichael(n: int) -> bool:
    if n <= 560 or is_prime(n):
        return False 
    bases_to_check = [2, 3, 5, 7, 11, 13] 
    for a in bases_to_check:
        if a >= n:
            break 
        if math.gcd(a, n) == 1:
            if pow(a, n - 1, n) != 1:
                return False
    return True


n1 = 561
print(f"Is {n1} a Carmichael number? -> {is_carmichael(n1)}")
n2 = 1105
print(f"Is {n2} a Carmichael number? -> {is_carmichael(n2)}")
n3 = 91
print(f"Is {n3} a Carmichael number? -> {is_carmichael(n3)}")
n4 = 17
print(f"Is {n4} a Carmichael number? -> {is_carmichael(n4)}")
