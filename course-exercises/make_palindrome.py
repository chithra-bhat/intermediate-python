def make_palindrome(s):
    """Create a palindrome with the given string as a prefix.

    :param s: A string to form the prefix of a new palindrome.
    """
    s = s + s[::-1]
    return s


print(make_palindrome("abc"))
