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

''' whenever you open a file, we need to close it. 
But Sometimes we might forget to close. zTo resilve this we use built in statements'''

with open("test.txt") as my_file:  #default mode for reading
    print(my_file.readlines())

with open("test.txt", mode = 'r') as my_file: 
    print(my_file.readlines())

with open("test.txt", mode = 'r+') as my_file: #this will read and write into file
    text = my_file.write("helloooo")
    print(text)

with open("test.txt", mode = 'a') as my_file: #this will append the text into already available file
    text = my_file.write("sweety")
    print(text)

with open("test.txt", mode = 'w') as my_file: #this will write into file. write mood can create a file or it can rewrite an existing file. be careful
    text = my_file.write(": 0")
    print(text)