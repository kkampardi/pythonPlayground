# write a program to read through a mail log, build a histogram using a
# dictionary to count how many messages have come from each email address
# and print the dictionary

filename = "mbox-short.txt"

# handle file opened
try:
    fp = open(filename, 'r')
except Exception as e:
    print "Failed open file: ", filename
    exit()

# init varribles and structures
mailCounter = dict()
i = 0

for line in fp:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    print line
