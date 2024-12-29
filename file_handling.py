# There are two type of file text file and binary file
# Text file is a human redable
# binary file is no-redable
# create new file using 'x' mode
# create_file = open('file_1.txt', 'w+')
# print(create_file.tell()) # tells the corsor position
# create_file.write('hiii')
# print(create_file.tell())
#
# create_file.write('\n welcome to file handling using seek function')
# print(create_file.tell())
# create_file.seek(0) # using seek function you can read the file data
# print(create_file.read())
# create_file.close()

# append mode
file = open('file_1.txt', 'a+')
print(file.tell())
file.seek(0)

print(file.read())
file.write('\n this is append mode')

