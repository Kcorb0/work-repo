def pass_validator(inp):

    inp_sep = inp.replace(" ", "").split(":")
    char = inp_sep[0][-1]
    char_index = [int(i) for i in inp_sep[0][:-1].split("-")]
    password = inp_sep[1]
    char_cnt = password.count(char)

    index_1 = char_index[0] - 1
    index_2 = char_index[1] - 1

    if index_1 < len(password) and index_2 < len(password):
        if password[index_1] == char and password[index_2] == char:
            return False
        elif password[index_1] == char or password[index_2] == char:
            return True
    elif index_1 == char:
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


print(total_valid("part_2+/inputs.txt"))
