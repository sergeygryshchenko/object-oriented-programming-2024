import tkinter as tk
from tkinter import filedialog, messagebox
import math

class TCanvasContent:
    def __init__(self, graph):
        self.graph = graph

    def draw_content(self, canvas, window, color):
        count = self.graph.vertices_count()

        p_size = 20

        center_w = 0.5 * canvas.winfo_width()
        center_h = 0.5 * canvas.winfo_height()
        circle_r = min(center_w, center_h) - 2 * p_size - 50
        gap = 2.0 * math.acos(-1.0) / count

        font = ("Calibri", p_size)

        t = []
        for i in range(count):
            x = center_w + circle_r * math.sin(i * gap)
            y = center_h - circle_r * math.cos(i * gap)
            t.append((x, y))

        for i in range(count):
            for j in range(count):
                if self.graph.get_element(i, j) != 0:
                    if i == j:  # Петля
                        self.draw_loop(canvas, t[i], p_size)
                    else:
                        self.draw_lines(canvas, t, i, j, p_size)

        for i in range(count):
            x, y = t[i]
            canvas.create_oval(x - p_size, y - p_size, x + p_size, y + p_size, fill="white", outline="black")
            canvas.create_text(x, y, text=str(i + 1), font=font)

    def draw_loop(self, canvas, center, radius):
        x, y = center
        canvas.create_oval(x - 1*radius, y - 2*radius, x + 1*radius, y + 0*radius, outline="black")

    def draw_lines(self, canvas, t, i, j, radius):
        canvas.create_line(t[i], t[j], fill="black")
        self.draw_arrow(canvas, t[j][0] , t[j][1],  t[i][0] , t[i][1], radius )
       
    def draw_arrow(self,canvas, x0, y0, x1, y1, radius):
        arrow_length = 2*radius
        r = 3*radius
        vx = x1 - x0
        vy = y1 - y0
        length = math.sqrt(vx**2 + vy**2)
        vx_unit = vx / length
        vy_unit = vy / length
        x = x1 - r * vx_unit
        y = y1 - r * vy_unit
        dx = x0- x1
        dy = y0 - y1
        line_angle = math.atan2(dy, dx)
        end_x = x - arrow_length * math.cos(line_angle)
        end_y = y - arrow_length * math.sin(line_angle)
        arrow_angle = math.pi / 6  
        side_x1 = end_x + arrow_length * math.cos(line_angle + arrow_angle)
        side_y1 = end_y + arrow_length * math.sin(line_angle + arrow_angle)
        side_x2 = end_x + arrow_length * math.cos(line_angle - arrow_angle)
        side_y2 = end_y + arrow_length * math.sin(line_angle - arrow_angle)

        canvas.create_line(end_x, end_y, side_x1, side_y1, fill="black")
        canvas.create_line(end_x, end_y, side_x2, side_y2, fill="black")