# This will open the names.txt file and then break the names after each line break and then return back an array of the names 'word'
words = open('./names.txt', 'r').read().splitlines()

# now let's try and go with 'bigram' language model (more about it in ./docs/makemore/day01.md)

# This is an empty dictionary which we will later fill up in the format:
# bigram : count_of_appearence 
b = {}
for w in words[:3]:

    # this is done to make sure that start and end of the word is signified by some tags, this gives a new list 
    # 
    # for example: "Mona" will be 
    # ["<S>","m","o","n","a","<E>"]
    chs = ['<S>'] + list(w) + ['<E>']

    # if this confuses you try looking more about zip() function in python, resource: https://www.w3schools.com/python/ref_func_zip.asp
    for ch1, ch2 in zip(chs, chs[1:]):
        bigram = (ch1,ch2)

        # b.get(bigram, 0) looks for "bigram" key's value in b and if there is none then it returns 0
        b[bigram] = b.get(bigram, 0) + 1
        print(ch1,ch2)

    print(b)
# continue from below 
# https://youtu.be/PaCmpygFfXo?t=758