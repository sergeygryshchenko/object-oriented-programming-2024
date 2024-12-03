import tkinter as tk
from tkinter import ttk
from math import sqrt

class HexNumber:
    def __init__(self, value="0"):
        self.value = value.upper()

    def __str__(self):
        return self.value

    def to_decimal(self):
        if '.' in self.value:
            whole, frac = self.value.split('.')
            whole = int(whole, 16)
            frac = sum(int(digit, 16) * 16**-(i+1) for i, digit in enumerate(frac))
            return whole + frac
        else:
            return int(self.value, 16)

    def from_decimal(self, decimal_value):
        if isinstance(decimal_value, float):
            whole_part = int(decimal_value)
            frac_part = decimal_value - whole_part
            hex_frac = []
            while frac_part and len(hex_frac) < 10:  
                frac_part *= 16
                digit = int(frac_part)
                hex_frac.append(hex(digit)[2:].upper())
                frac_part -= digit
            if hex_frac:
                self.value = f"{hex(whole_part)[2:].upper()}.{''.join(hex_frac)}"
            else:
                self.value = f"{hex(whole_part)[2:].upper()}"
        else:
            self.value = hex(decimal_value)[2:].upper()
        return self

    def add(self, other):
        result = self.to_decimal() + other.to_decimal()
        return HexNumber().from_decimal(result)

    def subtract(self, other):
        result = self.to_decimal() - other.to_decimal()
        return HexNumber().from_decimal(result)

    def multiply(self, other):
        result = self.to_decimal() * other.to_decimal()
        return HexNumber().from_decimal(result)

    def divide(self, other):
        result = self.to_decimal() / other.to_decimal()
        return HexNumber().from_decimal(result)


class DisplayWindow:
    def __init__(self, master):
        self.master = master
        self.entry = ttk.Entry(self.master, width=50)
        self.entry.grid(row=0, column=0, columnspan=4, sticky="we", padx=1)

    def get(self):
        return self.entry.get()

    def set(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)

    def clear(self):
        self.entry.delete(0, tk.END)

    def delete(self):
        current_entry = self.entry.get()
        new_entry = current_entry[:-1]
        self.entry.delete(0, tk.END)
        self.entry.insert(0, new_entry)


class ControlWindow:
    def __init__(self, master, display):
        self.master = master
        self.display = display
        self.create_buttons()

    def create_buttons(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("actions.TButton", foreground="black", background ="silver")
        self.button_0 = ttk.Button(self.master, text="0", command=lambda: self.button_click("0"))
        self.button_1 = ttk.Button(self.master, text="1", command=lambda: self.button_click("1"))
        self.button_2 = ttk.Button(self.master, text="2", command=lambda: self.button_click("2"))
        self.button_3 = ttk.Button(self.master, text="3", command=lambda: self.button_click("3"))
        self.button_4 = ttk.Button(self.master, text="4", command=lambda: self.button_click("4"))
        self.button_5 = ttk.Button(self.master, text="5", command=lambda: self.button_click("5"))
        self.button_6 = ttk.Button(self.master, text="6", command=lambda: self.button_click("6"))
        self.button_7 = ttk.Button(self.master, text="7", command=lambda: self.button_click("7"))
        self.button_8 = ttk.Button(self.master, text="8", command=lambda: self.button_click("8"))
        self.button_9 = ttk.Button(self.master, text="9", command=lambda: self.button_click("9"))
        self.button_A = ttk.Button(self.master, text="A", command=lambda: self.button_click("A"))
        self.button_B = ttk.Button(self.master, text="B", command=lambda: self.button_click("B"))
        self.button_C = ttk.Button(self.master, text="C", command=lambda: self.button_click("C"))
        self.button_D = ttk.Button(self.master, text="D", command=lambda: self.button_click("D"))
        self.button_E = ttk.Button(self.master, text="E", command=lambda: self.button_click("E"))
        self.button_F = ttk.Button(self.master, text="F", command=lambda: self.button_click("F"))
        self.button_purge = ttk.Button(self.master, text="P", style="actions.TButton", command=self.display.clear)
        self.button_add = ttk.Button(self.master, text="+", style="actions.TButton", command=lambda: self.button_click("+"))
        self.button_equal = ttk.Button(self.master, text="=", style="actions.TButton", command=self.button_equal)
        self.button_subtract = ttk.Button(self.master, text="-", style="actions.TButton", command=lambda: self.button_click("-"))
        self.button_multiply = ttk.Button(self.master, text="*", style="actions.TButton", command=lambda: self.button_click("*"))
        self.button_divide = ttk.Button(self.master, text="/", style="actions.TButton", command=lambda: self.button_click("/"))
        self.button_to_decimal = ttk.Button(self.master, text="DEC", style="actions.TButton", command=self.button_to_decimal)
        self.button_to_hex = ttk.Button(self.master, text="HEX", style="actions.TButton", command=self.button_to_hex)
        self.button_dot = ttk.Button(self.master, text=".", style="actions.TButton", command=lambda: self.button_click("."))
        self.button_delete = ttk.Button(self.master, text="DEL", style="actions.TButton", command=self.display.delete)

        self.button_0.grid(row=3, column=0)
        self.button_1.grid(row=3, column=1)
        self.button_2.grid(row=3, column=2)
        self.button_3.grid(row=3, column=3)
        self.button_4.grid(row=4, column=0)

        self.button_5.grid(row=4, column=1)
        self.button_6.grid(row=4, column=2)
        self.button_7.grid(row=4, column=3)
        self.button_8.grid(row=5, column=0)
        self.button_9.grid(row=5, column=1)

        self.button_A.grid(row=5, column=2)
        self.button_B.grid(row=5, column=3)
        self.button_C.grid(row=6, column=0)
        self.button_D.grid(row=6, column=1)
        self.button_E.grid(row=6, column=2)

        self.button_F.grid(row=6, column=3)
        self.button_purge.grid(row=0, column=4)
        self.button_add.grid(row=2, column=2)
        self.button_equal.grid(row=6, column=4) 
        self.button_subtract.grid(row=2, column=3)

        self.button_multiply.grid(row=4, column=4)
        self.button_divide.grid(row=5, column=4)
        self.button_to_decimal.grid(row=2, column=4)
        self.button_to_hex.grid(row=3, column=4)
        self.button_dot.grid(row=2, column=0)
        self.button_delete.grid(row=2, column=1)

    def button_click(self, number):
        current = self.display.get()
        self.display.set(current + number)

    def button_add(self):
        first_number = self.display.get()
        self.f_num = HexNumber(first_number)
        self.display.set(first_number + "+")

    def button_equal(self):
        input_str = self.display.get()
        if '+' in input_str:
            first_number_str, second_number_str = input_str.split('+')
            operator = "+"
        elif '-' in input_str:
            first_number_str, second_number_str = input_str.split('-')
            operator = "-"
        elif '*' in input_str:
            first_number_str, second_number_str = input_str.split('*')
            operator = "*"
        elif '/' in input_str:
            first_number_str, second_number_str = input_str.split('/')
            operator = "/"
        else:
            self.display.set("Error")
            return
        first_number = HexNumber(first_number_str.strip())
        second_number = HexNumber(second_number_str.strip())
        if operator == "+":
            result = first_number.add(second_number)
        elif operator == "-":
            result = first_number.subtract(second_number)
        elif operator == "*":
            result = first_number.multiply(second_number)
        elif operator == "/":
            result = first_number.divide(second_number)
        else:
            result = HexNumber()
        self.display.set(str(result))

    def button_subtract(self):
        first_number = self.display.get()
        self.f_num = HexNumber(first_number)
        self.display.set(first_number + "-")

    def button_multiply(self):
        first_number = self.display.get()
        self.f_num = HexNumber(first_number)
        self.display.set(first_number + "*")

    def button_divide(self):
        first_number = self.display.get()
        self.f_num = HexNumber(first_number)
        self.display.set(first_number + "/")

    

    def button_to_decimal(self):
        hex_value = HexNumber(self.display.get())
        decimal_value = hex_value.to_decimal()
        self.display.set(str(decimal_value))
        
    def button_to_hex(self):
        decimal_value = float(self.display.get())
        hex_value = HexNumber()
        hex_value.from_decimal(decimal_value)
        self.display.set(hex_value.value)


class OptionsWindow:
    def __init__(self, master, display, memory):
        self.master = master
        self.display = display
        self.memory = memory
        self.create_buttons()

    def create_buttons(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("actions.TButton", foreground="black", background ="silver")
        self.button_memory_add = ttk.Button(self.master, text="M+", style="actions.TButton", command=self.button_memory_add)
        self.button_memory_1 = ttk.Button(self.master, text="M1", style="actions.TButton", command=lambda: self.button_memory_recall(0))
        self.button_memory_2 = ttk.Button(self.master, text="M2", style="actions.TButton", command=lambda: self.button_memory_recall(1))
        self.button_memory_3 = ttk.Button(self.master, text="M3", style="actions.TButton", command=lambda: self.button_memory_recall(2))
        self.button_memory_4 = ttk.Button(self.master, text="M4", style="actions.TButton", command=lambda: self.button_memory_recall(3))

        self.button_memory_add.grid(row=1, column=4)
        self.button_memory_1.grid(row=1, column=0)
        self.button_memory_2.grid(row=1, column=1)
        self.button_memory_3.grid(row=1, column=2)
        self.button_memory_4.grid(row=1, column=3)

    def button_memory_add(self):
        value = HexNumber(self.display.get())
        self.memory.insert(0, value)
        self.memory = self.memory[:4]

    def button_memory_recall(self, index):
        if 0 <= index < len(self.memory):
            current = self.display.get()
            self.display.set(current + str(self.memory[index]))
       

class HexCalculator:
    def __init__(self,master):
        self.master = master
        self.master.title("Шестнадцатеричный калькулятор")
        self.master.geometry("500x300")
        self.memory = [HexNumber() for _ in range(4)]

        self.display_window = DisplayWindow(self.master)
        self.control_window = ControlWindow(self.master, self.display_window)
        self.options_window = OptionsWindow(self.master, self.display_window,self.memory)


if __name__ == '__main__':
    root = tk.Tk()
    calc = HexCalculator(root)
    root.mainloop()