# filename: 15-calculate.py
"""
Z3Py支持所有基本的算术运算
"""
from z3 import *

a, b, c = Ints('a b c')
d, e = Reals('d e')
solve(a > b + 2,
      a == 2*c + 10,
      c + b <= 1000,
      d >= e)
