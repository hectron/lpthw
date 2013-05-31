tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = ''' 
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

"""
Extra credit section
"""
start_list = "I'll do a list:"
grocery_list = "\t* %r\n\t* %r\n\t* %r"

print start_list
print grocery_list % ('cat food', "steak fries", 'burrito sauce')
