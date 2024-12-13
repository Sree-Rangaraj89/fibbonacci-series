def fibonacci_series(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    return fib_series

n = 20

fib_series = fibonacci_series(n)
for index, value in enumerate(fib_series):
    print(f"Term {index + 1}: {value}")
