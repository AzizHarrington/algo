import random


def generateOne(str_len):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(str_len):
        res = res + alphabet[random.randrange(27)]

    return res


def score(goal, teststring):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numSame = numSame + 1
    return float(numSame) / len(goal)


def main():

    goalstring = "methinks it is like a weasel"
    newstring = generateOne(28)
    best = 0
    newscore = score(goalstring, newstring)
    while newscore < 1:
        if newscore > best:
            print(newstring, newscore)
            best = newscore
        newstring = generateOne(28)
        newscore = score(goalstring, newstring)

main()