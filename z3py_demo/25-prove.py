# filename: 25-prove.py
"""
检查这个公式的非是否是不可满足的。下述的函数是Z3Py的命令prove 的简化版。
"""
from z3 import *

p, q = Bools('p q')
demorgan = And(p, q) == Not(Or(Not(p), Not(q)))
print(demorgan)

# 表达式 f 为假，无解。即 永真
def prove(f):
    s = Solver()
    s.add(Not(f))
    if s.check() == unsat:
        print("proved")
    else:
        print("failed to prove")

print("Proving demorgan...")
prove(demorgan)
