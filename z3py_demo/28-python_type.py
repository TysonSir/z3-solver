# filename: 28-python_type.py
"""
解方程
"""

from z3 import *

# 变量
list_data = [2,10,7]

x = Real('x')
y = Real('y')
solve(x > list_data[0], y < list_data[1], x + 2*y == list_data[2])

# 函数
def xor(A, B):
    return Or(And(A, Not(B)), And(Not(A), B))
solve(Not(xor(x>0, y>0))) # 正负一致