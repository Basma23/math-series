def sum_series(n, a = 0, b = 1):
    """
    Generates a generic series based on arguments

    Arguments:
        n {integer} -- [index that will be used to generate the series]
        a {integer} -- [value to determine the base case of 0 index]
        b {integer} -- [value to determine the base case of 1 index]

    Returns:
        {integer} -- [generic math series based on the arguments a,b]
    """
    if n <= 0:   # in case n is negative
        return a
    elif n == 1:
        return b
    return sum_series(n - 1, a, b) + sum_series(n - 2, a, b)


def fibonacci(n):
#   if n <= 0:
#       return 0
#   if n == 1:
#     return n
#   return fibonacci(n - 1) + fibonacci(n- 2)
  return sum_series(n, 0, 1)


def lucas(n):
    # if n <= 0: # Catch it here
    #     return 2
    # if n == 1:
    #     return 1
    # return lucas(n-1) + lucas(n-2)
    return sum_series(n, 2, 1)


if __name__=="__main__":
    print("I'm inside the script series")
    print(fibonacci(0))
    print(lucas(0))
    print(sum_series(3, 10, 2))
    print(help(sum_series))
    print(help(fibonacci))