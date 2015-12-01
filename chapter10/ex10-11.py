# Read and parse the "From" lines, in the mbox-short.txt, and pull out the
# addresses from the line. Using a dict count the number of messages of each
# person. After all the data has been read print the person with the most
# commits by creating a list of tuples (count, email) from the dict.
# Then sort the list in reverse order and prin out the person who has the
# most commits.

try:
    fh = open("mbox-short.txt", "r")
except Exception as e:
    print "Could not open file"

counts = dict()

for line in fh:
    line = line.rstrip()
    # get rid of unusefull lines
    if not line.startswith("From: "):
        continue
    # print "Debug: ", line
    words = line.split()
    email = words[1]
    # print "Debug: ", email
    if email not in counts:
        counts[email] = 1
    else:
        counts[email] += 1
# print  "Counts: ", counts
# sort by value
lst = list()
# move data to a tuple
for key, value in counts.items():
    lst.append((value, key))
# sort data by value
lst.sort(reverse=True)

for key, value in lst[:1]:
    print value, key
