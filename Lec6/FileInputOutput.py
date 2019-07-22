# Reading from a file

myFile = open("data\\Readfile.txt", 'r')
line = myFile.readline()
print(line)
myFile.close()

# This can also be written as below which does not explicitly require to close the file

with open("data\\ReadFile.txt", 'r') as myFile:
    line = myFile.readline()
    print(line)


# Writing to a file
with open("data\\WriteFile.txt", 'w') as myFile:
    myFile.write("Writing first line." + "\n")

with open("data\\WriteFile.txt", 'r') as myFile:
    print(myFile.readline())


# To read all the lines from a file we can either use while loop or as shown below

with open("data\\WriteFile.txt", 'r') as myFile:
    for linetoread in myFile:
        print(linetoread)

# To open a binary file like Word processor, image etc we can use parameters as 'rb', 'wb' and 'ab' while opening a file