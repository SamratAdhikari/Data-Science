# Loading Data from Files

import matplotlib.pyplot as plt


# Part 1
'''
import csv

x = []
y = []

with open("examples.txt", "r") as f:
    plots = csv.reader(f, delimiter=",")
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, label="Loaded from File")
'''


# Part 2
import numpy as np

x, y = np.loadtxt("examples.txt", delimiter=",", unpack=True)

plt.plot(x, y, label="Loaded from File")


plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter Plots")
plt.legend()
plt.show()