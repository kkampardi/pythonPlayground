# 8.4 Open the file romeo.txt and read it line by line. For each line, split
# the line into a list of words using the split() function. The program should
# build a list of words. For each word on each line check to see if the word
# is already in the #list and if not append it to the list. When the program
# completes, sort and print the resulting words in alphabetical order.

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
words = list()
for line in fh:
    line = line.rstrip()
    lst = line.split()
    print "Debug: ", set(lst).difference(words)
    lst = list(set(lst).difference(words))
    for i in range(len(lst)):
        words.append(lst[i])
    words.sort()
print words
