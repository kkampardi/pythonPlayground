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

for key in counts:
    if counts[key] < 3:
        print  key, counts[key]
