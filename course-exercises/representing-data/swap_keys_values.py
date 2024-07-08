from collections import defaultdict


def swap_keys_and_values(d):
    result = defaultdict(set)
    for key, value in d.items():
        result[value].add(key)
    return result


groceries = {"tomato": 5, "potato": 2, "sapota": 3, "milk": 2}
print(swap_keys_and_values(groceries))
