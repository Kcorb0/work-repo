file = "advent_of_code/part_5/input.txt"
b_passes = [i.replace("\n", "") for i in open(file, "r")]


def decode_pass(b_pass):
    row_range = list(range(0, 128))
    col_range = list(range(0, 8))

    for i in b_pass[:-4]:
        if i == "F":
            row_range = row_range[: len(row_range) // 2]
        else:
            row_range = row_range[len(row_range) // 2 :]

    for x in b_pass[-3:-1]:
        if x == "R":
            col_range = col_range[len(col_range) // 2 :]
        else:
            col_range = col_range[: len(col_range) // 2]

    if b_pass[:-3][-1] == "F":
        row_range = row_range[0]
    else:
        row_range = row_range[-1]

    if b_pass[-1] == "L":
        col_range = col_range[0]
    else:
        col_range = col_range[-1]

    return row_range * 8 + col_range


decoded_passes = [decode_pass(i) for i in b_passes]
decoded_passes.sort()

# Part 1 Answer
print(f"A1: {max(decoded_passes)}")
# Part 2 Answer
for idx, i in enumerate(decoded_passes):
    if decoded_passes[idx] + 1 != decoded_passes[idx + 1]:
        print(f"A2: {i + 1}")
        break