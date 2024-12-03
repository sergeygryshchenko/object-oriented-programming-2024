from matrix import TMatrix
from rational import TRational
from complex import TComplex

class TSquareMatrix(TMatrix):
    def __init__(self, size=3, num_type=None, matrix: list[list] = None):
        super().__init__(rows=size, cols=size, num_type= num_type, matrix=matrix)


    def inputMatrix(self):
        self.rows = int(input("Enter the dimension of the matrix: "))
        self.cols = self.rows
        self.matrix = []

        print("Enter the matrix elements:")
        for i in range(self.rows):
            row = list(map(float, input().split()))
            self.matrix.append(row)
        return self.matrix

    def matrixDeterminant(self, matrix) -> 'num_type':
        n = len(matrix)
        det = self.num_type(0)
        # для матрицы 2x2
        if n == 2:
            det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            return det

        
        for i in range(n):
            sign = (-1) ** i
            sub_matrix = [row[:i] + row[i + 1:] for row in matrix[1:]]
            det = matrix[0][i] * sign  * self.matrixDeterminant(sub_matrix) +det
        return det

    