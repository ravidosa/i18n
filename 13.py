inp = open("input-13.txt", "r", encoding="utf-8").read().split("\n\n")

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
    b = bytes.fromhex(i)

    if i.startswith("fffe") or i.startswith("feff"):
        ch = [b.decode("utf-16")]
    elif i.startswith("efbbbf"):
        ch = [b.decode("utf-8-sig")]
    else:
        ch = []
        for enc in ["utf-8", "utf-16-le", "utf-16-be", "latin-1"]:
            try:
                c = b.decode(enc)
                if all(ii not in c for ii in ["©", "\ufeff", "¶", "Ã¤", "Ã\x9f", "\0", "¼", "¢"]):
                    ch.append(c)
            except:
                continue
    for m in match:
        for c in ch:
            if m[1] < len(c) and c[m[1]].lower() == m[0].lower() and len(c) == m[2]:
                print(m, c, ind + 1)
                sol += (ind + 1)

print(sol)