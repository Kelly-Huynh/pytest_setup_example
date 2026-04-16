class Reminder:
    def __init__(self, name):
        self.name = name
        self.task = None # <-- New code
    
    def remind_me_to(self, task):
        self.task = task

    def remind(self):
        # Look here! We want to fail if there is no reminder yet.
        if self.task is None: # <-- New code
            raise Exception("No reminder set!") # <-- New code
        return f"{self.task}, {self.name}!"
    