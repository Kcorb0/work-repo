def report(num):

    inp_file = [int(i) for i in open("part_1/inputs.txt", "r")]

    for i in inp_file:
        for j in inp_file:
            if i + j == num:
                return f"{i} + {j} = {num}\n{i} * {j} = {i*j}"

    return "There does not seem to be a match for that input sadge :("


print(report(2020))