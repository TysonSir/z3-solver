# filename: 05-solve2.py
"""
定义变量：有理数、无理数
"""
from z3 import *

x = Real('x')
y = Real('y')
solve(x**2 + y**2 > 3, x**3 + y < 5)
