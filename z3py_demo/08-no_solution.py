# filename: 08-no_solution.py
"""
无解
"""
from z3 import *

x = Real('x')
solve(x > 4, x < 0)
