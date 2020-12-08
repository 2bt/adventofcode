s1 = s2 = 0
for p in open("input").read().split("\n\n"):
    if {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} - { w[:3] for w in p.split() }: continue
    s1 += 1
    valid = True
    for w in p.split():
        k, v = w.split(":")
        if k == "byr": valid &= 1920 <= int(v) <= 2002
        if k == "iyr": valid &= 2010 <= int(v) <= 2020
        if k == "eyr": valid &= 2020 <= int(v) <= 2030
        if k == "hgt":
            if   v[-2:] == "cm": valid &= 150 <= int(v[:-2]) <= 193
            elif v[-2:] == "in": valid &= 59 <= int(v[:-2]) <= 76
            else: valid = False
        if k == "hcl": valid &= len(v) == 7 and v[0] == "#" and not set(v[1:]) - set("0123456789abcdef")
        if k == "ecl": valid &= v in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        if k == "pid": valid &= v.isdigit() and len(v) == 9
    s2 += valid
print(s1, s2)

