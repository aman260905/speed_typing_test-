import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"Elapsed time:{elapsed_time:.6f} seconds")
def mod_exp(base, exponent, modulus):
    if modulus <= 0:
        raise ValueError("Modulus must be a positive integer.")
    if exponent < 0:
        raise ValueError("Exponent must be a non-negative integer for this operation.")
    if exponent == 0:
        return 1 % modulus
    base %= modulus
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result
print(f"(5^3) % 7 = {mod_exp(5, 3, 7)}")
print(f"(3^10) % 11 = {mod_exp(3, 10, 11)}")
print(f"(2^100) % 13 = {mod_exp(2, 100, 13)}")
