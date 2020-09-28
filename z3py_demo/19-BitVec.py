# filename: 19-BitVec.py
"""
创建 位向量变量 和 常量
"""
from z3 import *

# 1.创建一个位向量变量，名称为x，具有16位。
x = BitVec('x', 16)
y = BitVec('y', 16)
print(x + 2)
# 提取内部表示
print((x + 2).sexpr())

# 16位中，-1 == 65535
print(simplify(x + y - 1))

# 2.创建bit常量
# BitVecVal(10,32)创建一个大小为32的位向量，其值为10
a = BitVecVal(-1, 16)
b = BitVecVal(65535, 16)
# 16位中，-1 == 65535
print(simplify(a == b))

a = BitVecVal(-1, 32)
b = BitVecVal(65535, 32)
# 32位中，-1 != 65535
print(simplify(a == b))
