import tkinter as tk
from tkinter import simpledialog, messagebox
from rational import TRational

number = TRational

class Matrix:
    dimension: int = 3                   
    matrix: list[list[number]] = [[number(), number(), number()],
                                   [number(), number(), number()],
                                   [number(), number(), number()]]

    def inputMatrix(self):
        self.dimension = int(input("Enter the dimension of the matrix: "))
        self.matrix = []

        print("Enter the matrix elements ")
        for i in range(self.dimension):
            row = []
            for j in range(self.dimension):
                el_input = input(f"Enter element {i}{j}: ")
                elements = el_input.split() 
                if len(elements) == 0:
                    real=0
                    imag=None
                if len(elements) == 1:
                    real = int(elements[0])
                    imag = None
                if len(elements) == 2:
                    real = int(elements[0])
                    imag = int(elements[1])
                row.append(number(real, imag))
            self.matrix.append(row)
        return self.matrix


    @staticmethod
    def printMatrix(matrix):
        for row in matrix:
            print(" ".join(map(str, row)))


    def transposeMatrix(self):
        dim = len(self.matrix)
        transposed = []

        for i in range(dim):
            transposed.append([self.matrix[j][i] for j in range(dim)])

        self.printMatrix(transposed)
        return transposed


    @staticmethod
    def computeRank(matrix) -> int:
        dim = len(matrix) 
        rank = dim
        copy_of_matrix = [[1] * dim for _ in range(dim)]
        for i in range(dim):
            for j in range(dim):
                copy_of_matrix[i][j] = matrix[i][j]
        row_positions = 0
        for i in range(rank):
            if copy_of_matrix[row_positions][i] != 0:
                for j in range(dim):
                    if j != row_positions and copy_of_matrix[j][i] != 0:
                        scalar = copy_of_matrix[j][i] / copy_of_matrix[row_positions][i]
                        for k in range(rank):
                            copy_of_matrix[j][k] -=  copy_of_matrix[row_positions][k] * scalar 
                row_positions += 1

        return row_positions


    def matrixDeterminant(self, matrix) -> number:
        n = len(matrix)

        # для матрицы 2x2
        if n == 2:
            det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            return det

        det = number(0)
        for i in range(n):
            sign = (-1) ** i
            sub_matrix = [row[:i] + row[i + 1:] for row in matrix[1:]]
            det +=  matrix[0][i] * sign  * self.matrixDeterminant(sub_matrix)
        return det


    def  inputMatrix_widgets_gui(self,window):
        self.dimension = simpledialog.askinteger('Entering the dimension', 'Enter the dimension of the square matrix: ')
        if self.dimension:
            self.matrix = []
            for i in range(self.dimension):
                row = []
                for j in range(self.dimension):
                    valid_input = False
                    while not valid_input:
                        entry = simpledialog.askstring('Entering the matrix',
                                            f'Enter the element with the number ({i + 1},{j + 1}) in the format a/b: ')
                        try:
                            numerator, denominator = map(int, entry.split('/'))
                            row.append(TRational(numerator, denominator))
                            valid_input = True
                        except ValueError:
                            messagebox.showerror('Error', 'Incorrect input. Enter the element in the format: a/b')
                self.matrix.append(row)



    def printMatrix_widgets_gui(self,window):
        for i, row in enumerate(self.matrix):
            label = tk.Label(window, text=' '.join(map(str, row)))
            label.grid(row=i, column=0,padx=5, pady=5)
