# Substitutes the number 10 into the %d portion of the string.
x = "There are %d types of people." % 10

# Assign variable names
binary = "binary"
do_not = "don't"

# Fills in the %s with the tuple provided.
y = "Those who know %s and those who %s." % (binary, do_not)

# Prints the variables.
print x
print y

# Substitutes the previous sentence (note that the placeholders are filled in).
print "I said: %r." % x
print "I also said '%s'." % y

# Creates a boolean variable.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Prints out the joke with the boolean filled in.
print joke_evaluation % hilarious

# Create two strings and assign them to the w, e variables.
w = "This is the left side of..."
e = "a string with a right side."

# Concatenates the strings
print w + e

"""
Extra credit questions are 
answered in the following section
"""
# 1. Done.
# 2. There are only four places where STRINGS are placed.
# 4. They are concatenated; that is, they are appended.
