inp = open("input-6.txt", "r", encoding="utf-8").read().split("\n\n")

sol = 0

cross = inp[1].split("\n")
match = []
for c in cross:
    ind = 0
    while c.strip()[ind] == ".":
        ind += 1
    match.append((c.strip()[ind], ind, len(c.strip())))

words = inp[0].split("\n")
for ind, i in enumerate(words):
    if (ind + 1) % 3 == 0:
        i = i.encode("iso-8859-1").decode("utf-8")
    if (ind + 1) % 5 == 0:
        i = i.encode("iso-8859-1").decode("utf-8")
    for m in match:
        if m[1] < len(i) and i[m[1]].lower() == m[0].lower() and len(i) == m[2]:
            sol += (ind + 1)

print(sol)