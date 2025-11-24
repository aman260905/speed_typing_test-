import time
start_time=time.perf_counter()
for i in range (1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")
def multiply_digits(n):
    if n < 0:
              return 0
    product = 1
    for digit_char in str(n):
        product *= int(digit_char)
    return product
def multiplicative_persistence(n):
    if n < 10:
        return 0
    if n <= 0:
        return 0
    persistence_count = 0
    current_number = n
    while current_number >= 10:
        current_number = multiply_digits(current_number)
        persistence_count += 1
    return persistence_count
print(f"Persistence of 39: {multiplicative_persistence(39)}")
print(f"Persistence of 77: {multiplicative_persistence(77)}") 
