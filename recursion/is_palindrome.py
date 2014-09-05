def is_palindrome(a_string):
    stripped = [a.lower() for a in a_string if a.isalpha()]
    # base case
    if len(stripped) <= 1:
        return True
    elif stripped[0] == stripped[-1]:
        return is_palindrome(stripped[1:-1])
    else:
        return False


def test():
    s1 = "kayak"
    s2 = "Madam, I'm Adam."
    s3 = ""
    s4 = "a"
    s5 = "aaaa"
    s6 = "python"
    s7 = "abc"

    assert is_palindrome(s1) == True
    assert is_palindrome(s2) == True
    assert is_palindrome(s3) == True
    assert is_palindrome(s4) == True
    assert is_palindrome(s5) == True

    assert is_palindrome(s6) == False
    assert is_palindrome(s7) == False

    print("tests pass")


if __name__ == "__main__":

    test()
