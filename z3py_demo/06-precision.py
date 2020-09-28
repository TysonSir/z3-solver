# filename: 06-precision.py
"""
设置精度
"""
from z3 import *

x = Real('x')
y = Real('y')

print("默认输出（?代表被截断）：")
solve(x**2 + y**2 == 3, x**3 == 2)

set_option(precision=30)
print("保留小数点后30位：")
solve(x**2 + y**2 == 3, x**3 == 2)
