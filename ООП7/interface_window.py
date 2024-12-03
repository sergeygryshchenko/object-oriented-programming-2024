import tkinter as tk
from tkinter import filedialog, messagebox
from directed_graph import TDirectedGraph
from canvas import TCanvasContent
import math


class TInterfaceWindow:
    def __init__(self, root):
        self.root = root
        self.graph = TDirectedGraph()
        self.content = TCanvasContent(self.graph)

        self.root.title("Graph")
        self.root.geometry("500x500")

        self.canvas = tk.Canvas(root, width=500, height=500, bg="white")
        self.canvas.pack()

        self.file_button = tk.Button(root, text="Choose Graph", command=self.browse)
        self.file_button.place(x=5, y=5)

    def browse(self):
        file_path = filedialog.askopenfilename(initialdir="../Graph files", title="Select a Graph File", filetypes=(("Graph files", "*.txt"), ("all files", "*.*")))
        if file_path:
            try:
                self.graph.file_init(file_path)
                self.clear_canvas()
                self.content.draw_content(self.canvas, self.canvas, "white")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def clear_canvas(self):
        self.canvas.delete("all")