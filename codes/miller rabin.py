import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"Elapsed time:{elapsed_time:.6f} seconds")
import random
def miller_rabin_test(a: int, n: int) -> bool:
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(s - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False
def is_prime_miller_rabin(n: int, k: int = 10) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        if not miller_rabin_test(a, n):
            return False
    return True
n1 = 17
print(f"Is {n1} likely prime (k=5)? -> {is_prime_miller_rabin(n1, 5)}")
n2 = 91
print(f"Is {n2} likely prime (k=5)? -> {is_prime_miller_rabin(n2, 5)}")
n3 = 2147483647
print(f"Is {n3} likely prime (k=10)? -> {is_prime_miller_rabin(n3, 10)}")
n4 = 561 
print(f"Is {n4} likely prime (k=3)? -> {is_prime_miller_rabin(n4, 3)}")
