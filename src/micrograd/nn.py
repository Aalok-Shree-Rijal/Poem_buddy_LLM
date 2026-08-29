import random

# which way we are going to use import matters as well
# NOTE: if you are using nn.py as a module and importing Neuron then use the below importing method
from .value import Value

# NOTE: if you are just running experiments directly in the nn.py file
# use : 
# from value import Value

class Neuron:
    def __init__(self, size:int):
        self.size = size
        self.weights = []
        # 'po' means 'pre output'
        self.po = 0.0

        # initializing weights
        for i in range(0, size):
            name = f"w{i}"
            name = Value(random.uniform(-1.0, 1.0)); name._label = f"w{i}"
            self.weights.append(name)

        # initializing bias
        self.bias = Value(random.uniform(-1.0, 1.0)); self.bias._label = 'b'

    def __repr__(self):
        return f"weights: {self.weights}, bias: {self.bias}"

    def __call__(self, data):
        # initializing weighted sum to 0. i.e: x1w1 + x2w2 + ... + xnwn
        weighted_sum = Value(0); weighted_sum._label='sum'

        # creating 'Value' variable for variables(x1,x2,...,xn)
        for i in range(0, len(data)):
            name = f"x{i}"
            name = Value(data[i]); name._label = f"x{i}"

            # calculating product of a single term of weighted sum (x1*w1),(x2*w2),..., (xn*wn)
            mul_name = f"x{i}w{i}"
            mul_name = name * self.weights[i]; mul_name._label = f"x{i}w{i}"

            # adding every term from the product to get weighted sum
            weighted_sum += mul_name; weighted_sum._label = 'sum'

        # calculating final result after adding bias
        sum = weighted_sum + self.bias; sum._label = 'res'
        self.po = sum._data

        # calculating final output after passing result through tanh()
        o = sum.tanh(); o._label='o'

        # this returns a value object that is assigned to the calling variable.
        return o

# Below this is the content of Day 4 so don't look at it if you are in day 2
class Layer:
    def __init__(self, nin, nout):
    # nin = neuron inputs, nout = no. of outputs/neurons

        # array of neurons
        self.neurons = []

        # creating the neurons
        for i in range(0, nout):
            name = f"neuron{i}"
            name = Neuron(nin)
            self.neurons.append(name)

    def __call__(self, inputs):
        self.outputs = []
        self.inputs = inputs
        # giving the inputs
        for neuron in self.neurons:
            out = neuron(inputs)
            self.outputs.append(out) 

        return self.outputs

# for experiments using this go to (./experiments/day02.py and ./experiments/day03.py)
