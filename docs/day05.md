<h1>I think calling day 4 as "HECTIC" was inappropriate once we complete day 5</h1>

Today we tackled a major problem in our abstraction using the "Value" class.
We couldn't operate with constants and values, the order of the operations
between constant and value also dictated if it will get carried out or not.
So we used: radd, rsub, rmul, rpow to make it so that we do not need to
worry if the operation we are doing is Value-Value operation.

It substantially improved our abstraction.
<hr>
Now the most important thing,
Remember from [file](./day04.md) line:46
Well, today we trampled that statement.
Now, our model is able to <b><i>"LEARN"</i><b>

<b>ISN'T THAT FUCKING AWESOMEEE????<b>

it is crazy how we moved from basic abstraction of a Value class, integrating calculus logic
behind calculating gradients and to a learning model.

To make it click for you, 
Think of it like this, <u>our model works in the following step which gives it the "learning title"</u>

1. it gets a random set of inputs and we choose the layers and no. of neurons in our MLP
2. it spits out a random/trash output using our forward pass and randomized initial weights and bias
3. we use the output/prediction it makes along what should have been the output and compute a loss function
4. Now we back propagate through all the parameters(weights, bias) with the respect to the loss funcion
5. Now we are able to calculate the gradient of all the parameters
6. Now our job is to minimize the loss funcion so we take a "learning step" and the formed gradients to gain new weights and bias
7. These new weight and bias help decrease the loss funcion because we follow the path of the gradient
8. We repeat this learning iteration over a wide set of inputs and targets of a dataset
9. Then we get what we call a "learning model" that can predict (~)accurately<br>
TADAAA!!
<hr>
PS: today we have only taken a neural network that explicitly only has 1 neuron in the final layer so that there is only
one output/prediction and calculating loss function and iteration becomes simpler, we will expand on it later.
Also the xs and ys are carefully made such that the <mark>output ys</mark> only consists of <mark>-1 and 1</mark> because that's the normal<br>
output we get from our neurons due to <mark>tanh()</mark>
