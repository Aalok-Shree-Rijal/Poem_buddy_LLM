<h1>Word Generation and Broadcasting Semantics</h1>
<p>Now we have used our bigrams and the probability distribution and we can use the multinomial function of pytorch to sample our probability distribution and then join the prediction that is made my the function to get our output word.</p>
<code>
<pre>
initializing char : " " {"." in our code} [whitespace]
multinomial function : takes arguments - (initializing char, probability distribution tensor, generator seed, etc...)
prediction : multinomial throws a predicted char at us
reuse of prediction : now the prediction is again used as initializing char to make the next prediction
loop : this is done until the prediction is whitespace and then the loop is broken 
output : now we have a array of predicted chars which is joined using .join() and printed
</pre>
</code>

<h2>Broadcasting Semantics</h2>
<p>another important concept for day 2 is that while doing tensor operations we should the rules in mind. The most basic set of rules that govern operations in tensors is.</p>
<ul>
Two tensors are “broadcastable” if the following rules hold:
<li>When iterating over the dimension sizes, starting at the trailing dimension, the dimension sizes must either be equal, one of them is 1, or one of them does not exist.</li><ul><br>
<p>This is the basics of using bigram model, multinomial and python to build a simple makemore model.</p>