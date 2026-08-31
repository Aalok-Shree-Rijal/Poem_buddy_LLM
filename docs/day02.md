If you directly go to the code in /src/micrograd/nn.py it will probably go over your head and become confusing
but it is not that hard to be honest.
Let's dissect the things you need to know before hand and the things that the code tells you 

To grasp the idea of how an artificial neuron (simplified form of biological ones) work take a look at
[image](./images/Artificial_neuron.png)

every neuron follows the below steps and that's what we are trying to replicate by code:
1. we take inputs (x0, x1, ..., xn)
2. we multiply the inputs with initialized respective weights (w0, w1, ..., wn)
3. we take the weighted sum (x0w0 + x1w1 + x2w2 + ... + x3w3)
4. we add bias on top of this weighted sum
5. we pass this output from step 4 through a squishification function (i.e for our case 'tanh()')
6. we use back propagation to find the gradient of each component i.e (x0, x1, ..., xn), (w0, w1, ..., wn), (x0*w0, x1*w1, ..., xn*wn), b

NOTE: in our current neuron no learning is happening, we are just trying to comprehend how a neuron works in just a 
single cycle.