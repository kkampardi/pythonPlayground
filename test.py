# this is the real playground file
import string
try:
    fp = open('romeo.txt', 'r')
except Exception as e:
    print "Could not open file:  romeo.txt"
counts = dict()

for line in fp:
    # get rid of panctuation charachters
    line = line.translate(None, string.punctuation)
    # transform to lower case
    line = line.lower()
    # split to a list
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
# Sort the dictionary by value
lst = list()
# copy items to a list
for key, val in counts.items():
    lst.append((val, key))
# now sort by value
lst.sort(reverse=True)
# output 10 most common words in the file
for key, val in lst[:10]:
    print key, val
