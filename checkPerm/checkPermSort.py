# Returns true iff s1 is a permutation of s2

def checkPermSort(s1, s2):
    if len(s1) != len(s2):
        print "S1 is NOT a permutation of S2."
        return False
    s1s, s2s = sorted(s1), sorted(s2)
    for i in range(0, len(s1)):
        if s1s[i] != s2s[i]:
            print "s1 is NOT a permutation of s2."
            return False
    print "s2 is a permutation of s1"
    return True

# time complexity is O(nlogn)
# space complexity is O(n)

if __name__ == "__main__":
    while True:
        s1 = raw_input("Enter the first string.\n>> ")
        s2 = raw_input("Enter the second string.\n>> ")
        checkPermSort(s1,s2)
