import numpy as np
import tkinter as tk
import random

def normalize_vector(v):
    return v / np.linalg.norm(v)

def angle_between_two_vectors(v, u):
    v_norm = normalize_vector(v)
    u_norm = normalize_vector(u)
    dot = np.clip(np.dot(v_norm, u_norm), -1, 1)
    return np.degrees(np.arccos(dot))
    
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
        self.possible_directions_to_take = 100
        self.ticks_per_second = 5
        self.color = color
        self.gravity_slider = None
        self.priority_direction_slider = None

    def tick(self):
        x_position_before_moving = self.position.x
        y_position_before_moving = self.position.y

        self.move_randomly_and_update_pos()

        canvas.create_line(x_position_before_moving, y_position_before_moving, self.position.x, self.position.y, fill = self.color)

        root.after(1000 // self.ticks_per_second, self.tick)

    def move_randomly_and_update_pos(self):
        step = 180 / (self.possible_directions_to_take / 2)

        gravity_toward_prioritized_direction = self.gravity_slider.get() / 100

        angles = []
        for i in range(self.possible_directions_to_take):
            angles.append(-self.priority_direction_slider.get() + step * i)
            angles.append(-self.priority_direction_slider.get() - step * i)

        possible_directions = [(np.cos(np.radians(x)), np.sin(np.radians(x))) for x in angles]


        possible_directions_with_priority = possible_directions[:1 if gravity_toward_prioritized_direction == 1
        else int((1 - gravity_toward_prioritized_direction) * self.possible_directions_to_take)]

        self.direction = Vector2D(*possible_directions_with_priority[random.randint(0, len(possible_directions_with_priority) - 1)])

        canvas.move(self.shape, self.direction.x * self.step, self.direction.y * self.step)

        self.position.x += self.direction.x * self.step
        self.position.y += self.direction.y * self.step


root = tk.Tk()

x_window_size = 500
y_window_size = 500

canvas = tk.Canvas(root, width = x_window_size, height = y_window_size, background = 'black')
canvas.grid(row = 0, column = 1, rowspan = 10)

dot1 = RunningDot()

priority_direction_slider = tk.Scale(root, from_ = 0, to = 360, orient = 'horizontal', length = 200)
priority_direction_slider.grid(row = 0, column = 0)

gravity_slider = tk.Scale(root, from_ = 0, to = 100, orient = 'horizontal', length = 200)
gravity_slider.grid(row = 1, column = 0)

dot1.gravity_slider = gravity_slider
dot1.priority_direction_slider = priority_direction_slider
dot1.tick()

root.mainloop()
