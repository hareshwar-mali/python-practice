# write a code for count less than 100 and greater than 101
sample_list = [11, 301, 311, 401, 411, 21, 51, 101, 201, 251]

less_count = 0
greater_count = 0
for number in sample_list:
    if number < 100:
        less_count += 1
    else:
        greater_count += 1

print(less_count)
print(greater_count)
