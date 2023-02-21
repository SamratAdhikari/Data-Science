# Bar Charts and Histograms

import matplotlib.pyplot as plt


# Bar Charts
# x1 = [2, 4, 6, 8, 10]
# y1 = [1, 5, 3, 4, 6]
#
# x2 = [1, 2, 3, 4, 5]
# y2 = [9, 8, 7, 6, 5]
#
# plt.bar(x1, y1, label="Bar1", color="red")
# plt.bar(x2, y2, label="Bar2", color="c")


# Histogarm
popu = [18, 20, 21, 25, 23, 29, 24, 27, 26, 30, 35, 31, 36, 69, 99, 140, 101]
# ids = [x for x in range(len(popu))]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
plt.hist(popu, bins, histtype="bar", rwidth=0.8)

plt.xlabel("x")
plt.ylabel("y")

plt.title("Bar Chart and Histograms")

plt.legend()

plt.show()