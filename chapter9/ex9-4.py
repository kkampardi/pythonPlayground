# Write a program that categorizes each mail message by witch day of the week
# the commit was done. To do this look for lines start with 'From' then look for
# the third word and keep a running count of each of the days of the week.
# At the end of the program print out the contents of your dictionary,
# order doesn't count.

filename = "mbox-short.txt"

# handle file opened
try:
    fp = open(filename, 'r')
except Exception as e:
    print "Failed open file: ", filename
    exit()

# init varribles and structures
dayCounter = dict()
i = 0
for line in fp:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    # now process with interesting lines
    words = line.split()
    day = words[2]
    if day not in dayCounter:
         dayCounter[day] = 1
    else:
        dayCounter[day] += 1
print dayCounter
