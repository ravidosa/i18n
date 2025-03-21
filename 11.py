inp = open("input-11.txt", "r", encoding="utf-8").read().split("\n")

caesar = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
od = ["Οδυσσευ".upper(), "Οδυσσευς".upper(), "Οδυσσεως".upper(), "Οδυσσει".upper(), "Οδυσσεα".upper(), "Οδυσσευ".upper()]

rot = 0

for i in inp:
    enc = i.upper()
    for r in range(len(caesar)):
        dec = "".join(caesar[(caesar.index(c) + r) % len(caesar)] if c in caesar else c for c in enc)
        if any(o in dec for o in od):
            rot += r
            break

print(rot)