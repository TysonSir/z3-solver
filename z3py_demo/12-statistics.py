# filename: 12-statistics.py
"""
遍历断言解析器中的约束.
收集检查方法的性能统计信息。
"""
from z3 import *

x = Real('x')
y = Real('y')
s = Solver()
s.add(x > 1, y > 1, Or(x + y > 3, x - y < 2))
print("asserted constraints...")
for c in s.assertions():
    print(c)

print(s.check())
print("statistics for the last check method...")
print(s.statistics())
# Traversing statistics
for k, v in s.statistics():
    print("%s : %s" % (k, v))
    
    
