import time
import operator
from random import randint, shuffle, choice
from math import sqrt

# We create the constants here.

## Time constants

start_time = 0
actual_time = 0
estimated_time = 0

problems = []

while len(problems) <= 1:
  problems = [randint(1, n + 1) for n in range(1, randint(1, 9) + 1)]

# We expect 7 seconds per problem. But we expect a minimum of
# sqrt(number of problems) and a maximum of number of problems.

operations = ["+", "-", "*", "/", "%"]

def randomize_lists():
  """
  Randomizes all lists available in this script.
  Leverages random's shuffle.
  """

  shuffle(problems)
  

def is_number(s):
  """
  Checks if the given string is a number.
  """

  try:
	float(s)
	return True
  except ValueError:
	return False


def print_welcome():
  """Prints the welcome message for the start of the game."""

  print """
  There is a fire igniting in MIT. A metaphorical fire.\n
  Fermat is scheduled to give the prove to his enigma. Members of
  the mathematical community are encouraging you to go.\n\n
  You are one commute away from getting to MIT."""


def ask_questions(p = []):
  """
  Generates equations for the player to solve
  based on the randomly generated numbers.

  p is the problem array.

  Returns the number of questions asked.
  """

  number_of_questions_asked = 0
  correct_answers = 0
  minimum_questions_asked = sqrt(len(p))

  while len(p) > 1 or correct_answers < minimum_questions_asked):
	# grab two random numbers.
	first_number = choice(p)
	second_number = choice(p)

	# grab an operation randomly
	operation = choice(operations)

	print "%s %s %s = ?" % (first_number, operation, second_number)
	number_of_questions_asked += 1
	
	answer = 0

	if operation == "+":
	  answer = operator.add(first_number, second_number)
	elif operation == "-":
	  answer = operator.sub(first_number, second_number)
	elif operation == "*":
	  answer = operator.mul(first_number, second_number)
	elif operation == "/":
	  answer = operator.div(first_number, second_number)
	else:
	  answer = operator.mod(first_number, second_number)
	
	player_answer = raw_input("> ")

	while not is_number(player_answer):
	  print "That is not a number! Please enter a valid number."
	  player_answer = raw_input("> ")

	if int(player_answer) == answer:
	  correct_answers += 1
	
	p.remove(first_number)

	# If there are two numbers which are equal in the list,
	# only remove one of them
	if first_number != second_number:
	  p.remove(second_number)
  
  return number_of_questions_asked

def play_game():
  """
  Starts the whole game. The game should perform any calls here.
  """

  # initialize the timer
  start_time = time.time()
  
  print_welcome()
  randomize_lists()
  estimated_time = ask_questions(problems) * 7 # Num of questions asked * 7 seconds
  actual_time = time.time() - start_time

  # print "Time taken: %r" % actual_time
  # print "Est. time: %r" % estimated_time

  if actual_time > estimated_time:
	print "You missed the lecture. You're lack of knowledge turns you into a slug."
  else:
	print "You made the lecture! Share the knowledge on Wikipedia."


# Game on!
play_game()
