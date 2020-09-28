# filename: 22-function.py
"""
函数定义
"""
from z3 import *

x = Int('x')
y = Int('y')

"""
定义一个函数，它接受一个类型（又名 sort）整数的参数并生成一个整数值。
def f(intA):
    return intB
    
类型（又名 sort）
"""
f = Function('f', IntSort(), IntSort())

solve(f(f(x)) == x, f(x) == y, x != y)

# [x = 0, y = 1, f = [1 -> 0, else -> 1]]
def f(a):
    if a == 1:
        return 0
    else:
        return 1
