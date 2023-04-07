# filename: 28-python_type.py
"""
解方程
"""

from z3 import *

list_data = [2,10,7]

x = Int('x')
y = Int('y')
solve(x > list_data[0], y < list_data[1], x + 2*y == list_data[2])
