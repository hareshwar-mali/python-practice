# merge two string
# str1 = 'abc'
# str2 = 'pqr
# output = 'apbqcr'


def merge_string(str1, str2):
    result = ''
    count = 0
    while count < len(str1) or count < len(str2):
        if count < len(str1):
            result += str1[count]
        if count < len(str2):
            result += str2[count]
        count += 1
    return result


str1 = 'abc'
str2 = 'pqr'
ot = merge_string(str1, str2)

print(ot)
