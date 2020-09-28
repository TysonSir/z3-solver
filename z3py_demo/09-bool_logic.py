# filename: 09-bool_logic.py
"""
逻辑运算：与、或、非、蕴含（Implies）
T（Imp）T=T
T（Imp）F=F
F（Imp）T=T
F（Imp）F=T
"""
from z3 import *

print('\n# 逻辑运算求解')
p = Bool('p')
q = Bool('q')
r = Bool('r')
solve(Implies(p, q), r == Not(q), Or(Not(p), r))

print('\n# 逻辑运算化简')
p = Bool('p')
q = Bool('q')
print(And(p, q, True))
print(simplify(And(p, q, True)))
print(simplify(And(p, False)))

print('\n# 多项式与布尔组合')
p = Bool('p')
x = Real('x')
solve(Or(x < 5, x > 10), Or(p, x**2 == 2), Not(p))
print('全部解：x = +-sqrt(2)')

"""
因为solve中的三个assert都要满足，
所以Not(p) => p = False，
所以x**2 == 2要成立，所以x = +- sqrt(2)。
又因为x > 10不可能，所以就是x < 5，也就是正负根号2都可以，--“只输出一个解即可”--，所以输出负根号2可行.
"""
