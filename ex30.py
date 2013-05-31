# Assigns the amounts to the variables.
people = 30
cars = 40
buses = 15


# If 40 > 30
if cars > people:
  print "We should take the cars."
# If not true, then 40 < 30
elif cars < people:
  print "We should not take the cars."
# Otherwise just print a fallback.
else:
  print "We can't decide."

# If 15 > 40
if buses > cars:
  print "That's too many buses."
# Otherwise, if 15 < 40
elif buses < cars:
  print "Maybe we could take the buses."
# Otherwise print the default message.
else:
  print "We still can't decide."

# If there are more people than buses
if people > buses:
  print "Alright, let's just take the buses."
# Otherwise print the default message.
else:
  print "Fine, let's stay home then."

