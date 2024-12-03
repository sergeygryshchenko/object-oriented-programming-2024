import tkinter as tk
from tkinter import messagebox,simpledialog
from common import Messages, Modes


class TInterface:
    def __init__(self, window, app):
            self.window = window
            self.application = app
            self.window.title("Squere matrix operations")
            self.window.geometry("500x400")
            self.window.resizable(width = False, height = False)
            self.create_widgets()


    def create_widgets(self):
               # Frame for modes
        self.radio_frame = tk.Frame(self.window)
        self.radio_frame.grid(row=0, column=0, padx=10, pady=10)

        self.radio_var = tk.StringVar()
        self.radio_button1 = tk.Radiobutton(self.radio_frame, text="float", variable=self.radio_var, value="f_mode")
        self.radio_button1.pack(side='left', padx=5)

        self.radio_button2 = tk.Radiobutton(self.radio_frame, text="complex", variable=self.radio_var, value="c_mode")
        self.radio_button2.pack(side='left', padx=5)

        self.radio_button3 = tk.Radiobutton(self.radio_frame, text="rational", variable=self.radio_var, value="r_mode")
        self.radio_button3.pack(side='left', padx=5)

               # Frame for menu
        self.menu_frame = tk.Frame(self.window)
        self.menu_frame.grid(row=1, column=0, padx=50, pady=10)

        self.menu_label = tk.Label(self.menu_frame, text='Menu:')
        self.menu_label.pack()

        self.input_button = tk.Button(self.menu_frame, text='Input matrix', command=lambda:self.request('INPUT_MATRIX'), fg="green")
        self.input_button.pack()

        self.determinant_button = tk.Button(self.menu_frame, text='Find determinant', command=lambda:self.request('FIND_DETERMINANT'), fg="green")
        self.determinant_button.pack()

        self.transpose_button = tk.Button(self.menu_frame, text='Transpose matrix', command=lambda:self.request('TRANSPOSE_MATRIX'), fg="green")
        self.transpose_button.pack()

        self.rank_button = tk.Button(self.menu_frame, text='Find rank of matrix', command=lambda:self.request('FIND_RANK_OF_MATRIX'), fg="green")
        self.rank_button.pack()

        self.print_button = tk.Button(self.menu_frame, text='Print current matrix', command=lambda:self.request('PRINT_CURRENT_MATRIX'), fg="green")
        self.print_button.pack()

        self.exit_button = tk.Button(self.menu_frame, text=' Exit', command=lambda:self.request('EXIT'), fg="green")
        self.exit_button.pack()

                 # Frame for output
        self.output_frame = tk.Frame(self.window)
        self.output_frame.grid(row=2, column=0, padx=10, pady=10)


    def compute_Rank(self,ans):
        for widget in self.output_frame.winfo_children():
            widget.destroy()
        rank = ans
        self.rank_label=tk.Label(self.output_frame, text=f"Rank of the matrix is {rank}.")
        self.rank_label.grid(row=0, column=0, pady=10)

    def matrix_Determinant(self,ans):
        for widget in self.output_frame.winfo_children():
            widget.destroy()
        determinant = ans
        self.rank_label=tk.Label(self.output_frame, text=f"Determinant of the matrix is {determinant}.")
        self.rank_label.grid(row=0, column=0, pady=10)


    def print_Matrix(self,ans):
        for widget in self.output_frame.winfo_children():
            widget.destroy()
        self.rank_label=tk.Label(self.output_frame, text=ans)
        self.rank_label.grid(row=0, column=0, pady=10)

    def exit_program(self):
        self.window.destroy()
        

    def input_Matrix(self,dimension):
        matrix_elements = []  
        selected_value = self.radio_var.get()
        for i in range(dimension):
            row_elements = []  
            for j in range(dimension):
                if selected_value == "f_mode":
                    element_str = simpledialog.askstring('Entering the matrix',
                                                     f'Enter the element with the number ({i + 1},{j + 1}) in the format a.b: ')
                if selected_value == "c_mode":
                    element_str = simpledialog.askstring('Entering the matrix',
                                                     f'Enter the element with the number ({i + 1},{j + 1}) in the format a_b: ')
                if selected_value == "r_mode":
                    element_str = simpledialog.askstring('Entering the matrix',
                                                     f'Enter the element with the number ({i + 1},{j + 1}) in the format a/b: ')
                row_elements.append(element_str)  
            row_str = ' '.join(row_elements) 
            matrix_elements.append(row_str)  

        matrix_str = '\n'.join(matrix_elements)  
        return matrix_str

    def request(self,com):
        selected_value = self.radio_var.get()
        if selected_value == "f_mode":
            msg = str(Modes['F_MODE'].value) + " " +  str(Messages[com].value)
            split_msg = msg.split()
            mode = split_msg[0]
            action = split_msg[1]
            self.application.to_communicator(msg)
            ans=self.application.communicator.receive()
            if action == str(Messages.INPUT_MATRIX.value) :
                dimension = simpledialog.askinteger('Entering the dimension', 'Enter the dimension of the square matrix: ')
                self.application.to_communicator(str(dimension))
                self.application.to_communicator(self.input_Matrix(int(dimension)))
            if action == str(Messages.FIND_DETERMINANT.value):
                self.matrix_Determinant(ans)
            if action == str(Messages.TRANSPOSE_MATRIX.value) :
                self.print_Matrix(ans)
            if action == str(Messages.FIND_RANK_OF_MATRIX.value):
                self.compute_Rank(ans)
            if action == str(Messages.PRINT_CURRENT_MATRIX.value):
                self.print_Matrix(ans)
            if action == str(Messages.EXIT.value):
                self.exit_program()

        if selected_value == "c_mode":
            msg = str(Modes['C_MODE'].value) + " " + str(Messages[com].value)
            split_msg = msg.split()
            mode = split_msg[0]
            action = split_msg[1]
            self.application.to_communicator(msg)
            ans=self.application.communicator.receive()
            if action == str(Messages.INPUT_MATRIX.value) :
                dimension = simpledialog.askinteger('Entering the dimension', 'Enter the dimension of the square matrix: ')
                self.application.to_communicator(str(dimension))
                self.application.to_communicator(self.input_Matrix(int(dimension)))
            if action == str(Messages.FIND_DETERMINANT.value):
                self.matrix_Determinant(ans)
            if action == str(Messages.TRANSPOSE_MATRIX.value) :
                self.print_Matrix(ans)
            if action == str(Messages.FIND_RANK_OF_MATRIX.value):
                self.compute_Rank(ans)
            if action == str(Messages.PRINT_CURRENT_MATRIX.value):
                self.print_Matrix(ans)
            if action == str(Messages.EXIT.value):
                self.exit_program()

        if selected_value == "r_mode":
            msg = str(Modes['R_MODE'].value) + " " +  str(Messages[com].value)
            split_msg = msg.split()
            mode = split_msg[0]
            action = split_msg[1]
            self.application.to_communicator(msg)
            ans=self.application.communicator.receive()
            if action == str(Messages.INPUT_MATRIX.value) :
                dimension = simpledialog.askinteger('Entering the dimension', 'Enter the dimension of the square matrix: ')
                self.application.to_communicator(str(dimension))
                self.application.to_communicator(self.input_Matrix(int(dimension)))
            if action == str(Messages.FIND_DETERMINANT.value):
                self.matrix_Determinant(ans)
            if action == str(Messages.TRANSPOSE_MATRIX.value) :
                self.print_Matrix(ans)
            if action == str(Messages.FIND_RANK_OF_MATRIX.value):
                self.compute_Rank(ans)
            if action == str(Messages.PRINT_CURRENT_MATRIX.value):
                self.print_Matrix(ans)
            if action == str(Messages.EXIT.value):
                self.exit_program()


    