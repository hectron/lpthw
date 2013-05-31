# import the required libraries to analyze arguments
from sys import argv

# retrieve the script name (first argument) and the filename (second argument)
script, filename = argv

# Opens the filename based on the second argument given to python
txt = open(filename)

# Prints out the line with the filename provided
print "Here's your file %r:" % filename

# Reads the text file in its entirety and prints it out
print txt.read()

# Prints out the string to prompt the user for another string.
print "Type the filename again:"
file_again = raw_input("> ")

# Opens the file again
txt_again = open(file_again)

# Prints the file again
print txt_again.read()

"""
Extra credit
"""
txt.close()
txt_again.close()
