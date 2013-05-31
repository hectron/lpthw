# import the system arguments to read from the input stream
from sys import argv

# grab the arguments from the input stream
script, input_file = argv

# define a function called print_all
def print_all(f):
  """
  Reads the file passed in as a parameter.
  """
  print f.read()

# defines a rewind function
def rewind(f):
  """
  Returns to the first byte in the file.
  """
  f.seek(0)

# defines a function called print_a_line
def print_a_line(line_count, f):
  """
  Prints out the line number for given
  file "f".
  """
  print line_count, f.readline()

# opens the file passed in as an argument
# assigns it to a variable.
current_file = open(input_file)

# prints out a string
print "First let's print the whole file:\n"

# makes a call to print_all with the given file.
# prints all the contents of the file.
print_all(current_file)

# prints out a string
print "Now let's rewind, kind of like a tape."

# makes a call to rewind() with the given file.
# goes to the first byte of the file.
rewind(current_file)

# prints out a string
print "Let's print three lines:"

# starts a line counter
current_line = 1

# prints the line counter's line from the
# opened file. Currently, line 1
print_a_line(current_line, current_file)

# increments the line counter (line 2)
# current_line = current_line + 1 # Rewritten in EC
current_line += 1
print_a_line(current_line, current_file)

# Line 3
# current_line = current_line + 1 # Rewritten in EC
current_line += 1
print_a_line(current_line, current_file)

current_file.close()
