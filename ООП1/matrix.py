class Matrix:
    rows: int = 3
    cols: int = 3
    matrix: list[list] = [[1, 2, 3],  #значение матрицы по умолчанию
                          [4, 5, 6],
                          [7, 8, 9]]

    def inputMatrix(self):
        self.rows = int(input("Enter the number of rows: "))
        self.cols = int(input("Enter the number of сolumns: "))
        self.matrix = []

        print("Enter the matrix elements:")
        for i in range(self.rows):
            row = list(map(float, input().split()))
            self.matrix.append(row)
        return self.matrix


    @staticmethod
    def printMatrix(matrix):
        for row in matrix:
            print(" ".join(map(str, row)))


    def transposeMatrix(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        transposed = []

        for i in range(cols):
            transposed.append([self.matrix[j][i] for j in range(rows)])

        self.printMatrix(transposed)
        return transposed


    @staticmethod
    def computeRank(matrix) -> int:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        rank = min(num_rows, num_cols)

        row_positions = 0
        for i in range(rank):
            if matrix[row_positions][i] != 0:
                for j in range(num_rows):
                    if j != row_positions and matrix[j][i] != 0:
                        scalar = matrix[j][i] / matrix[row_positions][i]
                        for k in range(rank):
                            matrix[j][k] -= scalar * matrix[row_positions][k]
                row_positions += 1

        return row_positions


    def matrixDeterminant(self, matrix):
        n = len(matrix)

        # для матрицы 2x2
        if n == 2:
            det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            return det

        det = 0
        for i in range(n):
            sign = (-1) ** i
            sub_matrix = [row[:i] + row[i + 1:] for row in matrix[1:]]
            det += sign * matrix[0][i] * self.matrixDeterminant(sub_matrix)
        return det
