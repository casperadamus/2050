import time 

def fib_recursive(n):
    if n == 1 or n == 0:
        return n
    elif n < 0:
        raise ValueError("Input must be a non-negative integer.")
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_memo(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n == 1 or n == 0:
        return n
    elif n < 0:
        raise ValueError("Input must be a non-negative integer.")
    else:
        cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
        return cache[n]

def fib_iter(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    if n <= 1:
        return n 

    a, b = 0, 1

    for i in range(2, n + 1):
        a, b = b, a + b
    return b 

test_cases = [10, 25, 35]

for n in test_cases:
    print(f"Testing n = {n}")

# Measure Recursive
    start = time.time()
    fib_recursive(n)
    print(f"Recursive: {time.time() - start} seconds")

# Measure Memoization
    start = time.time()
    fib_memo(n)
    print(f"Memoized:  {time.time() - start} seconds")

# Measure Iterative
    start = time.time()
    fib_iter(n)
    print(f"Iterative: {time.time() - start} seconds")
    print()
