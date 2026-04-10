import math
from __future__ import annotations

class variable:
    def __init__(self, name: str):
        self.name = name
        self.value = 0

    def __str__(self):
        return f"{self.name} = {self.value}"

    def dict(self):
        return {self.name: self.value}


class function:
    def __init__(self, variable: variable):
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
            'pi': math.pi,
            'sin': math.sin,
            'exp': exp
        }

    def set_equations(self, equation: str):
        self.equation = equation
        print(f"Set function equation to: {self.equation}")

    def calculate(self, domain):
        # Clear previous results
        self.domain = []
        self.range = []

        if isinstance(domain, list):
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
            self.domain = [domain]
            self.range = [self.variable.value]

        else:
            print(f"Domain must be array [x, y] or float/int")

def exp(x, terms=25):
    try:     
        if isinstance(x, float) or isinstance(x, int):
            output = 0
            for i in range(0, terms, 1):
                output += ((x**i)/(math.factorial(i)))
            return output
        elif isinstance(x, square_matrix):
            pass

    except:
        print(f"Equation Failed: Try checking type")

'''
Must be square matrix 
#of Columns == #of Rows

matrix = [
    [1, 2],
    [3, 4]
]
'''

class square_matrix:
    def __init__(self, matrix):
        for column in matrix:
            if len(column) != len(matrix):
                print(f"Not a square Matrix")
                del self
                break
        self.matrix = matrix
        self.matrix_len = len(matrix)

    def __add__(self, other: square_matrix):
        pass

    def __mul__(self, other: square_matrix):
        # Check for same shape
        if other.matrix_len != self.matrix_len:
            print(f"__mul__ Matrice length must be the same {other.matrix_len} {self.matrix_len}")
            pass    

        output_matrix = [[0 for d in range(0, self.matrix_len, 1)] for i in range(0, self.matrix_len, 1)]

        for i in range(0, self.matrix_len, 1):
            for j in range(0, len(other.matrix[0]), 1):
                for k in range(0,  other.matrix_len, 1):
                    output_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return output_matrix

