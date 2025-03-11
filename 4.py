import datetime, pytz

inp = open("input-4.txt", "r").read().split("\n\n")

travel = 0

for i in inp:
    dept, arr = i.split("\n")
    _, dtz, ddt = dept.split(maxsplit=2)
    _, atz, adt = arr.split(maxsplit=2)
    ddt = pytz.timezone(dtz).localize(datetime.datetime.strptime(ddt, "%b %d, %Y, %H:%M"))
    dat = pytz.timezone(atz).localize(datetime.datetime.strptime(adt, "%b %d, %Y, %H:%M"))
    travel += int((dat - ddt).total_seconds()) // 60

print(travel)