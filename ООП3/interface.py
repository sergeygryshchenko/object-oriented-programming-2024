import tkinter as tk
from tkinter import messagebox
from rational import TRational
from matrix import Matrix

class TInterface:
    def __init__(self, window):
        self.window = window
        self.window.title("Squere matrix operations")
        self.window.geometry("500x400")
        self.window.resizable(width = False, height = False)

        self.matrix = Matrix()
        self.create_widgets()

    def create_widgets(self):
               # Frame for menu
        self.menu_frame = tk.Frame(self.window)
        self.menu_frame.grid(row=0, column=0, padx=50, pady=10)

        self.menu_label = tk.Label(self.menu_frame, text='Menu:')
        self.menu_label.pack()

        self.input_button = tk.Button(self.menu_frame, text='Input matrix', command=self.input_Matrix, fg="green")
        self.input_button.pack()

        self.determinant_button = tk.Button(self.menu_frame, text='Find determinant', command=self.matrix_Determinant, fg="green")
        self.determinant_button.pack()

        self.transpose_button = tk.Button(self.menu_frame, text='Transpose matrix', command=self.transpose_Matrix, fg="green")
        self.transpose_button.pack()

        self.rank_button = tk.Button(self.menu_frame, text='Find rank of matrix', command=self.compute_Rank, fg="green")
        self.rank_button.pack()

        self.print_button = tk.Button(self.menu_frame, text='Print current matrix', command=self.print_Matrix, fg="green")
        self.print_button.pack()

        self.exit_button = tk.Button(self.menu_frame, text=' Exit', command=self.exit_program, fg="green")
        self.exit_button.pack()

                 # Frame for output
        self.output_frame = tk.Frame(self.window)
        self.output_frame.grid(row=1, column=0, padx=10, pady=10)


    def transpose_Matrix(self):
        for widget in self.output_frame.winfo_children():
            widget.destroy()
        transposed = self.matrix.transposeMatrix()
        for i, row in enumerate(transposed):
            label = tk.Label(self.output_frame, text=' '.join(map(str, row)))
            label.grid(row=i, column=0)

    def compute_Rank(self):
        for widget in self.output_frame.winfo_children():
            widget.destroy()
        rank = self.matrix.computeRank(self.matrix.matrix)
        self.rank_label=tk.Label(self.output_frame, text=f"Rank of the matrix is {rank}.")
        self.rank_label.grid(row=0, column=0, pady=10)

    def matrix_Determinant(self):
        for widget in self.output_frame.winfo_children():
            widget.destroy()
        determinant = self.matrix.matrixDeterminant(self.matrix.matrix)
        self.rank_label=tk.Label(self.output_frame, text=f"Determinant of the matrix is {determinant}.")
        self.rank_label.grid(row=0, column=0, pady=10)

    def input_Matrix(self):
        for widget in self.output_frame.winfo_children():
            widget.destroy()
        self.matrix.inputMatrix_widgets_gui(self.output_frame)

    def print_Matrix(self):
        for widget in self.output_frame.winfo_children():
            widget.destroy()
        self.matrix.printMatrix_widgets_gui(self.output_frame)

    def exit_program(self):
        self.window.destroy()