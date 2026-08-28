# importing value from ./src/micrograd/value.py
from micrograd.value import Value

# if the above import fails try running this: $env:PYTHONPATH="..\src"
# NOTE: you must be inside Poem_buddy_LLM/experiments while running the above code in terminal

# from below here experiment different expressions and make your own mini networks, calculate the gradient
# and compare what the code produced by what you got, it is lot more fun

# experiment 1 (same from docs/graphical_representation.png)
a = Value(5); a._label="a"
b = Value(3); b._label="b"

c = a * b; c._label="c"
d = a + c; d._label="d"

# don't forget to use d.backward()
d.backward()

print("values from exp 1")
print(a._grad)
print(b._grad)
print(c._grad)
print(d._grad)

# experiment 2
# Im not redeclaring the Value i am just changing the data value
a._data=7
b._data=8
c = a+b; c._label="c"
d = a*b + c; d._label="d"

d.backward()

print("\nvalues from exp 2")
print(a._grad)
print(b._grad)
print(c._grad)
print(d._grad)

# experiment 3
a._data=3
c = a+a+a; c._label="c"

c.backward()

print("\nvalues from exp 3")
print(a._grad)
print(c._grad)

# similarly run multiple experiments and manually calculate the gradient and then compare it with the code generated gradient
# until you feel confident that you understand it