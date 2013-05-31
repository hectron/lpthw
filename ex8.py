formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	)

"""
Extra credit
"""
# 1. No mistake.
# 2. It treats whatever input is given to it as either an int or an object. Since we fed %r a string, it's enclosed with single quotes.

# 2. Upon closer inspection, it seems since we used single quotes in the third parameter, it enclosed the whole thing in double quotes.
