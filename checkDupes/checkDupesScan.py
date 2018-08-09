def checkDupesScan(s):
    for i in range(0, len(s)-1):
        for j in range(i+1, len(s)):
            if s[i]==s[j] and i!=j:
                print "Duplicate Found"
                return False
    print "No duplicates"
    return True

#time compexity is O(n^2)
#space complexity is O(n)
