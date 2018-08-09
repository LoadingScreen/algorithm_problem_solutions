from checkDupesSort import checkDupesSort
from checkDupesHash import checkDupesHash
from checkDupesScan import checkDupesScan
print 'test1'
if __name__ == "__main__":
    print 'test2'
    choice = raw_input("Enter a number to pick a solution method.\n1) sort\n2) hash\n3) scan\n>> ")

    if choice == '1':
        while True:
            input = raw_input("Enter a string.\n>>")
            checkDupesSort(input)
    elif choice == '2':
        while True:
            input = raw_input("Enter a string.\n>>")
            checkDupesHash(input)
    elif choice == '3':
        while True:
            input = raw_input("Enter a string.\n>>")
            checkDupesScan(input)
    else:
        print "Enter a valid option."
