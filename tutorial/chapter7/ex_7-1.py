#7.1 Write a program that prompts for a file name,
#then opens that file and reads through the file,
#and print the contents of the file in upper case. Use the file words.txt
#to produce the output below.

filename = raw_input("Enter the name of the file: ")

try:
    fhand = open(filename)
except Exception as e:
    print "File cannot be open: ", filename

for line in fhand:
    line = line.rstrip()
    toupper = line.upper()
    print toupper
