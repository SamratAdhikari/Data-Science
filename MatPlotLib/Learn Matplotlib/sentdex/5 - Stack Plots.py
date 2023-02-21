# Stack Plots

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 2, 1]
working = [7, 8, 6, 5, 1]
playing = [8, 5, 1, 7, 6]


# For labels in stackplot
plt.plot([], [], color="m", label="Sleeping", linewidth=5)
plt.plot([], [], color="c", label="Eating", linewidth=5)
plt.plot([], [], color="r", label="Working", linewidth=5)
plt.plot([], [], color="k", label="Playing", linewidth=5)
plt.stackplot(days, sleeping, eating, working, playing, colors=["pink", "cyan", "red", "black"])

plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter Plots")
plt.legend()
plt.show()