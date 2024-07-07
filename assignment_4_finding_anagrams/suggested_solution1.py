from wordsets import english_words, english_words_small


def find_anagrams(letters, words):
    lookup = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in lookup:
            lookup[key] = set()
        lookup[key].add(word)

    # Search the lookup table for the queried letters.
    search = ''.join((sorted(letters)))
    return lookup.get(search, set())


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
