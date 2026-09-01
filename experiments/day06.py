from micrograd.nn import MLP
# if the above import fails try running: $env:PYTHONPATH='../src'

model = MLP(2, [4,3,2,1])

# using parameter_count to find total no. of parameters
print(f"total no. of parameters: {model.parameter_count()}")

# printing all the parameters with labels and values
print(model.parameters())

# resetting all gradients to 0.0
model.zero_grad()
for p in model.parameters():
    print(p, p._grad)

# respective inputs
xs = [
    [2, 3],
    [3, 4],
    [-1, -2],
    [1, -1]
]

# respective output
ys = [
    [1],
    [1],
    [-1],
    [-1]
]

# checking if the fresh gradients replace the reset
prediction = model([2, 3])[-1][0]

loss = (prediction - 1) ** 2

loss.backward()

for p in model.parameters():
    print(p, p._grad)


# checking if the parameters are changing properly with the learning step and gradient
old = model.parameters()[0]._data

model.update(0.1)

new = model.parameters()[0]._data

print(old)
print(new)