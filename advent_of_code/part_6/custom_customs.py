file = "advent_of_code/part_6/input.txt"
groups = open(file, "r").read().split("\n\n")
individuals = [i.split("\n") for i in groups]

p1_cnt = 0


for i in individuals:
    p1_cnt += len(set("".join(i)))

p2_cnt = 0

# cnt all letters, if greater than 1 increase count
for i in individuals:
    p2_cnt += len(set.intersection(*map(set, i)))

print(f"Part 1: {p1_cnt}")
print(f"Part 2: {p2_cnt}")
