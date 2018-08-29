
def palindromePermSort(s):
    if len(s) <= 1:
        print True
        return True
    elif len(s) < 4:
        length = len(s)
    else:
        length = len(s) - 1
    l = list(s)
    ls = sorted(l)
    pivots = 0
    i = 0
    while 0 <= i < length - 1:
        if ls[i] == ls[i+1]:
            i += 2
        else:
            i += 1
            pivots += 1
        if pivots == 2:
            print False
            return False
    print True
    return True

def palindromePermHash(s):
    h = {}
    pivotCount = 0
    for x in s:
        if x not in h:
            h[x] = 0
        h[x] += 1
    for x in s:
        if h[x] % 2 != 0:
                pivotCount += 1
        if pivotCount == 2:
            print False
            return False
    print True
    return True

if __name__ == "__main__":
    if raw_input("Use the sorting solution (s) or the Hash solution (h)?\n>>> ") == 'h':
        while True:
            s = raw_input(">>> ")
            palindromePermHash(s)
    else:
        while True:
            s = raw_input(">>> ")
            palindromePermSort(s)
