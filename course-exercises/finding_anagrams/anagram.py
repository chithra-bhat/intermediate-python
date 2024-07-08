from wordsets import english_words, english_words_small
from collections import defaultdict


def find_anagrams(letters, words):
    """Find a collection of anagrams of given letters from a given word bank.

    :param letters: The letters from which to form anagrams.
    :param words: A set of lowercase, alphabetic English words in a word bank.
    :return: A set of anagrams of the given letters found in the word bank.
    """

    anagrams = defaultdict(set)
    for word in words:
        key = "".join(sorted(word))
        anagrams[key].add(word)

    search = "".join(sorted(letters))
    if search in anagrams:
        return anagrams[search]


if __name__ == '__main__':
    while True:
        letters = input("What letters would you like to find the anagram of? ")
        letters = letters.lower().strip()
        anagram_list = find_anagrams(letters, english_words)
        if anagram_list:
            for anagram in anagram_list:
                print(anagram)
        else:
            print(f"{letters} word not found. Please try again!")

        response = input("\nDo you want to continue (type quit to exit)? ")
        if response.lower().strip() == 'quit':
            break
