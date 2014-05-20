"""
Write two Python functions to find the minimum number in a list. 
The first function should compare each number to every other number on the list. 
O(n2). 
The second function should be linear O(n).
"""

# O(n2)
def min1(thelist):
    for i in thelist:
        for j in thelist:
            if j < i:
                break
        else:
            return i


# O(n)
def min2(thelist):
    least = thelist[0]
    for e in thelist:
        if e < least:
            least = e
    return least


def test():
    a = list(range(10))
    b = list(reversed(a))
    c = [3 for x in range(10)]
    assert min1(a) == 0
    assert min1(b) == 0
    assert min1(c) == 3
    assert min2(a) == 0
    assert min2(b) == 0
    assert min2(c) == 3
    print('tests pass')


print(test())