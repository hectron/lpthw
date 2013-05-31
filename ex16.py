# import the library required to read the parameters.
from sys import argv

# grab the parameters from the input stream
script, filename = argv

# explains that we are going to 
# erase the file supplied from the input stream.
# Prompt how they cna exit this script.
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# Take in whatever input, but don't assign to a variable.
# This is used to ensure that they accept the terms above.
raw_input("?")

# Prints out the string and attempts to
# open that file with writing permissions
# It creates it if not available.
print "Opening the file..."
target = open(filename, 'w')

# Erases everything that is in that file.
print "Truncating the file. Goodbye!"
target.truncate()

# Prints out the instructions.
print "Now I'm going to ask you for three lines."

# Takes in three arguments from the command line.
line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

# Prints out what we are going to do.
print "I'm going to write those to the file."

# Writes line, empty line, line, empty line, line, empty line
# to the file.
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
# This is written again for extra credit.
input_string = "%r\n%r\n%r\n" % (line1, line2, line3)
target.write(input_string)

# Closes the file that was specified from the file.
print "And finally, we close it."
target.close()
