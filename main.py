import numpy as np
import tkinter as tk
import random

import numpy.random


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
        self.possible_directions_to_take = 10
        self.gravity_toward_prioritized_direction = 0
        self.ticks_per_second = 20
        self.color = color

    def tick(self):
        x_position_before_moving = self.position.x
        y_position_before_moving = self.position.y

        self.move_randomly_and_update_pos()

        canvas.create_line(x_position_before_moving, y_position_before_moving, self.position.x, self.position.y, fill = self.color)

        root.after(1000 // self.ticks_per_second, self.tick)

    def move_randomly_and_update_pos(self, prioritized_direction = (1, 1)):
        possible_directions = []
        for i in range(self.possible_directions_to_take):
            possible_direction = normalize_vector((random.randint(-100, 100), random.randint(-100, 100)))

            possible_directions.append(possible_direction)

        new_direction = Vector2D(*possible_directions[0])

        for i in range(len(possible_directions)):
            for j in range(len(possible_directions)):
                if (angle_between_two_vectors(possible_directions[i], prioritized_direction)
                    < angle_between_two_vectors(possible_directions[j], prioritized_direction)):
                        possible_directions[i], possible_directions[j] = possible_directions[j], possible_directions[i]

        possible_directions_with_priority = possible_directions[:1 if self.gravity_toward_prioritized_direction == 1
        else int((1 - self.gravity_toward_prioritized_direction) * self.possible_directions_to_take)]

        self.direction = Vector2D(*possible_directions_with_priority[random.randint(0, len(possible_directions_with_priority) - 1)])

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
