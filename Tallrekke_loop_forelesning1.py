list_a = [12,4,7,18,4,2,9,15]

def laveste():
    minst = list_a[0]
    for x in list_a:
        if x < minst:
            minst = x
    print(minst)

def storste():
    maxa = list_a[0]
    for m in list_a:
        if m > maxa:
            maxa = m
    print(maxa)

def summering():
    tot = 0
    for s in list_a:
        tot += s
    print(tot)

def tre_func():
    laveste()
    storste()
    summering()

tre_func()
