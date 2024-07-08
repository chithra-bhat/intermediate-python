def add_layer(triangle):
    last = triangle[-1]  # The most recent row of Pascal's triangle.
    row = []  # Build up the next row.
    for left, right in zip(last + (0,), (0,) + last):
        row.append(left + right)
    triangle.append(tuple(row))
    return triangle


pascals_triangle = [
    (1,),
    (1, 1),
    (1, 2, 1),
    (1, 3, 3, 1),
]

# Add a few layers, just to check.
output = []
for _ in range(5):
    output = add_layer(pascals_triangle)
print(output)
