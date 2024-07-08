def add_layer(triangle):
    # Add a layer to Pascal's triangle.
    # Each layer should be a tuple.

    if not triangle:
        triangle.append((1,))
    else:
        prev_row = triangle[-1]
        new_row = [1]

        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])

        new_row.append(1)
        triangle.append(tuple(new_row))
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
