inp = open("input-3.txt", "r", encoding="utf-8").read().split("\n")

valid = 0

for i in inp:
    if 4 <= len(i) <= 12:
        if any(map(lambda c: c.isdigit(), i)):
            if any(map(lambda c: c.isalpha() and c == c.lower(), i)):
                if any(map(lambda c: c.isalpha() and c == c.upper(), i)):
                    if any(map(lambda c: not c.isascii(), i)):
                        valid += 1

print(valid)