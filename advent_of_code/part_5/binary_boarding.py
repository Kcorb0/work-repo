file = "advent_of_code/part_5/input.txt"
b_passes = [i.replace("\n", "") for i in open(file, "r")]


def decode_pass(b_pass):
    row_code = b_pass[:-4]
    col_code = b_pass[-3:-1]
    r_range = list(range(0, 128))
    c_range = list(range(0, 8))

    for i in row_code:
        if i == "F":
            r_range = r_range[: len(r_range) // 2]
        else:
            r_range = r_range[len(r_range) // 2 :]

    if b_pass[:-3][-1] == "F":
        r_range = r_range[0]
    else:
        r_range = r_range[-1]

    for x in col_code:
        if x == "R":
            c_range = c_range[len(c_range) // 2 :]
        else:
            c_range = c_range[: len(c_range) // 2]

    if b_pass[-1] == "L":
        c_range = c_range[0]
    else:
        c_range = c_range[-1]

    return (r_range * 8) + c_range


decoded_passes = [decode_pass(i) for i in b_passes]
decoded_passes.sort()

# Part 1 Answer
print(f"Part 1: {max(decoded_passes)}")
# Part 2 Answer
for idx, i in enumerate(decoded_passes):
    if decoded_passes[idx] + 1 != decoded_passes[idx + 1]:
        print(f"Part 2: {i + 1}")
        break