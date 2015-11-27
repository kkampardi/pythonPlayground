from sys import argv

script, filename = argv

target = open(filename, "r")
for line in filename:
    line = line.rstrip()
    print target.read()
