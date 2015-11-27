# make a little text aditor

from sys import argv

script, filename = argv

print "We are going to erase %r!" % filename
print "If you dont wont that, hit CTRL-C (^C)"
print "If you do want that hit RETURN"

raw_input("?")

print "Opening the file ..."
target = open(filename, "a+")

print "Truncating the file"
target.truncate()

print "Now i am going to ask you for three lines"

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally we close it"
target.close()


print "Close the program or continue"

answer = raw_input("y/n?")

if answer == "y":
    print "Type the filename to read the file:"
    filename = raw_input()
    target = open(filename, "r")
    print target.read()
    target.close()
elif answer == "n":
    print "Bye Bye!"
else:
    print "Invalid input <%s>" % answer
    print "Program close"
