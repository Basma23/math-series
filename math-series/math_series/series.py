def fibonacci(n):
  if n <= 2:
    return 1
  return fibonacci(n - 1) + fibonacci(n- 2)

print(fibonacci(0))

def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)
    
print(lucas(0))

def sum_series(n, a = 0, b = 1):
    if n == 0:
        return a
    elif n == 1:
        return b
    return sum_series(n - 1, a, b) + sum_series(n - 2, a, b)

print(sum_series(8, 10, 2))
