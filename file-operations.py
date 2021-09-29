
my_file = open("file.txt", "w")
my_file.write("first line\n")
my_file.write("second line\n")
my_file.write("third line\nfourth line\n")
my_file.close()

with open("file.txt", "a") as my_file:
    my_file.write("first line\n")
    my_file.write("second line\n")
    my_file.write("third line\nfourth line\n")


with open("file.txt", "r") as my_file:
    for line in my_file:
        line = line.strip()
        print(line)


with open("file.txt") as my_file:
    content = my_file.readlines()
    print(content)

with open("file.txt") as my_file:
    content = my_file.read()
    print(content)

