import tkinter as tk

import time

def plot_point(canvas, x, y, color='black', size=3):
    """
    Plots a point on the canvas by drawing a small filled circle.

    x, y: coordinates of the center of the point.
    size: radius of the point.
    """
    x1 = x - size
    y1 = y - size
    x2 = x + size
    y2 = y + size

    # Draw the oval with the specified fill color
    canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)


# --- Main Application Setup ---
root = tk.Tk()
root.title("Plotting Points with root.update()")

# Create a Canvas widget
canvas_width = 400
canvas_height = 300
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack(padx=10, pady=10)

# --- Drawing with root.update() ---

# 1. Plot a large point
plot_point(canvas, x=50, y=50, color='red', size=5)

# Force the window to draw the point immediately
root.update()

time.sleep(2)

# 2. Plot a medium point
plot_point(canvas, x=150, y=100, color='blue', size=3)

# Force the window to draw the point immediately
root.update()

# 3. Plot many small points in a loop
import time  # Import time for a brief pause (optional, for visual effect)

for i in range(20):
    x_val = 200 + i * 5
    y_val = 150 + i * 3
    plot_point(canvas, x=x_val, y=y_val, color='darkgreen', size=1)

    # Update the display after each point.
    # Without this, all points would appear at once.
    root.update()
    # time.sleep(0.01) # Uncomment for a visible animation effect

# --- Keep the window open ---
# Since we didn't use root.mainloop(), the program will exit immediately 
# after all the drawing is done. To keep the window open so you can see 
# the final result, you must call mainloop() *at the very end*.






class graph:
    def __init__(self):
        # For Plotting
        self.x_vals = []
        self.y_vals = []

        # For graph setup
        self.x_axis_range = 10
        self.y_axis_range = 10

    def plot(self):
        for i in range(len(self.x_vals))
            plot_point(self.x_vals[i], self.y_vals[i])











