# Legends, Titles and Labels

import matplotlib.pyplot as plt

x1 = [1, 2, 3]
y1 = [5, 6, 1]
x2 = [5, 1, 8]
y2 = [10, 14, 15]

plt.plot(x1, y1, label="First Line")
plt.plot(x2, y2, label="Second Line")

plt.xlabel("Plot Number")
plt.ylabel("Important Var")

plt.legend()

plt.title("Interesting Graph\nCheck it out")



plt.show()