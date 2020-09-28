# filename: 14-ToReal.py
"""
Z3支持实数和整数变量, 自动添加强制转换
"""
from z3 import *

x = Real('x')
y = Int('y')
a, b, c = Reals('a b c')
s, r = Ints('s r')
print(x + y + 1 + (a + s))
print(ToReal(y) + c)
