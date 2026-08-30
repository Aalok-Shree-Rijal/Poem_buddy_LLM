from micrograd.nn import MLP

# if the above import fails, try running ($env:PYTHONPATH="../src") in the terminal

# let's create a MLP with 2 base inputs and 3 layers with 3, 2 and 3 neurons in each layer respectively [reference](../docs/simple_mlp.png)
test = MLP(2, [3,2,3])
outputs = test([1,2])

# prints o1, o2 and o3
print("\n### Printing just the final output ###")
print("--------------------------------------")
print(test.final_output())

# now let's print all of the weights, bias involved while making those final outputs
print("\n### list of all the parameters involved ###")
print("-------------------------------------------")
print(test.val_layers)

# now let's see what happens to the gradient of all the weights before and after backpropagating just o1

print("\n### checking weight's gradients before backpropagation ###")
print("------------------------------------------------------------")
for layers in test.val_layers:
    for neurons in layers.neurons:
        for weights in neurons.weights:
            print (f"{weights._label}: {weights._grad}") 

# now let's initiate back propagation on the o1
test.final_output()[0].backward()

print("\n### checking weight's gradients after backpropagation on o1 ###")
print("-----------------------------------------------------------------")
for layers in test.val_layers:
    for neurons in layers.neurons:
        for weights in neurons.weights:
            print (f"{weights._label}: {weights._grad}") 

# compare the output before and after propagation and read the line 40 of (./docs/day04.md) and take help of the
# illustrations and try to figure out why the last four weight's gradient is 0.0

# if you can say why then you have learnt more than enough for day 4