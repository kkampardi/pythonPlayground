# 9.4 Write a program to read through the mbox-short.txt and figure out who has
# the sent the greatest number of mail messages. The program looks for 'From '
# lines and takes the second word of those lines as the person who sent the
# mail. The program creates a Python dictionary that maps the sender's mail
# address to a count of the number of times they appear in the file. After the
# dictionary is produced, the program reads through the dictionary using a
# maximum loop to find the most prolific committer.

filename = raw_input('Enter the filename: ')

# handle file opened
try:
    fp = open(filename, 'r')
except Exception as e:
    print "Failed open file: ", filename
    exit()

# init varribles and structures
emails_counter = dict()
counter = 0
key = 0
i = 0
for line in fp:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    # now process with interesting lines
    words = line.split()
    sender = words[1]
    if sender not in emails_counter:
        emails_counter[sender] = 1
    else:
        emails_counter[sender] += 1
# print emails_counter

for i in emails_counter:
    # print "Debug: ", i, emails_counter[i]
    if emails_counter[i] > counter:
        counter = emails_counter[i]
        key = i
print key, counter
