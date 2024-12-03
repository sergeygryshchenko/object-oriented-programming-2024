import tkinter as tk
from tkinter import filedialog, messagebox
from state_graph import TStateGraph
from canvas import TCanvasContent
import math

class TInterfaceWindow:
    def __init__(self, root):
        self.root = root
        self.graph = TStateGraph()
        self.content = TCanvasContent(self.graph)

        self.root.title("State Graph")
        self.root.geometry("600x600")

        self.canvas = tk.Canvas(root, width=500, height=500, bg="white")
        self.canvas.place(x=50, y=100)

        self.file_button = tk.Button(root, text="Choose Graph", command=self.browse)
        self.file_button.place(x=5, y=5)

        self.vertex_entry_label = tk.Label(root, text="Active Vertex:")
        self.vertex_entry_label.place(x=5, y=35)

        self.vertex_entry = tk.Entry(root)
        self.vertex_entry.place(x=90, y=35)
        self.vertex_entry.bind("<Return>", self.update_active_vertex)

        self.event_label = tk.Label(root, text="Events:")
        self.event_label.place(x=5, y=65)

        self.event_buttons_frame = tk.Frame(root)
        self.event_buttons_frame.place(x=60, y=65)

    def browse(self):
        file_path = filedialog.askopenfilename(initialdir="../Graph files", title="Select a Graph File", filetypes=(("Graph files", "*.txt"), ("all files", "*.*")))
        if file_path:
            try:
                self.graph.file_init(file_path)
                self.vertex_entry.delete(0, tk.END)
                self.vertex_entry.insert(0, "1")
                self.update_event_buttons()
                self.update_canvas()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def update_active_vertex(self, event=None):
        try:
            vertex = int(self.vertex_entry.get()) - 1
            self.graph.set_active_vertex(vertex)
            self.update_canvas()
        except ValueError:
            messagebox.showerror("Error", "Invalid vertex number")

    def update_canvas(self):
        self.content.draw_content(self.canvas)

    def update_event_buttons(self):
        for widget in self.event_buttons_frame.winfo_children():
            widget.destroy()

        for i in range(self.graph.events_count()):
            button = tk.Button(self.event_buttons_frame, text=f"Event {i+1}", command=lambda i=i: self.process_event(i))
            button.pack(side=tk.LEFT)

    def process_event(self, event):
        self.graph.process_event(event)
        self.vertex_entry.delete(0, tk.END)
        self.vertex_entry.insert(0, str(self.graph.active_vertex + 1))
        self.update_canvas()