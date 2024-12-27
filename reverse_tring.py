
def reversestring(s) -> str:
    # code here
    s = s[::-1]
    return s
s='abcde'
a = reversestring(s)



def is_same(s):
    # code here
    add = ""
    for i in range(len(s)):
        if s[i].isdigit():
            add += (s[i])
    result = int(add)
    l = len(s) - len(add)
    if result == l:
        return 1
    else:
        return 0

k = is_same('gypgqgr07')
