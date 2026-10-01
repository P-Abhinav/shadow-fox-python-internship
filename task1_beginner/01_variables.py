"""ShadowFox Python Internship - Task 1: Variables"""

# 1. Store 22/7 in pi and check its type.
pi = 22 / 7
print("1. pi =", pi)
print("   Data type:", type(pi).__name__)

# 2. `for` is a Python keyword, so it cannot be used as a variable name.
# The following would raise SyntaxError if uncommented:
# for = 4
print("2. `for` cannot be used as a variable because it is a Python keyword.")

# 3. Calculate simple interest for 3 years.
principal = 10000
rate = 5
time = 3
simple_interest = principal * rate * time / 100
print("3. Simple Interest =", simple_interest)
