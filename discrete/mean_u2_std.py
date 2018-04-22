import math

x = [0, 1975, 2800, 3000]
px = [0.11, 0.11, 0.17, 0.61]

mean = 0
for xx, ppx in zip(x, px):
    mean += xx * ppx

mean = round(mean, 2)
print("mean", mean)
u2 = 0
for xx, ppx in zip(x, px):
    u2 += math.pow(xx - mean, 2) * ppx

print("u2", u2)
print("std", math.sqrt(u2))