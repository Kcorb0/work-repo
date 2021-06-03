def palindromic(start, end):

    values = [i for i in range(start, end)][::-1]

    all_pals = []
    products = []

    for i in values:
        for x in values:
            num = x * i
            if str(num) == str(num)[::-1]:
                print(f"{x} * {i} = {num}")
                all_pals.append(num)

    return max(all_pals)


print(palindromic(100, 1000))