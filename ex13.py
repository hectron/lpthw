from sys import argv

script, first, second, third, additional_step = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

"""
Extra credit.
"""

print "You entered %r." % additional_step

additional_step = raw_input("-->New value: ")

print "You entered %r." % additional_step
