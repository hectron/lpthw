from sys import argv

script, limit, increment = argv

def print_limit(limit, increment = 1):
    """ Prints out an array of numbers from 0 through the limit parameter.
    The increment is the step that we take while iterating through the numbers."""

#    i = 0
#    numbers = []

#    while i < limit:
#        print "At the top i is %d" % i
#        numbers.append(i)
#
#        i += increment
#        print "Numbers now: ", numbers
#        print "At the bottom i is %d" % i

#    print "The numbers: "

#    for n in numbers:
#        print n

    numbers = []

    for i in range(0, limit, increment):
        print "At the top i is %d" % i
        numbers.append(i)
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "
    for n in numbers:
        print n


print_limit(int(limit), int(increment))
