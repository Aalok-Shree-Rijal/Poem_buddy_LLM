<h1>This day is HECTIC !!!</h1>

<u>if all you have done up to day 03 is scroll past the code</u> and fool yourself by
saying you have understood it deeply without sitting with the code and executing 
it yourself, <b>it will be a long time staring at the screen.</b>
<hr>
Today we have basically moved from modules that we needed (Value class, neuron, layers) 
and transformed them into a basic MLP that actually works like the real deal except
upcoming complex topics like (loss function, gradient descent, etc)
<hr>
I have very carefully made the <mark>illustration</mark> for you guys so that it will be easier
to understand, go to [image](./images/simple_mlp.png)

Now see, how initially all we did was give two inputs i1 and i2,
but then those inputs are passed not just through a neuron but layers
and not just through layers but multiple layers and not just to get
one output but multiple outputs.<br>

<pre>
<code>
For the illustration i have made,
no. of initial given inputs = 2
no. of neurons in layer 1 = 3
no. of neurons in layer 2 = 2
no. of neurons in layer 3 = 3
no. of outputs = 3
</code>
</pre>

Trust me if you just try to vizualize and understand what is happening
you might reach the conclusion that<br>
<b>"the outputs of one layer is the input of the another layer"</b>

and you are not wrong but i don't think that way will help you get crystal clear about this,<br><br>
one thing that made this click was whenever seeing relation between input and a layer<br>
focus on the layer's neuron rather than the inputs.<br>
<mark><u>look for a single neuron.<u></mark><br>
inorder to make this visualization easy i have made another illustration of the same image<br>
but <mark>isolated just o1's path</mark>.<br>
go see the [image](./images/mlp_single_output_path.png)
<br><br>
notice how n2 and n3 of L3 don't have any direct relationship with o1?<br>
this will come in handy in day04's one experiment.<br>
<br>
And if you have paid attention to all the things we have gone through earlier like Values, neurons, layers then <br>
looking at the code carefully with the comments and looking at the illustration is enough to understand for day 04.<br>
<hr>
NOTE: we haven't built something that "learns" this is just a simple neural network that takes two initial inputs
and passes it through specified no. of layers having specified no. of neurons and provides us with the outputs with 
the connection through the Value abstraction we have made and having the ability to conduct backpropagation