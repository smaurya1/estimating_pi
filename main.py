# Estimating the value of Pi using the Monte Carlo method

import random
import numpy as np

n = 1000


def estimate_pi(trials):
    avg = np.array([])
    for num in range(trials):
        points = np.array([])
        for i in range(n):
            pts = (np.random.uniform(1, -1), np.random.uniform(-1, 1))
            points = np.append(points, pts)
        points_in_circ = np.array([])
        for i in range(0, len(points), 2):
            x = points[i]
            y = points[i + 1]
            distance = x ** 2 + y ** 2
            if distance <= 1:
                points_in_circ = np.append(points_in_circ, [x, y])
        pi = 4 * (len(points_in_circ) / len(points))
        avg = np.append(avg, pi)

    pi_avg = np.mean(avg)
    return pi_avg


prnt_pi = estimate_pi(500)
print(prnt_pi)
