class Map(object):
    """
    A Map class determines the different types
    of stages which exist in a game.

    """

    self.stages = {
            "home": Home(),
            "train": TrainStation(),
            "bus": BusStation(),
            "run": RunToDestination()
            }

    def __init__(self, start_stage):
        self.start_stage = start_stage

    def next_stage(self, stage):
        return self.stages.get(stage)

    def opening_stage(self):
        return self.next_stage(self.start_stage)
