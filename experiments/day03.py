from micrograd.nn import Layer

# if the above import fails, try running $env:PYTHONPATH="..\src"

# testing if Layers class works properly
l = Layer(2,3)
out = l([2,3])

print("\n### before backpropagation ###\n")

print("Neuron 0:")
for w in l.neurons[0].weights:
    print(w, w._grad)

print("Neuron 1:")
for w in l.neurons[1].weights:
    print(w, w._grad)

print("Neuron 2:")
for w in l.neurons[2].weights:
    print(w, w._grad)

# checking if backpropagation works
out[0].backward()

# NOTE: only the output you choose to backpropagate will have changed gradient values and that is the expected behaviour

print("\n### after backpropagation of Neuron 0 ###\n")
print("Neuron 0:")
for w in l.neurons[0].weights:
    print(w, w._grad)

print("Neuron 1:")
for w in l.neurons[1].weights:
    print(w, w._grad)

print("Neuron 2:")
for w in l.neurons[2].weights:
    print(w, w._grad)

out[1].backward()

print("\n### after backpropagation of Neuron 1 ###\n")
print("Neuron 0:")
for w in l.neurons[0].weights:
    print(w, w._grad)

print("Neuron 1:")
for w in l.neurons[1].weights:
    print(w, w._grad)

print("Neuron 2:")
for w in l.neurons[2].weights:
    print(w, w._grad)

out[2].backward()

print("\n### after backpropagation of Neuron 2 ###\n")
print("Neuron 0:")
for w in l.neurons[0].weights:
    print(w, w._grad)

print("Neuron 1:")
for w in l.neurons[1].weights:
    print(w, w._grad)

print("Neuron 2:")
for w in l.neurons[2].weights:
    print(w, w._grad)