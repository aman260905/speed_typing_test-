import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"Elapsed time:{elapsed_time:.6f} seconds")
def collatz_length(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 0
    steps = 0
    current_n = n
    while current_n != 1:
        if current_n % 2 == 0:
            current_n = current_n // 2
        else:
            current_n = 3 * current_n + 1
        steps += 1
    return steps
n1 = 6
print(f"Collatz length for {n1}: {collatz_length(n1)}")
n2 = 1
print(f"Collatz length for {n2}: {collatz_length(n2)}")
n3 = 27 
print(f"Collatz length for {n3}: {collatz_length(n3)}") 
n4 = 15
print(f"Collatz length for {n4}: {collatz_length(n4)}")
