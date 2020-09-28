# filename: 11-unknown.py
"""
z3能求解“非线形多项式约束", 2**x 不满足
"""
from z3 import *

x = Real('x')
s = Solver()
s.add(2**x == 3)
print(s.check())
