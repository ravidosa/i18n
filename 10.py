import unicodedata, bcrypt, itertools

inp = open("input-10.txt", "r", encoding="utf-8").read().split("\n\n")

def powerset(iterable):
    "Subsequences of the iterable from shortest to longest."
    # powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

valid = 0

database = {i.split()[0]: i.split()[1] for i in inp[0].split("\n")}
truepass = {}

logins = inp[1].split("\n")
for ii, i in enumerate(logins):
    user, passw = i.split()
    if user in truepass:
        if truepass[user] == unicodedata.normalize("NFC", passw):
            valid += 1
    else:
        passwn = unicodedata.normalize("NFD", passw)
        hash = database[user]
        salt = hash[:29]
        comb = [ind for ind, b in enumerate(passwn.encode("utf-8")) if b == 204]
        for decombo in powerset(comb):
            chk = passwn.encode("utf-8")
            for rep in reversed(decombo):
                chk = chk[:rep - 1] + unicodedata.normalize("NFC", chk[rep - 1:rep + 2].decode("utf-8")).encode("utf-8") + chk[rep + 2:]
            if bcrypt.hashpw(chk, salt.encode('utf-8')).decode("utf-8") == hash:
                truepass[user] = unicodedata.normalize("NFC", passw)
                valid += 1
                break

print(valid)