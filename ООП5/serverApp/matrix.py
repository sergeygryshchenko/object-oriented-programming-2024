import tkinter as tk
from tkinter import simpledialog, messagebox
from rational import TRational

number = TRational

class TMatrix:
    def __init__(self, rows=3, cols=2,  matrix: list[list[number]] = None):
        self.rows = rows
        self.cols = cols
        if matrix is None:
            self.matrix: list[list[number]] = [[number() for _ in range(cols)] for _ in range(rows)]
        else:
            self.matrix = matrix

    def inputMatrix(self):
        self.rows = int(input("Enter the number of rows: "))
        self.cols = int(input("Enter the number of сolumns: "))
        self.matrix = []

        print("Enter the matrix elements ")
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
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
        copy_of_matrix = [[1] * num_cols for _ in range(num_rows)]
        for i in range(num_rows):
            for j in range(num_cols):
                copy_of_matrix[i][j] = matrix[i][j]
        row_positions = 0
        for i in range(rank):
            if copy_of_matrix[row_positions][i] != 0:
                for j in range(num_rows):
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
        self.rows = simpledialog.askinteger('Entering the dimension', 'Enter the number of rows of the matrix: ')
        self.cols = simpledialog.askinteger('Entering the dimension', 'Enter the number of cols of the matrix: ')

        if self.rows and self.cols:
            self.matrix = []
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
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

    def parseMatrix(self,matrix_str):
        matrix_lines = matrix_str.strip().split("\n")  
        self.matrix = []
        for line in matrix_lines:
            row_elements = line.split()  
            row = []
            for element_str in row_elements:
                numerator, denominator = map(int, element_str.split('/'))
                row.append(TRational(numerator, denominator))
            self.matrix.append(row)
        