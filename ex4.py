# Total number of cars
cars = 100

# Space in a standard car.
space_in_a_car = 4.0

# Amount of drivers
drivers = 30

# People (might be drivers) wishing to be in a car.
passengers = 90

# Total cars NOT driven. That is, since there are only N drivers and M cars, there are M - N cars remaining.
cars_not_driven = cars - drivers

# Cars driven directly corresponds with drivers.
cars_driven = drivers

# The carpool capacity is the average number of spaces in a car by the number of cars with drivers. If a car has no driver, then you can't carpool.
carpool_capacity = cars_driven * space_in_a_car

# Average number of passengers per car.
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

"""
This is the extra credit section.
"""
# 1. Since we are going to be multiplying spaces are not all or nothing. There are either 0 - 4 spaces in a car.
# 2. Floating point means decimal. These have more precision and can get rather granular.
# 3.
