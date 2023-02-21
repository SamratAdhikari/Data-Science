# Scatter Plots

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [5, 6, 3, 1, 9, 2, 2, 9, 9]

plt.scatter(x, y, label="skitcat", color="red", marker="*", s=500)


plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter Plots")
plt.legend()
plt.show()