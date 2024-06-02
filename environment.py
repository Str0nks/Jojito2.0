import sys

class Environment:
    testing = False

    def __init__(self):
        print("Initialising environment")
        for arg in sys.argv:
            if arg == "--testing" or arg == "-t":
                self.testing = True
            elif arg == "--help" or arg == "-h":
                # top line
                print("Usage:\n\tL9Bot.py [options]\n")

                # help
                print("OPTIONS\n\t-h, --help\t\tshow a list of command-line options")

                # testing
                print("\t-t, --testing\t\trun in a testing environment")

                exit(0)
