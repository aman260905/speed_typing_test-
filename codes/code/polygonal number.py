import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"Elapsed time:{elapsed_time:.6f} seconds")
def polygonal_number(s: int, n: int) -> int:
    if s < 3 or n < 1:
        return -1
    term1 = (s - 2) * n
    term2 = (s - 4)
    inner_term = term1 - term2
    result = (n * inner_term) // 2
    return result
s1, n1 = 3, 4 
print(f"The {n1}-th {s1}-gonal (Triangular) number: {polygonal_number(s1, n1)}")
s2, n2 = 4, 5
print(f"The {n2}-th {s2}-gonal (Square) number: {polygonal_number(s2, n2)}")
s3, n3 = 5, 3
print(f"The {n3}-th {s3}-gonal (Pentagonal) number: {polygonal_number(s3, n3)}")
s4, n4 = 6, 4
print(f"The {n4}-th {s4}-gonal (Hexagonal) number: {polygonal_number(s4, n4)}")
