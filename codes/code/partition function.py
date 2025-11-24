import time
start_time=time.perf_counter()
for i in range(1000000):
    _=i*2
end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"Elapsed time:{elapsed_time:.6f} seconds")
def partition_function(n: int) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[i - j]
    dp = [0] * (n + 1)
    dp[0] = 1
    for j in range(1, n + 1):
        for i in range(j, n + 1):
            dp[i] += dp[i - j]
    return dp[n]
n1 = 4
print(f"Number of partitions of {n1}, p({n1}): {partition_function(n1)}")
n2 = 5
print(f"Number of partitions of {n2}, p({n2}): {partition_function(n2)}")
n3 = 10
print(f"Number of partitions of {n3}, p({n3}): {partition_function(n3)}")
