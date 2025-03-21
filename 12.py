import unidecode, string, functools, itertools

inp = open("input-12.txt", "r", encoding="utf-8").read().split("\n")

directory = [i.split(": ") for i in inp]
mid = len(directory) // 2

def cmp(pair, let):
    for l1, l2 in pair:
        if l1 == None:
            return -1
        elif l2 == None:
            return 1
        else:
            if l1 == l2:
                continue
            else:
                return let.index(l1) - let.index(l2)

def eng(it1, it2):
    let = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    last1, first1 = it1[0].split(", ")
    last2, first2 = it2[0].split(", ")

    letmap = lambda l: "".join(i if i in let else unidecode.unidecode(i) for i in l.upper().translate(str.maketrans('', '', string.punctuation)).replace(" ", ""))

    last1, last2, first1, first2 = map(letmap, [last1, last2, first1, first2])

    if last1 == last2:
        pair = itertools.zip_longest(first1, first2)
    else:
        pair = itertools.zip_longest(last1, last2)
    
    return cmp(pair, let)

def swed(it1, it2):
    let = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
    last1, first1 = it1[0].split(", ")
    last2, first2 = it2[0].split(", ")

    letmap = lambda l: "".join("Ä" if i == "Æ" else "Ö" if i == "Ø" else i if i in let else unidecode.unidecode(i) for i in l.upper().translate(str.maketrans('', '', string.punctuation)).replace(" ", ""))

    last1, last2, first1, first2 = map(letmap, [last1, last2, first1, first2])

    if last1 == last2:
        pair = itertools.zip_longest(first1, first2)
    else:
        pair = itertools.zip_longest(last1, last2)
    
    return cmp(pair, let)

def dut(it1, it2):
    let = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    last1, first1 = it1[0].split(", ")
    last2, first2 = it2[0].split(", ")

    last1 = " ".join(l for l in last1.split(" ") if l != l.lower())
    last2 = " ".join(l for l in last2.split(" ") if l != l.lower())

    letmap = lambda l: "".join(i if i in let else unidecode.unidecode(i) for i in l.upper().translate(str.maketrans('', '', string.punctuation)).replace(" ", ""))

    last1, last2, first1, first2 = map(letmap, [last1, last2, first1, first2])

    if last1 == last2:
        pair = itertools.zip_longest(first1, first2)
    else:
        pair = itertools.zip_longest(last1, last2)
    
    return cmp(pair, let)

english = sorted(directory, key=functools.cmp_to_key(eng))
swedish = sorted(directory, key=functools.cmp_to_key(swed))
dutch = sorted(directory, key=functools.cmp_to_key(dut))

prod = int(english[mid][1]) * int(swedish[mid][1]) * int(dutch[mid][1])

print(prod)