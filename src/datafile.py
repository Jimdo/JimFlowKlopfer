class Datafile(object):
    def __init__(self, name, ctime):
        self.name = name
        self.ctime = ctime

    def __eq__(self, other):
        if isinstance(other, Datafile):
            return self.name == other.name and self.ctime == other.ctime
