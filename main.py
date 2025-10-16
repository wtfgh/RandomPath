import numpy as np
import tkinter as tk
import random

def normalize_a_vector(v):
    m = np.linalg.norm(v)
    return v / m

class Vector2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class RunningDot:
    def __init__(self, size = 5, step = 5, color = 'white'):
        self.position = Vector2D(x_window_size / 2, y_window_size / 2)
        self.shape = canvas.create_oval(self.position.x - size / 2, self.position.y - size / 2,
                                        self.position.x + size / 2, self.position.y + size / 2, fill = color)
        self.step = step
        self.direction = Vector2D()
        self.ticks_per_second = 20

    def tick(self):
        self.direction = Vector2D(*normalize_a_vector((random.random() * 10 - 5, random.random() * 10 - 5)))

        x_position_before_moving = self.position.x
        y_position_before_moving = self.position.y

        self.move_self_and_update_pos()

        canvas.create_line(x_position_before_moving, y_position_before_moving, self.position.x, self.position.y, fill='white')

        root.after(1000 // self.ticks_per_second, self.tick)

    def move_self_and_update_pos(self):
        canvas.move(self.shape, self.direction.x * self.step, self.direction.y * self.step)
        self.position.x += self.direction.x * self.step
        self.position.y += self.direction.y * self.step


root = tk.Tk()

x_window_size = 500
y_window_size = 500

canvas = tk.Canvas(root, width = x_window_size, height = y_window_size, background = 'black')
canvas.pack()

dot1 = RunningDot()
dot1.tick()

root.mainloop()


