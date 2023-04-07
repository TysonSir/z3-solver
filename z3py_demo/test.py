from z3 import *

# Create two Real variables
x = Real('x')
y = Real('y')

# Create a constraint that requires the square root of x to be greater than y
s = Solver()
s.add(x > y**2)

# Check if there is a solution
if s.check() == sat:
    # Get the solution
    m = s.model()
    print("x = %s" % m[x])
    print("y = %s" % m[y])
else:
    print("No solution")