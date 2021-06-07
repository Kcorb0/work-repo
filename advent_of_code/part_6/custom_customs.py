file = "advent_of_code/part_6/input.txt"
groups = open(file, "r").read().split("\n\n")
individuals = [i.split("\n") for i in groups]

print(individuals[0])
