from __future__ import annotations
import math


matrix = [
    [1, 2],
    [3, 4]
]

def exp(x, terms=25):
    try:     
        if isinstance(x, float) or isinstance(x, int):
            output = 0
            for i in range(0, terms, 1):
                output += ((x**i)/(math.factorial(i)))
            return output
        elif isinstance(x, square_matrix):
            print('Here!')
            output_matrix = square_matrix([[0 for d in range(0, x.matrix_len, 1)] for i in range(0, x.matrix_len, 1)])
            for i in range(0, terms, 1):
                output_matrix += ((x**i)/(math.factorial(i)))
            return output_matrix

    except:
        print(f"Equation Failed: Try checking type")

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
        if other.matrix_len != self.matrix_len:
            print(f"__mul__ Matrice length must be the same {other.matrix_len} {self.matrix_len}")
            pass
        
        output_matrix = [[0 for d in range(0, self.matrix_len, 1)] for i in range(0, self.matrix_len, 1)]

        for i in range(0, self.matrix_len, 1):
            for j in range(0, self.matrix_len, 1):
                output_matrix[i][j] += self.matrix[i][j] + other.matrix[i][j]

        return square_matrix(output_matrix)


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

        return square_matrix(output_matrix)

    def __pow__(self,  expontent):
        copy_self = self
        for i in range(1, expontent):
            self *= copy_self

        return square_matrix(self.matrix)

    def __truediv__(self, num: int):
        output_matrix = [[0 for d in range(0, self.matrix_len, 1)] for i in range(0, self.matrix_len, 1)]
        
        for i in range(0, self.matrix_len, 1):
            for k in range(0, self.matrix_len, 1):
                output_matrix[i][k] = self.matrix[i][k] / num 

        return square_matrix(output_matrix)

    def __str__(self):
        print(f"Matrix Size: {self.matrix_len}x{self.matrix_len}")
        for i in range(0, self.matrix_len, 1):
            print(f'\t{self.matrix[i]}')
        return ""

matrix1 = square_matrix([
    [1, 2],
    [3, 4]
])
matrix2 =square_matrix([
    [5, 6],
    [7, 8]
])

# print(f"{square_matrix(matrix1 + matrix2)}")
# print(matrix1)

print(exp(matrix1))

# print(matrix1 ** 4)
