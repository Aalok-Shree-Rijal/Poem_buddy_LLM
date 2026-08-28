# importing the Neuron class we made
from micrograd.nn import Neuron

# if the import fails try running "$env:PYTHONPATH="..\src"
# NOTE: you must be inside Poem_buddy_LLM/experiments while running the above code in terminal

# below are some experiments
# feel free to manually cross verify the produced output and do new experiments

# exp 1
# just verifying our readability and blocks we made in nn.py
print("experiment 1:")
n = Neuron(2)

out = n([1, 2])

print("Weights:", n.weights)
print("Bias:", n.bias)
print("Pre-activation:", n.po)
print("Output:", out)

# exp 2
# here we are trying to see does different inputs have different outputs
print("\nexperiment 2:")
n = Neuron(2)

out1 = n([1, 2])
out2 = n([2, 1])
out3 = n([0, 0])
out4 = n([-1, -2])

print(out1)
print(out2)
print(out3)
print(out4)

# exp 3
# in this experiment we are trying to see what happens to output when bias is modified
print("\nexperiment 3:")
n = Neuron(2)

n.weights[0]._data = 1
n.weights[1]._data = 1
n.bias._data = 0

print(n([1, 1]))

n.bias._data = 2
print(n([1, 1]))

n.bias._data = -2
print(n([1, 1]))

# exp 4
# we are trying to see what happens when weights are directly impacted which impacts weighted sum
print("\nexperiment 4:")
n = Neuron(2)

n.weights[0]._data = 1
n.weights[1]._data = 1
n.bias._data = 0

print(n([1, 1]))

n.weights[0]._data = 2
print(n([1, 1]))

n.weights[0]._data = -2
print(n([1, 1]))

# exp 5
# we are trying seeing the gradient of the components like weights and biases
print("\nexperiment 5:")
n = Neuron(2)

out = n([1, 2])

out.backward()

print("Output:", out)

for w in n.weights:
    print(w, "gradient =", w._grad)

print(n.bias, "gradient =", n.bias._grad)