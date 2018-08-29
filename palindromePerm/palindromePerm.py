

def palindromePermSort(s):
    if len(s) <= 1:
        print True
        return True
    l = list(s)
    ls = sorted(l)
    pivots = 0
    i = 0
    while 0 <= i < len(s)-2:
        if ls[i] == ls[i+1]:
            i += 2
        else:
            i += 1
            pivots += 1
        # if pivots == 2 or (pivots == 1 and len(s)==2):
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
    while True:
        s = raw_input(">>> ")
        palindromePermHash(s)
