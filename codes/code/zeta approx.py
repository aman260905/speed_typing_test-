import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"Elapsed time:{elapsed_time:.6f} seconds")
import math
def zeta_approx(s: float, terms: int) -> float:
    if s <= 1.0:
        return math.inf
    if terms <= 0:
        return 0.0
    zeta_sum = 0.0
    for k in range(1, terms + 1):
        term = 1.0 / (k ** s)
        zeta_sum += term
    return zeta_sum
s1, terms1 = 2.0, 100
approx1 = zeta_approx(s1, terms1)
exact1 = (math.pi**2) / 6
print(f"ζ({s1}) approx with {terms1} terms: {approx1:.6f} (Exact: {exact1:.6f})")
s2, terms2 = 3.0, 50
approx2 = zeta_approx(s2, terms2)
print(f"ζ({s2}) approx with {terms2} terms: {approx2:.6f}")
s3, terms3 = 1.0, 100
print(f"ζ({s3}) (Harmonic series): {zeta_approx(s3, terms3)}")
