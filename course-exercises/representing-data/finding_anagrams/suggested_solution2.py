from wordsets import english_words, english_words_small
from collections import defaultdict


def find_anagrams(letters, words):
    # Create a dictionary subclass that adds sets for missing values.
    lookup = defaultdict(set, {})
    for word in words:
        lookup[''.join(sorted(word))].add(word)
    return lookup.get(''.join(sorted(letters)), set())


if __name__ == '__main__':
    while True:
        letters = input("What letters would you like to find the anagram of? ")
        letters = letters.lower().strip()
        anagram_list = find_anagrams(letters, english_words)
        if anagram_list:
            for anagram in anagram_list:
                print(anagram)
        else:
            print(f"Couldn't find anagram for the word: {letters}.")

        response = input("\nDo you want to continue (type quit to exit)? ")
        if response.lower().strip() == 'quit':
            break
