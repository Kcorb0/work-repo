file = "advent_of_code/part_6/input.txt"
groups = open(file, "r").read().split("\n\n")
individuals = [i.split("\n") for i in groups]

cnt = 0

for i in individuals:
    cnt += len(set("".join(i)))

print(f"Part 1: {cnt}")
