class Present:
    def __init__(self):
        self.contents = None

    def wrap(self, contents):
        if self.contents is not None:
            # self.contents = contents <-- incorrect placement to see if tests are checking for this
            raise Exception("A contents has already been wrapped.")
        self.contents = contents


    def unwrap(self):
        if self.contents is None:
            raise Exception("No contents have been wrapped.")
        return self.contents