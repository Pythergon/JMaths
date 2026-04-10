from __future__ import annotations


matrix = [
    [1, 2],
    [3, 4]
]

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
    
matrix1 = square_matrix([
    [1, 2],
    [3, 4]
])
matrix2 =square_matrix([
    [5, 6],
    [7, 8]
])

print(f"{matrix1 * matrix2}")
