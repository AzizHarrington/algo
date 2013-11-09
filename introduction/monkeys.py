import random


def generate(length):
    """
    generate a random string of alpha + spaces
    equal to length
    """
    alpha = map(chr, range(97, 123))
    alpha.append(' ')
    result = ""
    for x in range(length):
        result += alpha[random.randrange(0,27)]
    return result


def score(sentence, test):
    """
    score how many elements of one 
    sentence match the test sentence
    """
    total = 0
    wrong = []
    i = 0
    while i < len(sentence):
        if sentence[i] == test[i]:
            total += 1
        else:
            # keep track of pos in list
            wrong.append(i)
        i += 1
    percent = float(total)/len(test)*100
    return percent, wrong


def find_match(sentence):
    """
    repeatedly calls generate and score
    until a one-hundred percent match is found
    """
    rand_sentence = generate(len(sentence))
    current_score = None
    times = 0
    while current_score != 100:
        current_score, wrong = score(sentence, rand_sentence)
        # create list from sentence 
        l = list(rand_sentence)
        # replace all wrong with randomly generated letters
        for e in wrong:
            l[e] = generate(1)
        # put list back into string form
        rand_sentence = "".join(l)
        times += 1
        if times % 1000 == 0:
            print "%s : %i" % (rand_sentence, current_score)
    return "%s : %i : %d" % (rand_sentence, current_score, times)



shakespeare = "methinks it is a weasel"

print find_match(shakespeare)
