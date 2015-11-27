# this is the real playground file
fname = raw_input("Enter the filename")
if len(fname) < 1:
    fname = 'romeo.txt'
try:
    fh = open(fname)
except Exception as e:
    print "File cannot be open: ", fname

words = dict()
i = 0
for line in fh:
    line = line.rstrip()
    x = line.split()
    words[i] = x[i]
    i = i + 1
    print line
print words
