# https://github.com/lucaarod/lab11-LR-GC
# Partner 1: Luca Rodriguez
# Partner 2: Guilherme Carvalheira

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# Part 2
def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

# Part 1 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b

