import random
def shuffle(card,n):
    for i in range(n):
        a = random.randint(0,20)
        r = i + a % (19 - i)
        temp = card[i]
        card[i] = card[r]
        card[r] = temp

a = ["salamon/BT3-033", "patamon/EX1-024", "lucemon/BT4-115", "salamon/BT2-034", "patamon/BT1-048", "lucemon/BT4-115" ,"salamon/BT2-034", "salamon/BT3-033", "angemon/BT1-O55", "angemon/ST3-05", "magnaangemon/BT1-060", "angewomon/ST3-09", "cherubimon/BT3-041", "seraphimon/BT1-063", "chaosmon/BT4-091", "gatomon/EX1-026", "lopmon/BT3-034","unimon/ST3-07", "unimon/ST3-07"]
shuffle(a,19)
print("security stack", a[:5], "starting hand", a[5:10], "remaining deck", a[10:])
