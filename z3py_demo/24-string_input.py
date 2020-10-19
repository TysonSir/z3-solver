# filename: 24-string_input.py
"""
字符串方式输入表达式
"""
from z3 import *

print('example1:')
x,y,z = Ints('x y z') 
s = 'x + y + 2*z == 5'
F = eval(s)
solve(F)

print('example2:')
p = Bool('p')
q = Bool('q')
r = Bool('r')
s = 'Implies(p, q), r == Not(q), Or(Not(p), r)'
F = eval(s)
solve(F)

print('example3:')
x, y, z = Reals('x y z')

s = Solver()
expr = eval('x > 1, y > 1, x + y > 3, z - x < 10')
s.add(expr)

ret = s.check()
if ret == sat:
    print('有解')
    m = s.model()
    print("解：" + str(m))
else:
    print('无解')
