import datetime, zoneinfo

inp = open("input-7.txt", "r").read().split("\n")

HALIFAX = zoneinfo.ZoneInfo("America/Halifax")
SANTIAGO = zoneinfo.ZoneInfo("America/Santiago")

sol = 0

for ind, i in enumerate(inp):
    dt, corr, inc = i.split()
    dt = datetime.datetime.fromisoformat(dt)
    loc = HALIFAX if HALIFAX.utcoffset(dt) == dt.utcoffset() else SANTIAGO
    dt += datetime.timedelta(minutes=int(corr) - int(inc))
    dt = dt.astimezone(loc)
    sol += dt.hour * (ind + 1)

print(sol)