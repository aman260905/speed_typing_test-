import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"Elapsed time:{elapsed_time:.6f} seconds")
def lucas_sequence(n: int) -> list[int]:
    if n <= 0:
        return []
    if n == 1:
        return [2]
    lucas_list = [2, 1]
    if n == 2:
        return lucas_list
    for _ in range(2, n):
        next_lucas = lucas_list[-1] + lucas_list[-2]
        lucas_list.append(next_lucas)
    return lucas_list
n1 = 5
print(f"First {n1} Lucas numbers: {lucas_sequence(n1)}")
n2 = 10
print(f"First {n2} Lucas numbers: {lucas_sequence(n2)}")
n3 = 1
print(f"First {n3} Lucas number: {lucas_sequence(n3)}")
