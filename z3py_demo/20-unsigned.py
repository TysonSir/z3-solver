# filename: 20-unsigned.py
"""
位运算，分有符号、无符号两个版本
有符号：<       <=     >      >=     /       ％      >>
无符号：ULT     ULE    UGT    UGE    UDiv    URem    LShR
"""
from z3 import *

# 创建32位x,y
x, y = BitVecs('x y', 32)
solve(x + y == 2, x > 0, y > 0)

# 位运算 与、或、非
# &   and
# |   or
# ~   not
solve(x & y == ~y)

solve(x < 0)

# 使用有符号版本的 < 小于号 
solve(ULT(x, 0))
