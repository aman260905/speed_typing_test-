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
def are_amicable(a, b):
    if a <= 0 or b <= 0 or a == b:
        return False
    sum_a = aliquot_sum(a)
    is_a_amicable = (sum_a == b)
    sum_b = aliquot_sum(b)
    is_b_amicable = (sum_b == a)
    return is_a_amicable and is_b_amicable
print(f"Are 220 and 284 amicable? {are_amicable(220, 284)}")
print(f"Are 6 and 8 amicable? {are_amicable(6, 8)}")
