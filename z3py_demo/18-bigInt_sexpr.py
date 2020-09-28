# filename: 18-bigInt_sexpr.py
"""
较大的整数，有理数 和 无理数 执行基本算术
sexpr() 方法: 提取Z3内部表示
"""
from z3 import *

x, y = Reals('x y')
solve(x + 10000000000000000000000 == y, y > 20000000000000000)

print(Sqrt(2) + Sqrt(3))
print(simplify(Sqrt(2) + Sqrt(3)))
print(simplify(Sqrt(2) + Sqrt(3)).sexpr())

# 显示前缀表达式
print((x + Sqrt(y) * 2).sexpr())
