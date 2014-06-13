class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print ("Initializing %s" %(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """I am dying."""
        print ("%s is being destroyed!" %(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print ("%s was the last one." %(self.name))
        else:
            print ("There are still %d robots working." %(Robot.population))

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print ("Greetings, my masters call me %s." %(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print ("We have %d robots." %(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print ("\nRobots can do some work here.\n")

print ("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
