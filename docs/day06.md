Today is the kind of day that gym bros call rest day, students call saturday, but no matter how small it seems, it is mayday !!

Think of it like this,
in Day 5 we opened a resturant and since we just opened it we were doing all of the tasks by ourselves: cooking, cleaning, greeting.

Our MLP class's learn() was forced into slavery,
it was doing everything from appending loss, updating values, resetting gradients, etc.
but today we broke it down. Now learn has workers who help him get work done much less chaotically.

This art of breaking down different tasks in modules/functions is known as modularity,
This is a must for developers who want to sclae a project.

main additions to the MLP class done today are:
1. parameters()
2. parameter_count()
3. zero_grad()
4. update()
5. train_step()