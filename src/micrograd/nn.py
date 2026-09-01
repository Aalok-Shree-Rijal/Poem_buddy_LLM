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

            ### This is very important ###
            # This right here is the python technicality of how our abstraction is working
            # since our layers provides the output that are not simple numbers but a value object
            # while using an MLP we should first check if whether the inputs are in numeric form
            # or already converted into Value objects
            if isinstance(data[i], Value):
                name = data[i]
            else:
                name = Value(data[i]); name._label = f"x{i}"

            # calculating product of a single term of weighted sum (x1*w1),(x2*w2),..., (xn*wn)
            mul_name = f"x{i}w{i}"
            mul_name = name * self.weights[i]; mul_name._label = f"x{i}w{i}"

            # adding every term from the product to get weighted sum
            weighted_sum += mul_name; weighted_sum._label = 'sum'

        # calculating final result after adding bias
        total_sum = weighted_sum + self.bias; total_sum._label = 'res'
        self.po = total_sum._data

        # calculating final output after passing result through tanh()
        o = total_sum.tanh(); o._label='o'

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

    # This will print all the weights and bias in the Layer in a form of array
    def __repr__(self):
        return f"{self.neurons}"

    def __call__(self, inputs):
        self.outputs = []
        self.inputs = inputs
        # giving the inputs
        for neuron in self.neurons:
            out = neuron(inputs)
            self.outputs.append(out) 

        return self.outputs

# below this is the content from day 4

class MLP:

    # MLP(no. of inputs, [no. of neurons in layer 0, no. of neurons in layer 1, .....])
    def __init__(self, nin, nouts):
        # this stores all the layers we have 
        self.val_layers = []

        # since the output of previous layer becomes the input of upcoming one we need this
        current_input = nin

        for i in range(0, len(nouts)):
            current_layer = Layer(current_input, nouts[i])
            self.val_layers.append(current_layer)
            current_input = nouts[i]

    def __repr__(self):

        # This prints the MLP in a form of array where no. of elements represents the no. of layers
        # Each layer's weights and bias is also shown in the array
        return f"{self.val_layers}"

    def __call__(self, inputs):
        current_input = inputs

        # this array contains outputs from all the layers in the form of an array
        self.outs = []
        for layer in self.val_layers:
            out = layer(current_input)
            self.outs.append(out)
            current_input = out

        return self.outs

    # This function is here to give us only the final output after the initial input has passed through
    # all the hidden layers
    def final_output(self):
        return self.outs[-1]

    # this loss function will be different later on but for just Day 05 we will have a very simple one because 
    # we will make sure to make the last layer give only one output as the final output
    def learn(self, input, target, learning_step):
        # This is the loop that decides the no. of iterations in learning
        for epoch in range(1,100):

            # clearing previous loss values
            loss = []

            for i in range(0, len(target)):

                # forward pass
                prediction = self(input[i])[-1][0]

                # calculating loss
                current_loss = (target[i][0] - prediction)**2 
                # appending the loss to our list
                loss.append(current_loss)

                # resetting gradients
                for layer in self.val_layers:
                    for neuron in layer.neurons:
                        for weight in neuron.weights:
                            weight._grad = 0
                
                        neuron.bias._grad = 0

                # backpropagation
                current_loss.backward()

                # updating parameters
                for layer in self.val_layers:
                    for neurons in layer.neurons:
                        for weight in neurons.weights:
                            weight._data = weight._data - (learning_step*weight._grad)
                        neurons.bias._data -= learning_step * neurons.bias._grad

            # calculating avg loss
            avg_loss = sum(val._data for val in loss)/len(loss)

            # printing out loss
            print(f"Epoch: {epoch}, loss={avg_loss}")



# for experiments using this go to (./experiments/day02.py and ./experiments/day03.py and ./experiments/day04.py)
