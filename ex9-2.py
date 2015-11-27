# Write a program to read throught the lines of a file brake each line into
# a list of words and then loop through each of the words in the line and count
# each word using a dictionary

filename = "romeo.txt"
try:
    fp = open( filename, "r")
except Exception as e:
    print  "File cannot be opened: ", filename
    exit()

words = list()
counts = dict()

for line in fp:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print  counts
