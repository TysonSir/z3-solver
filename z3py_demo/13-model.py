# filename: 13-model.py
"""
Solver显示求解结果值
"""
from z3 import *

x, y, z = Reals('x y z')
s = Solver()
s.add(x > 1, y > 1, x + y > 3, z - x < 10)
print(s.check())

m = s.model()
print("x = %s" % m[x])

print("traversing model...")
for d in m.decls():
    print("%s = %s" % (d.name(), m[d])) # Z3Py在需要时自动将Z3对象转换为文本表示。
