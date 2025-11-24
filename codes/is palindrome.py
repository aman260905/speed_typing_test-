import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time= end_time-start_time
print(f"Elapsed time: [{elapsed_time:.6f}seconds")
def is_palindrome(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    s = str(n)
    if s.startswith('-'):
        return False
    return s == s[::-1]
print(is_palindrome(121))
print(is_palindrome(333))
print(is_palindrome(78567))
