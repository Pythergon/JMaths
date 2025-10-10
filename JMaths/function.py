import math

class function:
    def __init__(self, variable):
        self.variable = variable
        self.equation = None
        self.delta = .01
        self.range = []
        self.domain = []
        self.calculation_errors = 0
        self.str_functions = {
            'x': self.variable.value,
            'sqrt': math.sqrt,
            'pow': math.pow,
            'pi': math.pi
        }

    def set_equations(self, equation):
        self.equation = equation
        print(f"Set function equation to: {self.equation}")

    def calculate(self, domain):

        if isinstance(domain, list):
            # Clear previous results
            self.domain = []
            self.range = []
            self.variable.value = domain[0]
            self.calculation_errors = 0

            if isinstance(self.equation, str):
                while self.variable.value <= domain[1]:

                    self.str_functions['x'] = self.variable.value
                    self.domain.append(self.variable.value)
                    try:
                        self.range.append(eval(self.equation, self.str_functions))
                    except Exception:
                        self.calculation_errors += 1
                    self.variable.value += self.delta

            print(f"Finished calculating with {self.calculation_errors} calculation errors")

        # If user just wants to computer 1 number
        elif isinstance(domain, int):
            self.variable.value = domain
            self.str_functions['x'] = self.variable.value

            self.variable.value = eval(self.equation, self.str_functions)


