# filename: 16-simplify2.py
"""
simplify命令对Z3表达式应用简单的转换
"""
from z3 import *

x, y = Reals('x y')
# 用 "单项式和" 的形式表示表达式
t = simplify((x + y)**3, som=True)
print(t)
# 用“指数”形式表示
t = simplify(t, mul_to_power=True)
print(t)
