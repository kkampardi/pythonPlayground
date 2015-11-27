# get the argv feature from sys package
from sys import argv

# assign varriable to the argv file name comes from stdin
script, filename = argv

# open the file and assign its "pointer" to the txt var
txt = open(filename)

# print out the file name
print "Here is your file %s" % filename
# print out the hole file in one line
print txt.read()
# ask user to type the file name again
	
