import math
import operator
import time
from random import randint, shuffle, choice

class Obstacle(object):
    """
    An Obstacle contains a set of questions
    which are asked to the user.

    """

    def generate_problems(self):
        """Generates a maximum of 10 random digits."""
        
        return [randint(1, n+1) for n in (
            range(1, randint(1, 9) + 1))]

    def shuffle_problems(self):
        """Randomizes all problems leveraging random's shuffle."""
        
        shuffle(self.problems)

    def increase_difficulty(self, difficulty_level = 9):
        """
        Increases the difficulty by multiplying the problems 
        by a multiple. The default difficulty is the most
        difficult.

        """

        self.problems *= randint(2, difficulty_level)

    def __init__(self, problems = []):
        self.problems = self.generate_problems() if not problems else problems
        self.operations = ["+", "-", "*", "/", "%"]

    def ask_questions(self):
        """
        Generates equations for the player to solve based on the randomly 
        generated numbers. This returns the number of questions asked,
        along with the time it took to ask the necessary questions.

        """
        
        number_of_questions_asked = 0
        correct_answers = 0
        minimum_questions_asked = math.sqrt(len(self.problems))

        start_time = time.time()

        while (len(self.problems) > 1 or 
            correct_answers < minimum_questions_asked):
            # Grab two random numbers.
            a = choice(self.problems) # Leveraging random lib
            b = choice(self.problems)
            operation = choice(self.operations)

            print "%s %s %s = ?" % (a, operation, b)

            number_of_questions_asked += 1

            answer = 0

            if operation == "+":
                answer = operator.add(a, b)
            elif operation == "-":
                answer = operator.sub(a, b)
            elif operation == "*":
                answer = operator.mul(a, b)
            elif operation == "/":
                answer = operator.div(a, b)
            else:
                answer = operator.mod(a, b)

            player_answer = raw_input("> ")

            while not is_number(player_answer):
                print "%s is not a number! Please enter a valid number." % (
                    player_answer)
                player_answer = raw_input("> ")

            if player_answer == str(answer):
                correct_answers += 1

            self.problems.remove(a)

            # If there are two numbers which are equal in problems,
            # only remove one of them.
            if a != b:
                self.problems.remove(b)

        return (number_of_questions_asked, time.time() - start_time)


def is_number(number_string):
    """
    Checks if given string is a number. This is preferred over built in
    string method isdigit() as it considers negative numbers.

    """

    try:
        float(number_string)
        return True
    except  ValueError:
        return False