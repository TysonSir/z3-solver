# filename: 10-Solver_obj.py
"""
SOLVERS 求解器: Solver类
"""
from z3 import *

x = Int('x')
y = Int('y')

s = Solver()
print('s: {}'.format(s))

s.add(x > 10, y == x + 2)
print('s: {}'.format(s))
print("求解器得到结果: ")
print(s.check()) # sat: 满足（satisfied），unsat:不满足（unsatisfied）

print("创建一个新的作用域：")
s.push()

s.add(y < 11)
print('s: {}'.format(s))
print("求解更新后的约束集合: ")
print(s.check())

print("恢复状态：")
s.pop()
print('s: {}'.format(s))
print("求解更新后的约束集合: ")
print(s.check())

"""
在一些应用中，我们想要探索几个共享几个约束的类似问题。我们可以使用push和pop命令来做到这一点。
每个求解器维护一堆断言。
命令push通过保存当前堆栈大小来创建一个新的作用域。
命令pop删除它与匹配推送之间执行的任何断言。
检查方法始终对求解器断言堆栈的内容进行操作。
"""
