# importing this to use 2d arrays
import torch

# importing this for visual aesthetics
import matplotlib.pyplot as plt

# if the above imports fails try running "pip install torch/matplotlib" in the terminal

# This will open the names.txt file and then break the names after each line break and then return back an array of the names 'word'
words = open('./names.txt', 'r').read().splitlines()

# now let's try and go with 'bigram' language model (more about it in ./docs/makemore/day01.md)

# creating a 2d array (tensor) using the imported torch library 26(alphabets) + 2(start and end tags) = 28

# and to embody all possible combinations of what can come after one we use a 28*28 tensor: more about it in the readme file
N = torch.zeros((28,28), dtype=torch.int32)

# since, words is a list of all the words this will first join all the words then 'set()' will remove all the repetition and we will convert it into a list and then sort it then we will get a big list of all the characters used sorted from a to z.
chars = sorted(list(set(''.join(words))))

# now we need a lookup dictionary of the characters, look up what enumerate() does in python
stoi = {s:i+1 for i,s in enumerate(chars)}
stoi['.'] = 0

# reversed mapping dictionary (mainly for matplotlib aesthetic purposes)
itos = {i:s for s,i in stoi.items()}



for w in words:

    # this is done to make sure that start and end of the word is signified by some tags, this gives a new list 
    # 
    # for example: "Mona" will be 
    # ["<S>","m","o","n","a","<E>"]
    chs = ['.'] + list(w) + ['.']

    # if this confuses you try looking more about zip() function in python, resource: https://www.w3schools.com/python/ref_func_zip.asp
    for ch1, ch2 in zip(chs, chs[1:]):
        ix1 = stoi[ch1]
        ix2 = stoi[ch2]

        # now rather than updating a dictionary value we are just updating the specific item in the 2d array
        N[ix1,ix2] += 1

# calculating probability distributions
p = N[0].float()
p = p/p.sum()

# remember the probability from school sum of probabilities is 1 !
print(p, sum(p))

# this is to plot the bigrams and their occurance
plt.figure(figsize=(16,16))
plt.imshow(N, cmap='Blues')
for i in range(27):
    for j in range(27):
        chstr = itos[i] + itos[j]
        plt.text(j,i,chstr, ha="center", va="bottom", color="gray")
        plt.text(j,i, N[i,j].item(), ha="center", va="top", color="gray")
plt.show()

# continue tommorrow from here
# https://youtu.be/PaCmpygFfXo?t=1631