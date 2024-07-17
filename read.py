my_file = open("test.txt")

print(my_file)

print(my_file.read())

# read again from initial index

my_file.seek(0)

print(my_file.read())

# real line

print(my_file.readline())

# all lines

print(my_file.readlines())

# whenever you open a file, you need to close it

my_file.close()