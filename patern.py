# *
# * *
# * * *
# * * * *
# * * * * *
n = int(input('Enter the number of rows '))
for i in range(0,n):
    for j in range(0, i+1):
        print('*', end=' ')
    print()

count = 1
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print(count, end=' ')
        count += 1
    print()


# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15