# intakes a string,
# outputs a the same string with '%20' in the place of whitespaces

def URLify1(s):
    nw = '%20' # nw stands for non-whitespace
    # first, the edge cases involving a space at i = 0
    if s == ' ':
        return nw
    if len(s) == 2:
        if s[0] == ' ':
            s = nw + s[1]
        elif s[1] == ' ':
            s = s[0] + nw
    i = 1
    while 0 < i < len(s) - 1:
        if s[i] == ' ':
            s = s[:i] + nw + s[i+1:]
            i += 3
        else:
            i += 1
    if s[-1] == ' ':
        s = s[:-1] + nw
    print s


if __name__ == "__main__":
    input = raw_input(">> ")
    URLify1(input)
