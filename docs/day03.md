<style>
  pre {
    background-color: #f4f4f4;
    border: 1px solid #ccc;
    padding: 15px;
    border-radius: 5px;
    overflow-x: auto; /* Adds a scrollbar if the code is too wide */
  }
  code {
    font-family: "Courier New", Courier, monospace;
    color: #c7254e;
  }
</style>


Day 3 is really simple and straightforward,

Now we have already built the complicated and manual task of creating Neurons and Values
We now proceed more into the area of trying to modularize those classes we have created
to get a deeper insight of how a neural net can use it's components.

The code says more than enough for day 3, just look at the day 3 code in nn.py 
give proper attention to the comments
<pre>
<code>
Think like this,

Thing -> What it is made up of

Layer -> Neurons
Neurons -> Weights, bias, variables
Weights, bias, variables -> Value class
Value class -> gradient values, data attributes, etc
</code>
</pre>
<br>
always think through this arrow diagram while trying to understand the code