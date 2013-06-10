class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

    def override(self):
        print "PARENT override()"

    def altered(self):
        print "PARENT altered()"


class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

# Calls the implicit function from the parent on both cases
dad.implicit()
son.implicit()

# Calls the override function on each objcet. It is overriden
# by the child object
dad.override()
son.override()

# Calls the altered function on each object. Since Child is-a
# Parent, it overrides the altered function. It will call
# the parent using itself as an argument, and call the altered()
# function
dad.altered()
son.altered()
