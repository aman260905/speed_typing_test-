import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"Elapsed time:{elapsed_time:.6f} seconds")
def aliquot_sum(n):
    if n <= 1:
        return 0
    total_sum = 1
    limit = int(n**0.5)
    for i in range(2, limit + 1):
        if n % i == 0:
            total_sum += i
            paired_divisor = n // i
            if paired_divisor != i:
                total_sum += paired_divisor
    return total_sum
print(aliquot_sum(28))
print(aliquot_sum(12))
print(aliquot_sum(10))
