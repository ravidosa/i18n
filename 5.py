inp = open("input-5.txt", "r", encoding="utf-8").read().split("\n")

poo = 0

for i in range(len(inp)):
    poo += inp[i][(2 * i) % len(inp[i])] == "💩"

print(poo)