
def checkPermHash(s1,s2):
    if len(s1) != len(s2):
        print "S1 is NOT a permutation of S2."
        return False
    h1, h2 = {}, {}
    length = len(s1)
    for i in range(0,length):
        h1.setdefault(s1[i], 0)
        h1[s1[i]] += 1
    for j in range(0, length):
        h2.setdefault(s2[j], 0)
        h2[s2[j]] += 1
    for k in range(0, length):
        if h1.setdefault(s1[k], 0) != h2.setdefault(s1[k], 0):
            print "S1 is NOT a permutation of S2."
            return False
    print "S1 is a permutation of S2."
    return True

# time complexity is O(n+n+2n) = O(n)
# space complexity is O(n)

if __name__ == "__main__":
    while True:
        s1 = raw_input("gimme the first string:\n>> ")
        s2 = raw_input("ok now gimme the second string:\n>> ")
        print "Thanks."
        checkPermHash(s1, s2)
