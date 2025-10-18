import line_profiler
import numpy as np
import random

def normalize_vector(v):
    return v / np.linalg.norm(v)

def angle_between_two_vectors(v, u):
    v_norm = normalize_vector(v)
    u_norm = normalize_vector(u)
    dot = np.clip(np.dot(v_norm, u_norm), -1, 1)
    return np.degrees(np.arccos(dot))

def move_randomly_and_update_pos(self, prioritized_direction=(1, 1)):
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

profiler1 = line_profiler.LineProfiler()
profiler1(avg_rating1)()
profiler1.print_stats()