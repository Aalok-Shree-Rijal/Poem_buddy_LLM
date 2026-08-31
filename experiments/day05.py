from src.micrograd import MLP

# This dummy dataset below is only used from Day 05

# respective inputs
xs = [
    [2, 3],
    [3, 4],
    [-1, -2],
    [1, -1]
]

# respective output
ys = [
    [1],
    [1],
    [-1],
    [-1]
]

model = MLP(2,[3,2,1])

# checking the initial prediction of model before training
for i in range(len(xs)):
    prediction = model(xs[i])[-1][0]
    print(
        f"input={xs[i]},"
        f"target={ys[i][0]},"
        f"prediction={prediction._data}"
    )

model.learn(xs, ys, 1)

# testing whether the model actually is good at prediction now
for i in range(len(xs)):
    prediction = model(xs[i])[-1][0]
    print(
        f"input={xs[i]},"
        f"target={ys[i][0]},"
        f"prediction={prediction._data}"
    )

# I didn't include it but i would encourage you to play around by changhing things like learning step
# size of dataset, etc and see how it affets the result