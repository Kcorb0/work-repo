import regex as re

PASSPORTS = open("advent_of_code/part_4/passports.txt", "r")
PASS_FILE = PASSPORTS.read().split("\n\n")
SORTED_PASSPORTS = [i.replace(" ", "\n") for i in PASS_FILE]


def validity_check(passport):
    fields = passport.split("\n")
    pass_dict = {}

    for i in fields:
        split_fields = i.split(":")
        pass_dict[split_fields[0]] = split_fields[1]

    if "cid" in pass_dict:
        pass_dict.pop("cid")

    if len(pass_dict) != 7:
        return False
    elif check_fields(pass_dict) == False:
        return False
    else:
        return True


def check_fields(fields):
    f = fields

    # Check fields byr, iyr, eyr
    if len(f["byr"]) != 4 or int(f["byr"]) not in range(1920, 2003):
        print("byr")
        return False
    elif len(f["iyr"]) != 4 or int(f["iyr"]) not in range(2010, 2021):
        print("iyr")
        return False
    elif len(f["eyr"]) != 4 or int(f["eyr"]) not in range(2020, 2031):
        print("eyr")
        return False

    # Check field hgt
    if "cm" in f["hgt"][-2:] and int(f["hgt"][:-2]) not in range(150, 193):
        print("hgt")
        return False
    elif "in" in f["hgt"][-2:] and int(f["hgt"][:-2]) not in range(59, 76):
        print("hgt")
        return False

    # Check field hcl
    if f["hcl"][0] != "#" or len(f["hcl"]) != 7:
        print("hcl")
        return False
    elif re.search("[g-zG-Z]", f["hcl"]):
        print("hcl")
        return False

    # Chekc field ecl
    if f["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        print("ecl")
        return False

    if len(f["pid"]) != 9:
        print("pid")
        return False

    print("real")
    return True


cnt = 0
for i in SORTED_PASSPORTS:
    if validity_check(i):
        cnt += 1

print(cnt)
