import datetime

inp = open("input-9.txt", "r").read().split("\n")

fdict = {"%y-%m-%d": "YMD", "%y-%d-%m": "YDM", "%m-%y-%d": "MYD", "%m-%d-%y": "MDY", "%d-%m-%y": "DMY", "%d-%y-%m": "DYM"}
nine_eleven = {"YMD": "01-09-11", "YDM": "01-11-09", "MYD": "09-01-11", "MDY": "09-11-01", "DMY": "11-09-01", "DYM": "11-01-09"}

formats = {}
dates = {}
writers = set()

for i in inp:
    dat, names = i.split(": ")
    poss = list(fdict.values())
    for format_string in ["%y-%m-%d", "%y-%d-%m", "%m-%y-%d", "%m-%d-%y", "%d-%m-%y", "%d-%y-%m"]:
        try:
            datetime.datetime.strptime(dat, format_string)
        except:
            poss.remove(fdict[format_string])
    for n in names.split(", "):
        formats[n] = list(set(formats.get(n, fdict.values())).intersection(poss))
        dates[n] = dates.get(n, []) + [dat]

for n in dates:
    for fmt in formats[n]:
        if nine_eleven[fmt] in dates[n]:
            writers.add(n)

print(" ".join(sorted(writers)))