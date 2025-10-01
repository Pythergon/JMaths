
class function:
    def __init__(self, variable):
        self.variable = variable
        self.equation = None
        self.delta = .01
        self.range = []
        self.domain = []

    def set_equations(self, equation):
        self.equation = equation
        print(f"Set function equation to: {self.equation}")


    def calculate(self, domain):
        # For domain insert a list EX: [-1, 1]
        self.variable.value = domain[0]

        if isinstance(self.equation, str):
            while self.variable.value <= domain[1]:
                self.domain.append(self.variable.value)
                self.range.append(eval(self.equation, {'x': self.variable.value}))
                self.variable.value += self.delta

        # return f"{self.variable.value}"
