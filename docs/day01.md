<h1>The Value Class</h1>
Whenever we are making a "value" then initially it is not connected through any set of operations,<br>
they are said to be "leaf nodes" that's why since no function being present initially, the derivative (grad)<br>
is initialized to be zero.

<pre>
<code>
Now, for this specific example we are taking 
a = 5
b = 3
c = a * b
d = c + a
</code>
</pre>

It is a bit complicated at the first glance but let's break it down.<br>
for the graphical representation to go [the graphical_representation](./images/graphical_representation.png)

<pre>
<code>
we know that,
dd/dd = 1 (this is basic derivative in action, basically: if you change by 1 d will change by 1 lol..)

now, 
d = c + a
let's differentiatie with respect to (w.r.t) c,
dd/dc = dc/dc + da/dc
dd/dc = 1 + 0
dd/dc = 1

again differentiating w.r.t a,
dd/da = dc/da + da/da
dd/da = 0 + 1
dd/da = 1

now,
c = a * b
</code>
</pre>

notice how we don't have direct relation of 'a' and 'b' with the output 'd'<br>
but... we do know dd/dc, so let's use chain rule and try to find dd/da and dd/db<br>

<pre>
<code>
differentiating w.r.t a,
dc/da = d(a*b)/da
dc/da = b

similarly,
dc/db = a

we know,
dd/da = dd/dc * dc/da
dd/da = dd/dc * b
dd/da = 1 * b
dd/da = b
dd/da = 3

similarly,
dd/db = 5
</code>
</pre>
<br>
notice how the variable 'a' is used in two operations,<br>
normally all the variables would have a singular gradient value<br>
but 'a' has two paths (contributions) so the change in output 'd'<br>
with respect to 'a' needs to accumulate all contributions of 'a'<br>
<br>
<pre>
<code>
so,
dd/da = 1 + 3
dd/da = 4
</code>
