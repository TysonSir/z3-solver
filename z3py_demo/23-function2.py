# filename: 23-function2.py
"""
评估模型中的约束系统表达式。 以下示例显示如何使用评估方法
"""
from z3 import *

x = Int('x')
y = Int('y')
f = Function('f', IntSort(), IntSort())
s = Solver()
s.add(f(f(x)) == x, f(x) == y, x != y)

# 求是否有解
print(s.check())
m = s.model()

# 求表达式值
print("f(f(x)) =", m.evaluate(f(f(x))))
print("f(x)    =", m.evaluate(f(x)))
