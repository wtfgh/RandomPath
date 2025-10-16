import tkinter as tk

root = tk.Tk()

x_window_size = 500
y_window_size = 500

canvas = tk.Canvas(root, width = x_window_size, height = y_window_size, background = 'black')
canvas.pack()

canvas.create_line(200, 200, 300, 300, fill = 'white')

root.mainloop()