import cProfile

#Write a boolean function that returns true if two inputted strings of equal length
#are anagrams of eachother.




def is_anagram(str1, str2):
    for a in set((str1 + str2)):
        if a not in set(str1) or a not in set(str2):
            return False
    return True


def test():
    a1 = 'heart'
    a2 = 'earth'
    b1 = 'Discriminator'
    b2 = 'Doctrinairism'
    assert is_anagram(a1, a2)
    assert is_anagram(b1, b2)
    print('tests pass')


test()