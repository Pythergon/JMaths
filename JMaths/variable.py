
class variable:
    def __init__(self, name):
        self.name = name
        self.value = 0

    def __str__(self):
        return f"Name: {self.name}"

    def dict(self):
        return {self.name: self.value}
