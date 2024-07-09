with open('queries.txt', 'r') as infile:
    contents = [line.strip().lower() + '\n' for line in infile if line.strip()]

    with open('output.txt', 'w') as outfile:
        outfile.writelines(contents)
