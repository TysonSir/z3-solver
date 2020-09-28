# filename: 17-help_simplify.py
"""
 Z3Py允许用户以两种风格书写选项"
 1. 以：开头，单词之间用 - 分隔
 2. 类似Python的名称，其中：被压缩并且被_替换
"""
from z3 import *

x, y = Reals('x y')
# Z3形式传参
print(simplify(x == y + 2, ':arith-lhs', True))
# Z3Py形式传参
print(simplify(x == y + 2, arith_lhs=True))

# rith-lhs参数被设置成True（default：False），意味着所有参数都放在 等号左边，右边只留下常数。

print("\n打印simplify可使用的参数:")
help_simplify()
