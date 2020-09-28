# filename: 07-RealVal.py
"""
Python数值 和 Z3有理数
"""
from z3 import *

print('Python数值：')
print(1/3)

print('Z3有理数：')
print(RealVal(1)/3)
print(Q(1,3))

print('')
x = Real('x') # 定义一个变量x
print(x + 1/3)
print(x + Q(1,3))
print(x + "1/3")
print(x + 0.25)

# 小数表示
set_option(rational_to_decimal=True)
print(x + 1/3)
