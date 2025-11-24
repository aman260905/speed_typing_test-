import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"Elapsed time:{elapsed_time:.6f} seconds")
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y
def mod_inverse(a, m):
    gcd_val, x, y = extended_gcd(a, m)
    if gcd_val != 1:
        raise ValueError(f"Modular inverse does not exist: {a} and {m} are not coprime (gcd={gcd_val})")
    else:
        return x % m
def crt(remainders, moduli):
    if len(remainders) != len(moduli) or not remainders:
        raise ValueError("Input lists must have the same length and not be empty.")
    M = 1
    for m in moduli:
        M *= m
    solution_x = 0
    for r_i, m_i in zip(remainders, moduli):
        M_i = M // m_i
        try:
            y_i = mod_inverse(M_i, m_i)
        except ValueError as e:
            raise ValueError(f"CRT requirement failed: Moduli must be pairwise coprime. {e}")
        term = r_i * M_i * y_i
        solution_x += term
    return solution_x % M
print(f"Solution x: {crt([2, 3, 2], [3, 5, 7])}")
