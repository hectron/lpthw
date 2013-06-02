ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

# finds the value of ten_things, finds the split method and calls
# split(ten_things, ' ')
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
  # looks up more_stuff, hits the ., and calls pop(more_stuff)
  next_one = more_stuff.pop()
  print "Adding: ", next_one
  # finds stuff, and calls append(stuff, next_one)
  stuff.append(next_one)
  print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar!
