# 9.1 Write a program that reads the words in words.txt and stores them as keys
# a dictionary it doesn't matters what the values are. Then you can use the in
# in operator as a fast way to check whether string is in a dictionary.


filename = "words.txt"
try:
    fp = open( filename, "r")
except Exception as e:
    print  "File cannot be opened: ", filename

words = dict()
i = 0
for line in fp:
    line = line.rstrip()
    print "Debug: ", line
    for word in line.split():
        words[word] = i
        i += 1

fp.close()
