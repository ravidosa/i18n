import unidecode

inp = open("input-8.txt", "r", encoding="utf-8").read().split("\n")

valid = 0

for i in inp:
    u = unidecode.unidecode(i.lower())
    if 4 <= len(u) <= 12:
        if any(map(lambda c: c.isdigit(), u)):
            if any(map(lambda c: c in "aeiou", u)):
                if any(map(lambda c: c in "bcdfghjklmnpqrstvwxyz", u)):
                    if len(set(u)) == len(u):
                        print(i)
                        valid += 1

print(valid)