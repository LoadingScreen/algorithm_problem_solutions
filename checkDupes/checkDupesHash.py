def checkDupesHash(s):
    h = {}
    for i in range(0,len(s)):
        h[s[i]] = 1
    for i in range(0, len(s)):
        if h[s[i]] == 2:
            print "Duplicate found"
            return False
        h[s[i]] = 2
    print "No duplicates"
    return True


# time complexity is O(n)
# space complexity is O(n)
