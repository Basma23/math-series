from math_series.series import fibonacci, lucas, sum_series
# import math_series.series as s
# print(dir(s))


def test_of_fibonacci():
    expected = 34
    actual = fibonacci(9)
    assert actual == expected

def test_fib_zero():
    expected = 0
    actual = fibonacci(0)
    assert actual == expected

def test_fib_one():
    expected = 1
    actual = fibonacci(1)
    assert actual == expected

def test_fib_neg():
    expected = 0
    actual = fibonacci(-10)
    assert actual == expected

def test_of_lucas ():
    expected = 123
    actual = lucas(10)
    assert actual == expected

def test_of_sum_series():
    expected = 172
    actual = sum_series(8,10,2)
    assert actual == expected