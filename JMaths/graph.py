
"""
As of today I realized just exporting to Excel to the libre equivalint would be vastly superipr

# jg.graph([-10, 10], [-10, 10])
# jg.root.mainloop()
"""

import tkinter as tk

# --- Main Application Setup ---
root = tk.Tk()
root.title("JMaths")

# Create a Canvas widget
canvas_width = 800
canvas_height = 800
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="#ffe98f")
canvas.pack(padx=10, pady=10)

class graph:
    def __init__(self, x_scale, y_scale):
        # For Plotting
        self.x_vals = []
        self.y_vals = []

        self.canvas = canvas
        if isinstance(x_scale, list) and isinstance(y_scale, list):
            self.x_min = x_scale[0]
            self.x_man = x_scale[1]
            self.y_min = y_scale[0]
            self.y_max = y_scale[1]

        self.canvas.create_line(canvas_width / 2, canvas_height, canvas_width / 2, 0, fill="#32b3fa")
        self.canvas.create_line(canvas_width, canvas_height / 2, 0, canvas_height / 2, fill="#32b3fa")

