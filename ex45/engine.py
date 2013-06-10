import obstacle
import time
from math import sqrt
from sys import exit

AUTHOR_EMAIL = "labeledloser [at] gmail dot com."

class Engine(object):
    def __init__(self, game_map):
      self.game_map = game_map

    def play(self):
      current_stage = self.game_map.opening_stage()

      while True:
        print "\n%s\n" % ("-" * 79)
        next_stage_name = current_stage.enter()

        # if they want to stay at home, forgetabouthem!
        if next_stage_name == 'home':
            exit(1)

        current_stage = self.game_map.next_stage(next_stage_name)

class GameState(object):
    """
    Creates an object depending of a game state. There are a variety
    of different game states specified by the map.

    """

    def __init__(self):
        self.obstacles = obstacle.Obstacle()

    def enter(self):
        print "This stage is DLC. Please paypal $10 at %s" % (AUTHOR_EMAIL)
        exit(1)

    def win(self):
        print "Running past the grave of former Fine Hall, you run up"
        print "the stairs of the mathematics hall -- hopping over a few at a"
        print "time.\n Bursting open the door, you come to a halt to see"
        print "Fermat starting to talk about the importance of this theorem."
        print "You stick through the lecture and smile at the fact that"
        print "one of the world's oldest mysteries has been solved."
        exit(1)

    def lose(self):
        print "Unfortunately, you were unable to make it on time."
        print "During the lecture, Fermat felt uneasy at the lack of enthusiasm."
        print "So much so that he postponed the lecture."
        print "If his health continues to deprecate, this marvelous thereom might"
        print "go to waste -- much like your time."
        exit(1)


class Home(GameState):

  def enter(self):
    sentences = ["There is a fire igniting in MIT.",
            "Fermat is scheduled to give the proof to his enigma.",
            "Members of the mathematical community are encouraging you to go.",
            "You are one commute away from MIT."]

    for sentence in sentences:
        print sentence

    print "\nOptions: %r" % Map.stages.keys()
    route_taken = raw_input("> ")
    
    if route_taken not in Map.stages.keys():
        while route_taken not in Map.stages.keys():
            print "\n%s is not a valid option.\nOptions: %r" % (
                route_taken, Map.stages.keys())
            route_taken = raw_input("> ")

    return route_taken


class TrainStation(GameState):
  def enter(self):
    difficulty = 9

    sentences = ["The train station is filled with vagrants and suits.",
            "None of them can understand the importance of Fermat's proof.",
            "Your hands shovel into your pockets and return with just enough change for the metro.",
            "There you meet your arch-nemesis -- the math major.",
            "He begins to pick your brain with mind-numbing questions."]

    for sentence in sentences:
        print sentence

    self.obstacles.increase_difficulty(difficulty)
    questions_asked, time_taken = self.obstacles.ask_questions()
    estimated_time = questions_asked * (sqrt(difficulty) + 7) # number in seconds

    if estimated_time > time_taken:
        self.win() # they won!

    exit(1)


class BusStation(GameState):
  def enter(self):

    difficulty = 5

    sentences = ["Bus fleets move synchronously about.",
    "You spot bus number 314, loading a disabled individual.",
    "The bus itself is packed with restless people, and airplane philosophers.",
    "Luck might not be on your side since your arch-nemesis pesters you.",
    "\"Hey chump,\" he says as he begins to insult your mathematical abilities.",
    "A throw-down is in-place!"]

    for sentences in sentences:
        print sentence

    self.obstacles.increase_difficulty(difficulty)
    questions_asked, time_taken = self.obstacles.ask_questions()
    estimated_time = questions_asked * (sqrt(difficulty) + 7) # number in seconds

    if estimated_time > time_taken:
        self.win() # they won!
    else:
        self.lose()

class RunToDestination(GameState):
  def enter:
    
    difficulty = 3

    sentences = ["There are faster ways of getting there, but traffic is variable.",
    "Rather than risk accidents, you run at heart-choking rates.",
    "Along the way, you start seeing patterns.",
    "Numbers begin to float and you wonder if the elevated heart-rate is a bad sign.",
    "To keep sane, you start to ask yourself questions and answer them."]

    for sentence in sentences:
        print sentence

    self.obstacles.increase_difficulty(difficulty)
    questions_asked, time_taken = self.obstacles.ask_questions()
    estimated_time = questions_asked * (sqrt(difficulty) + 7) # number in seconds

    if estimated_time > time_taken:
        self.win()
    else:
        self.lose()


class Map(object):
    """
    A Map class determines the different types
    of stages which exist in a game.

    """

    # Each stage is mapped to a defined function, thus this piece of code
    # must be in place after the classes have been implemented.
    stages = {
            "home": Home(),
            "train": TrainStation(),
            "bus": BusStation(),
            "run": RunToDestination()
            }

    def __init__(self, start_stage):
        self.start_stage = start_stage

    def next_stage(self, stage):
        """A stage is simply the route they take."""

        return Map.stages.get(stage)

    def opening_stage(self):
        return self.next_stage(self.start_stage)


a_map = Map("home")
a_game = Engine(a_map)
a_game.play()
