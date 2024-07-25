def generate_tribonacci_numbers():
    a, b, c = 0, 0, 1
    # Yield an infinite stream of Tribonacci numbers!
    # The next value of the sequence will be c + b + a.
    while True:
        yield a
        a, b, c = b, c, a + b + c


def is_tribonacci(num):
    """Return whether `num` is a Tribonacci number."""
    # Be careful to not loop infinitely!
    for i in generate_tribonacci_numbers():
        if i < num:
            continue
        return i == num


print(f"44 is a tribonacci number? {is_tribonacci(44)}")
print(f"45 is a tribonacci number? {is_tribonacci(45)}")
