import tkinter as tk
from tkinter import messagebox
from interface import TInterface  
from communicator import TCommunicator  

class TApplication:
    def __init__(self):
        self.communicator = TCommunicator("localhost", 10000, "localhost", 10001) 
        self.interface  = tk.Tk()
        TInterface(self.interface, self )
        self.interface .mainloop()
        
   
    def to_communicator(self, msg):
        self.communicator.send(msg)

    def from_communicator(self, msg):
        return self.communicator.receive()