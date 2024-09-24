file = open("poem.txt")
#print(file.readline())
#print(file.readline())
#print(file.read())
lines = file.readlines()
lines.sort()
print(lines)

'''
 readline(): will read one line of the file depending on the position it is in
 read() will read the whole file
 close() will close the file
 strip() will remove all white space
 sort() will sort the lines alphabetically
'''

with open("poem.txt") as file:
    for line in file:
        print(line.strip().upper())