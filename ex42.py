## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def run(self):
        # speed is an attribute that should be in mph
        self.speed = 10

## Make a class Dog that is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## from self find the name attribute and assign it name
        self.name = name

## Make a class Cat that is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## from self find the attribute name and assign it name (from arguments)
        self.name = name

## Make a class called Person that is-a object
class Person(object):

    def __init__(self, name):
        ## from self find the person attribute name and assign it name (from aguments)
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

    def shower(self):
        self.clean = True

## Make a class called Employee that is-a Person object
class Employee(Person):

    def __init__(self, name, salary):
        ## hmm what is this strange music?
        ## Get the super-implementation of Employee -- which is a Person object
        ## passing itself as an argument. Afterward, call the __init__ function
        ## of the super implementation using the Employee name argument
        super(Employee, self).__init__(name)

        ## Employee has-a salary attribute and assign it the salary from the argument.
        self.salary = salary

## Make a class Fish that is-a object
class Fish(object):
    pass

## Make a class Salmon that is-a Fish
class Salmon(Fish):
    pass

## Make a class Halibut that is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Assign Satan to Mary's pet attribute
mary.pet = satan

## frank is an Employee that has-a salary of 120000
frank = Employee("Frank", 120000)

## frank has-a pet which is rover
frank.pet = rover

## flipper is an instance of a Fish
flipper = Fish()

## crouse is an instance of a Salmon
crouse = Salmon()

## harry is an instance of a Halibut
harry = Halibut()

frank.shower()
print "Is %s clean? %s" % (frank.name, frank.clean)

