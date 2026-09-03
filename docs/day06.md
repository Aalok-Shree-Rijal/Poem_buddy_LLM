<h1>Modularization of MLP</h1>

<h3>Today is the kind of day that gym bros call rest day, students call saturday, but no matter how small it seems, it is mayday !!</h3><br>
Think of it like this,
in Day 5 we opened a resturant and since we just opened it we were doing all of the tasks by ourselves: cooking, cleaning, greeting.

Our MLP class's learn() was forced into slavery,<br>
it was doing everything from appending loss, updating values, resetting gradients, etc.<br>
but today we broke it down. Now learn has workers who help him get work done much less chaotically.<br>
<br>
This art of breaking down different tasks in modules/functions is known as modularity,<br>
This is a must for developers who want to scale a project.<br>
<br>
<b>main additions to the MLP class done today are:</b>
1. parameters()
2. parameter_count()
3. zero_grad()
4. update()
5. train_step()

<h1>Message regarding furthur expansion</h1>
<div>
    So, I want to be as honest as i can be.<br>
    I had started this repository so that I can learn more about LLM's in general<br>
    and my passion for writing poems guided me to the direction of a poem chat bot.<br>
    I had planned to take learning materials from different sources. But now i was<br>
    at the crossroads because we completed a very basiccccc MLP so what's next?<br>
    <br><br>
    I had learned of Value class, Neuron, Layers, Backpropagation and MLP from<br> 
    Karapathy's lecture 1.<br>
    <br><br>
    ANDREJ IF YOU ARE READING THIS <i>(I don't know how T0T)</i> HATS OFF TO YOU 🫡
    <br><br>
    So, I took a sneak peek on what exactly does Andrej teaches throughout this course<br>
    because i don't have good experiences with courses and tutorials throwback to <a href="https://github.com/Aalok-Shree-Rijal/learning_python/blob/main/README.md">readme file</a> of learning_python
    <br><br>
    and i found out that <mark>Andrej is basically building the same thing</mark> T_T<br>
    so, I have decided to use the <a href='https://karpathy.ai/zero-to-hero.html'>Neural Networks: Zero to Hero</a> as my main learning material<br><br>
    <i><b>but. but.. but...</b></i> in usual Aalok fashion I will document my journey not just copying code from Andrej's course but showcasing to you all about where i got stuck, how did i tackle it, what made it click, any other resources that i dug up for better understanding, etc. <br>
    <br>
    So stick around and see what happens to this project<br>
    PEACEE!!
</div>
