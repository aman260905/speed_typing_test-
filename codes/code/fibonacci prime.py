import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"Elapsed time:{elapsed_time:.6f} seconds")
import math
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def is_fibonacci_number(n: int) -> bool:
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    def is_perfect_square(k):
        if k < 0:
            return False
        root = int(math.isqrt(k))
        return root * root == k
    expr1 = 5 * n * n + 4
    expr2 = 5 * n * n - 4 
    return is_perfect_square(expr1) or is_perfect_square(expr2)
def is_fibonacci_prime(n: int) -> bool:
    if not is_prime(n):
        return False
    if not is_fibonacci_number(n):
        return False
    return True
n1 = 13
print(f"Is {n1} a Fibonacci Prime? -> {is_fibonacci_prime(n1)}")
n2 = 21
print(f"Is {n2} a Fibonacci Prime? -> {is_fibonacci_prime(n2)}")
n3 = 11
print(f"Is {n3} a Fibonacci Prime? -> {is_fibonacci_prime(n3)}")
