import datetime

inp = open("input-2.txt", "r").read().split("\n")

wave = {}

for i in inp:
    dt = datetime.datetime.fromisoformat(i)
    wave[str(dt - dt.utcoffset())[:-6]] = wave.get(str(dt - dt.utcoffset())[:-6], 0) + 1

target = max(wave, key=lambda t: wave[t])
print(target.replace(" ", "T") + "+00:00")