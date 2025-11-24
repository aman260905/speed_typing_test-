import time
start_time=time.perf_counter()
for i in range(1000000):
    _= i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"elapsed time:{elapsed_time:.6f}seconds")
def is_harshad(n):
    if n <= 0:
        return False
    digit_sum = sum(int(digit) for digit in str(n))
    return n % digit_sum == 0
print(is_harshad(34))
print(is_harshad(2))
print(is_harshad(9))
print(is_harshad(126374))
