# filename: 03-html_mode.py
"""
设置显示方式
"""
from z3 import *


x = Int('x')
y = Int('y')
print(x**2 + y**2 >= 1)

set_option(html_mode=False)
print(x**2 + y**2 >= 1)

set_option(html_mode=True)
print(x**2 + y**2 >= 1)
