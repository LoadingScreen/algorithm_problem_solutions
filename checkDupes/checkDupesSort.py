def checkDupesSort(s):
    print s
    ss = sorted(s)
    print ss
    for i in range(0,len(ss)-1):
        if ss[i] == ss[i+1]:
            print 'Duplicate found'
            return False
    print 'no duplicates'
    return True
