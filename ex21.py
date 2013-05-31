def add(a, b):
  print "ADDING %d + %d" % (a, b)
  return a + b

def subtract(a, b):
  print "SUBTRACTING %d - %d" % (a, b)
  return a - b

def multiply(a, b):
  print "MULTIPLYING %d * %d" % (a, b)
  return a * b

def divide(a, b):
  print "DIVIDING %d / %d" % (a, b)
  return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here's a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

print "\n\n\n\n"
print "Beginning Extra Credit.\n"
"""
Extra Credit Section.
"""
# 1.
def modulo(a, b):
  print "MODULO %d %% %d" % (a, b)
  return a % b


def print_attributes(age, height, weight, iq, fingers):
  print "Age: %d, Height: %d, Weight: %d, IQ: %d, Fingers: %d" % (
	  age, height, weight, iq, fingers)

fingers = modulo(50, 9)

print_attributes(age, height, weight, iq, fingers)

# 2.
operation1 = divide(iq, 2) # 25
operation2 = multiply(weight, operation1) # 4500
operation3 = subtract(height, operation2) # -4426
operation4 = add(age, operation3)

print operation4

# 3. Pointless since I'll be reverting it.

# 4.
modulo(fingers, divide(79.5, multiply(height, subtract(age, modulo(weight, 23)))))
