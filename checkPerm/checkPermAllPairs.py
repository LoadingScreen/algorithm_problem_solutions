# check each pair and cross them off when there is a match
# if all chars in both strings get crossed off, you have a
# permutation

def checkPermAllPairs(s1,s2):
    length = len(s2)
    if len(s1) != length:
        print "Nope. Different lengths."
    l1, l2 = list(s1), list(s2)
    crossout1 = list([0]*length)
    crossout2 = list([0]*length)
    for i in range(0, length):
        j = 0
        while 0 <= j < length:
            if crossout1[i] == 0 and crossout2[j] == 0:
                if l1[i] == l2[j]:
                    crossout1[i], crossout2[j] = 1,1
                    j = length
            j += 1
    print crossout1, crossout2
    if (0 in crossout1) or (0 in crossout2):
        print "S1 is NOT a permutation of S2."
        return False
    else:
        print "S1 is a permutation of S2."

# time complexity is O(n^2/2) = O(n^2)
# space complexity is O(4n) = O(n)

if __name__ == "__main__":
    while True:
        s1 = raw_input("Enter string #1.\n>> ")
        s2 = raw_input("Enter string #2.\n>> ")
        checkPermAllPairs(s1,s2)
