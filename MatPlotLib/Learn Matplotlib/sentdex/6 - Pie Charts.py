# Pie Charts

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 2, 1]
working = [7, 8, 6, 5, 1]
playing = [8, 5, 1, 7, 6]

slices = [7, 2, 2, 13]
act = ["sleeping", "eating", "working", "playing"]

plt.pie(slices,
        labels=act,
        colors=["b", "c", "maroon", "purple"],
        startangle=40,
        shadow=True,
        explode=(0, 0.15, 0, 0),
        autopct="%1.1f%%")



plt.title("Scatter Plots")
plt.show()