from itertools import count


def count_substring_occurrences(input_string, substring):
    count = 0
    index = 0
    while True:
        index = input_string.find(substring, index)
        if index == -1:
            break
        count += 1
        index += 1
    return count


a = count_substring_occurrences('haari baare hhaa, haa', 'haa')
print(a)