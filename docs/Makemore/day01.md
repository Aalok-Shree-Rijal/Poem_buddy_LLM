<h1>Bigrams and the probability distribution</h1>

In order to produce sentences we need words and for words we need characters.
<pre>
<code>
sentences -> words
words -> characters
</code>
</pre>
<br><br>
Well bigram is something in the middle.<br><br>
<u><b>We take group of two characters and treat it as an string that we calculate how often is repeated in the dataset.</b></u><br>
<br>
<b>For example:</b>
<pre>
<code>
sentence/string = "aalok shree rijal"

now, 
words = ["aalok", "shree", "rijal"]

again,
chars = ['a', 'e', 'h',  'i', 'j', 'k', 'l', 'o', 's', 'r']

#NOTE: I have only written non-repeated characters and sorted them as well
(I manually sorted them for your sake T-T)

but.. A bigram would look something like,
"aalok shree rijal" = [".aa", "al", "lo", "ok", "k.", ".s", "sh", ... , "l."]

where, "." is representing starting or ending of a word

Think of it like a two character wide frame just going across the sentence.
</code>
</pre>

<br>
<h2>2D- Arrays</h2>
<br>
Now we use the 'torch' library to store these occurances of specific bigram in a 2D - Array.<br>
You can gauge the structure of that 2D array by running <a href="../../src/makemore/day01.py">This</a> file.<br>

<br>
Now the dataset we have of "names.txt",<br>
In our code we use .join() to concatenate all of those words into a massive string and find all the characters involved using set() and sorted().<br>
Then we loop through the words just and find bigrams and tally their repetition in the 2D- array that we got thanks to the tensor library.<br>
<br>
Now, all we do is find the probabilty of that bigram occuring<br>
Example of calculating probability distribution:<br>
<pre>
<code>
probability = n(number of occurances of that event)/n(total number of occurances of all events)

so we do exactly that,
we divide each element of the row by sum of all the elements of the row,
i.e: 
let's suppose the 1st row had: [a, b, c, d]
then the new row of probability distribution can be found by,
A = a/(a+b+c+d)
B = b/(a+b+c+d)
C = c/(a+b+c+d)
D = d/(a+b+c+d)

so, the new row of probability distribution will be,
[A, B, C, D]
</code>
</pre>

<br>
This is it for today nothing complex, 
<ul>
    <li>What are bigrams?</li>
    <li>Visual representation of bigrams</li>
    <li>Manual calculation of probability distribution</li>
</ul>