inp = open("input-14.txt", "r", encoding="utf-8").read().split("\n")

MO2_TO_M2 = 1089000000

NUMERALS = {
    "一": 1,
    "二": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9,
    "十": 10,
    "百": 100,
    "千": 1000,
    "万": 10_000,
    "億": 100_000_000,
}

UNITS = {
    "毛": 1,
    "厘": 10,
    "分": 100,
    "寸": 1000,
    "尺": 10000,
    "間": 60000,
    "丈": 100000,
    "町": 3600000,
    "里": 129600000,
}

def decode(s):
    *dig, unit = s
    res = 0
    myrch, ch = 0, 0
    for d in dig:
        if d in "億万":
            res += (myrch + ch) * NUMERALS[d]
            myrch, ch = 0, 0
        elif d in "十百千":
            myrch += ch * NUMERALS[d] if ch else NUMERALS[d]
            ch = 0
        else:
            ch = NUMERALS[d]
    return (res + myrch + ch) * UNITS[unit]

area = 0

for i in inp:
    w, h = i.split(" × ")
    area += decode(w) * decode(h) // MO2_TO_M2

print(area)