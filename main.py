# Estimating the value of Pi using the Monte Carlo method

import random

n = 1000
runs = 0
num_pts_in_circ = 0
avg = []
points = []
points_in_circ = []

while runs <= 1000:
    runs += 1
    for i in range(n):
        pts = (random.uniform(1, -1), random.uniform(-1, 1))
        points.append(pts)

    for i in points:
        x = i[0]
        y = i[1]
        distance = x**2 + y**2
        if distance <= 1:
            points_in_circ.append(i)

    pi = 4 * (len(points_in_circ) / len(points))
    avg.append(pi)
    points.clear()
    points_in_circ.clear()

pi_avg = sum(avg)/len(avg)
print(pi_avg)




