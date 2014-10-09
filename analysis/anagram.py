#Write a boolean function that returns true if two inputted strings of equal length
#are anagrams of eachother.


#my solution
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    list_1 = list(str1)
    list_2 = list(str2)
    for c in list_1:
        if list_1.count(c) != list_2.count(c):
            return False
    return True


def test():
    a1 = 'heart'
    a2 = 'earth'
    b1 = 'Discriminator'
    b2 = 'Doctrinairism'
    c1 = 'aba'
    c2 = 'bab'
    assert is_anagram(a1, a2) == True
    assert is_anagram(b1, b2) == True
    assert is_anagram(c1, c2) == False
    print('tests pass')


test()
