import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"Elapsed time:{elapsed_time:.6f} seconds")
def is_quadratic_residue(a: int, p: int) -> bool:
    if p <= 1:
        print(f"Error: Modulus p must be greater than 1. Received p={p}")
        return False
    a_mod_p = a % p
    for x in range(p):
        x_squared_mod_p = (x * x) % p
        if x_squared_mod_p == a_mod_p:
            return True
    return False
a1, p1 = 10, 13
print(f"Is {a1} a quadratic residue modulo {p1}? -> {is_quadratic_residue(a1, p1)}")
a2, p2 = 5, 7
print(f"Is {a2} a quadratic residue modulo {p2}? -> {is_quadratic_residue(a2, p2)}")
