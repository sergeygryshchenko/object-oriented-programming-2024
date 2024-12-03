from matrix import TMatrix
from rational import TRational

number = TRational

class TSquareMatrix(TMatrix):
    def __init__(self, size=3, matrix: list[list[number]] = None):
        super().__init__(rows=size, cols=size, matrix=matrix)


    def inputMatrix(self):
        self.rows = int(input("Enter the dimension of the matrix: "))
        self.cols = self.rows
        self.matrix = []

        print("Enter the matrix elements:")
        for i in range(self.rows):
            row = list(map(float, input().split()))
            self.matrix.append(row)
        return self.matrix


    