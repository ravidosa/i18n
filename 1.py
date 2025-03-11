inp = open("input-1.txt", "r", encoding="utf-8").read().split("\n")

cost = 0

for i in inp:
    bytes = len(i.encode('utf-8'))
    chars = len(i)
    cost += (13 if bytes <= 160 and chars <= 140 else 11 if bytes <= 160 else 7 if chars <= 140 else 0)

print(cost)