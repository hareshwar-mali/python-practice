# Count a number of sub string

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count


# how many substring are possible
def print_substr(str):
    n = len(str)
    for i in range(n):
        for j in range(i+1, n+1):
            print(str[i:j])
str = 'abc'
print_substr(str)

