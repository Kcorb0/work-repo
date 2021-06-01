def pass_validator(inp):

    inp_sep = inp.replace(" ", "").split(":")
    char = inp_sep[0][-1]
    char_amnt = inp_sep[0][:-1].split("-")
    password = inp_sep[1]

    char_cnt = password.count(char)

    if char_cnt in range(int(char_amnt[0]), int(char_amnt[1]) + 1):
        return True
    else:
        return False


def total_valid(pass_file):

    inp_file = [i.replace("\n", "") for i in (open(pass_file, "r"))]
    cnt = 0

    for i in inp_file:
        if pass_validator(i) == True:
            cnt += 1

    return cnt


print(total_valid("part_2/inputs.txt"))
