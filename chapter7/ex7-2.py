filename = raw_input("Enter the name of the file: ")

try:
    fhand = open(filename)
except Exception as e:
    print "File cannot be open: ", filename

linecounter = 0
av = 0
suma = 0
for line in fhand:
    line = line.rstrip()
        if line.startswith('X-DSPAM-Confidence:'):
        linecounter += 1
        num = float(line[20:26])
        suma = suma + num
print linecounter
av = suma / linecounter
print av
